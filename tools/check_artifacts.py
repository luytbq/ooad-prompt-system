#!/usr/bin/env python3
"""Kiểm tra hình thức các artifact trong thư mục đầu ra của pipeline.

Chỉ đọc, không sửa file nào. Chỉ dùng thư viện chuẩn.

    python3 tools/check_artifacts.py <THU_MUC_DAU_RA> [--json] [--strict]

Mã thoát: 0 khi không có LOI, 1 khi có LOI (--strict tính cả CANH_BAO), 2 khi sai tham số.
"""
import argparse
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict

LOI = "LOI"
CANH_BAO = "CANH_BAO"

TEMP_TRACES = re.compile(r"mã tạm(?! thời)|\bQ-[UP]\d+[AB]?-(?:\d+|xx|nn)\b", re.I)
PROCESS_WORDS = re.compile(r"diakempt|classlayout|subagent|orchestrator|\bacpx\b|file \.bak", re.I)
FORBIDDEN_CHARS = re.compile("[—←→↔⇐⇒➜]")
REF = re.compile(r"(?<![\w-])(Q|ASM|BR|NFR|REQ|UC)-(\d+)\b")
REQ_RANGE = re.compile(r"REQ-(\d+)\s+đến\s+REQ-(\d+)")
BEND = re.compile(r"\(\s*(-?\d+(?:\.\d+)?)\s*,\s*(-?\d+(?:\.\d+)?)\s*\)")
INPUT_VERSION = re.compile(r"([\w./-]+\.md)\s+(\d+)\.(\d+)")
BR_STATUS = re.compile(r"^(Hiệu lực|Gộp vào BR-\d+|Loại( \(.*\))?)$")
SAME_QUESTION_MIN_OVERLAP = 0.3
NON_ACTION_TARGETS = {"ActivityFinal", "Merge", "Join", "Note", "Partition", "InterruptibleRegion"}
CONTROL_FREE_SOURCES = {"Decision", "Fork", "Note", "Partition", "InterruptibleRegion"}
DECIDERS = {"Bên nghiệp vụ", "Nhóm dự án"}

# P02R và X1 được phép gán mã tạm cho phần tử của bản đang review.
TEMP_CODE_ALLOWED = re.compile(r"^(P02R|X1)-")


class Report:
    def __init__(self):
        self.items = []

    def add(self, severity, code, path, line, message):
        self.items.append(
            {"severity": severity, "code": code, "path": path, "line": line, "message": message}
        )


class Doc:
    def __init__(self, rel, text):
        self.rel = rel
        self.name = os.path.basename(rel)
        self.lines = text.splitlines()
        self.fenced = fenced_mask(self.lines)


def fenced_mask(lines):
    mask, inside = [], False
    for line in lines:
        if line.lstrip().startswith("```"):
            inside = not inside
            mask.append(True)
        else:
            mask.append(inside)
    return mask


def split_row(line):
    s = line.strip()
    if not s.startswith("|"):
        return None
    s = s[1:-1] if s.endswith("|") and len(s) > 1 else s[1:]
    return [c.strip() for c in re.split(r"(?<!\\)\|", s)]


def is_separator(cells):
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", c) for c in cells)


def tables(doc, start=0, end=None):
    """Trả về danh sách (header, [(số dòng 1-based, cells)]) trong khoảng [start, end)."""
    end = len(doc.lines) if end is None else end
    found, i = [], start
    while i < end - 1:
        head = split_row(doc.lines[i]) if not doc.fenced[i] else None
        sep = split_row(doc.lines[i + 1])
        if head and sep and is_separator(sep):
            rows, j = [], i + 2
            while j < end:
                cells = split_row(doc.lines[j])
                if cells is None:
                    break
                rows.append((j + 1, cells))
                j += 1
            found.append((head, rows))
            i = j
        else:
            i += 1
    return found


def headings(doc):
    out = []
    for i, line in enumerate(doc.lines):
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m and not doc.fenced[i]:
            out.append((i, len(m.group(1)), m.group(2).strip()))
    return out


def section(doc, pattern):
    heads = headings(doc)
    for k, (i, level, title) in enumerate(heads):
        if re.match(pattern, title):
            end = len(doc.lines)
            for j, lv, _ in heads[k + 1 :]:
                if lv <= level:
                    end = j
                    break
            return i + 1, end
    return None


def load_docs(root):
    docs = []
    for base, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for f in sorted(files):
            if f.endswith(".md"):
                path = os.path.join(base, f)
                with open(path, encoding="utf-8", errors="replace") as fh:
                    docs.append(Doc(os.path.relpath(path, root), fh.read()))
    return docs


def is_review(doc):
    return doc.name.startswith("_review")


def is_artifact(doc):
    if doc.name.startswith("_"):
        return False
    parts = doc.rel.split(os.sep)
    if len(parts) == 1:
        return bool(re.match(r"^(P\d\d[ab]?|X\d)-", doc.name))
    return parts[0] in ("P04-uc-specs", "P07-uc-analysis") and doc.name.startswith("UC-")


def is_spec(doc):
    return doc.rel.startswith("P04-uc-specs" + os.sep) and doc.name.startswith("UC-")


def find(docs, prefix):
    return next((d for d in docs if d.name.startswith(prefix) and os.sep not in d.rel), None)


def header_value(doc, key):
    for head, rows in tables(doc, 0, min(len(doc.lines), 30)):
        for no, cells in [(1, head)] + rows:
            if len(cells) >= 2 and cells[0] == key:
                return no, cells[1]
    return None, None


def check_text(docs, report):
    for d in docs:
        if is_review(d):
            continue
        for i, line in enumerate(d.lines):
            if FORBIDDEN_CHARS.search(line):
                report.add(LOI, "K02", d.rel, i + 1, "Có em dash hoặc mũi tên Unicode (C2)")
            if "{{PH:" in line and not d.fenced[i]:
                report.add(LOI, "K13", d.rel, i + 1, "Còn placeholder chưa điền (C6)")
            if not is_artifact(d) and not d.name.startswith("_"):
                continue
            if TEMP_TRACES.search(line) and not TEMP_CODE_ALLOWED.match(d.name):
                report.add(LOI, "K01", d.rel, i + 1, "Còn dấu vết mã tạm (C10): " + line.strip()[:90])
            if PROCESS_WORDS.search(line):
                report.add(CANH_BAO, "K03", d.rel, i + 1, "Artifact nhắc tới quá trình chạy (C5): " + line.strip()[:90])


def check_frame(docs, report):
    required = ("Câu hỏi mở", "Đề xuất sửa artifact trước", "Vấn đề còn mở")
    for d in filter(is_artifact, docs):
        heads = headings(d)
        h1 = sum(1 for _, level, _t in heads if level == 1)
        if h1 != 1:
            report.add(LOI, "K04", d.rel, 1, f"Có {h1} tiêu đề cấp 1, cần đúng một (C8)")
        titles = {t for _, _, t in heads}
        for name in required:
            if not any(t.startswith(name) for t in titles):
                report.add(LOI, "K04", d.rel, 1, f'Thiếu mục "{name}" (C5)')
        if header_value(d, "Phiên bản")[1] is None:
            report.add(LOI, "K04", d.rel, 1, "Thiếu hàng Phiên bản ở khối thông tin (C5)")


def control_rows(doc, title_pattern):
    span = section(doc, title_pattern)
    if not span:
        return []
    out = []
    for head, rows in tables(doc, *span):
        out.extend((head, no, cells) for no, cells in rows)
    return out


def check_codes(docs, report):
    seen = defaultdict(list)
    for d in filter(is_artifact, docs):
        for head, no, cells in control_rows(d, r"^Câu hỏi mở") + control_rows(d, r"^Giả định"):
            if re.fullmatch(r"(Q|ASM)-\d+", cells[0]):
                seen[cells[0]].append((d.rel, no, cells[1] if len(cells) > 1 else ""))
            if "Người quyết" in head:
                k = head.index("Người quyết")
                if k < len(cells) and cells[k] not in DECIDERS:
                    report.add(LOI, "K16", d.rel, no, f'{cells[0]}: Người quyết phải là "Bên nghiệp vụ" hoặc "Nhóm dự án"')
    for code, places in seen.items():
        files = {p[0] for p in places}
        first = words(places[0][2])
        # Artifact tổng hợp được chép lại câu hỏi; chỉ hai nội dung khác hẳn nhau mới là cấp trùng mã.
        if len(files) > 1 and any(overlap(first, words(p[2])) < SAME_QUESTION_MIN_OVERLAP for p in places[1:]):
            where = ", ".join(sorted(files))
            report.add(LOI, "K05", places[0][0], places[0][1], f"{code} được cấp cho các nội dung khác nhau: {where}")


def words(text):
    return set(re.findall(r"\w+", text.lower()))


def overlap(a, b):
    return len(a & b) / len(a | b) if a | b else 1.0


def first_cell_codes(doc, prefix):
    pattern = re.compile(rf"^{prefix}-\d+")
    codes = set()
    for _, rows in tables(doc):
        for _, cells in rows:
            m = pattern.match(cells[0])
            if m:
                codes.add(m.group(0))
    return codes


def defined_codes(docs):
    defined = {}
    p00, p02, p06 = find(docs, "P00-"), find(docs, "P02-"), find(docs, "P06-")
    if p00:
        defined["REQ"] = first_cell_codes(p00, "REQ")
    if p02:
        defined["UC"] = first_cell_codes(p02, "UC")
    register = next((d for d in docs if d.name == "_BR-register.md"), None)
    if register or p06:
        defined["BR"] = set()
        for d in filter(None, (register, p06)):
            defined["BR"] |= first_cell_codes(d, "BR")
    if p06:
        defined["NFR"] = first_cell_codes(p06, "NFR")
    # Câu hỏi có thể được cấp ở file phụ của lô chạy hoặc file review.
    defined["Q"], defined["ASM"] = set(), set()
    for d in docs:
        defined["Q"] |= first_cell_codes(d, "Q")
        defined["ASM"] |= first_cell_codes(d, "ASM")
    return defined


def check_refs(docs, report):
    defined = defined_codes(docs)
    for d in docs:
        if is_review(d) or not (is_artifact(d) or d.name.startswith("_")):
            continue
        reported = set()
        for i, line in enumerate(d.lines):
            for kind, num in REF.findall(line):
                code = f"{kind}-{num}"
                if kind in defined and code not in defined[kind] and code not in reported:
                    reported.add(code)
                    report.add(CANH_BAO, "K06", d.rel, i + 1, f"{code} được dẫn nhưng không tìm thấy nơi định nghĩa")


def check_register(docs, report):
    register = next((d for d in docs if d.name == "_BR-register.md"), None)
    if not register:
        return
    seen = set()
    all_codes = first_cell_codes(register, "BR")
    for head, rows in tables(register):
        if "Trạng thái" not in head:
            continue
        k = head.index("Trạng thái")
        for no, cells in rows:
            if cells[0] in seen:
                report.add(LOI, "K07", register.rel, no, f"{cells[0]} trùng trong sổ BR")
            seen.add(cells[0])
            value = cells[k] if k < len(cells) else ""
            if not BR_STATUS.match(value):
                report.add(LOI, "K07", register.rel, no, f'{cells[0]}: trạng thái "{value}" ngoài tập cho phép (P04 F7.4)')
            m = re.match(r"Gộp vào (BR-\d+)", value)
            if m and m.group(1) not in all_codes:
                report.add(LOI, "K07", register.rel, no, f"{cells[0]} gộp vào {m.group(1)} không có trong sổ")


def check_versions(docs, report):
    current = {}
    for d in docs:
        value = header_value(d, "Phiên bản")[1]
        m = re.match(r"(\d+)\.(\d+)", value or "")
        if m:
            current[d.name] = (int(m.group(1)), int(m.group(2)))
    for d in filter(is_artifact, docs):
        no, value = header_value(d, "Đầu vào đã dùng")
        if not value:
            continue
        for path, major, minor in INPUT_VERSION.findall(value):
            name = os.path.basename(path)
            used = (int(major), int(minor))
            if name != d.name and name in current and used < current[name]:
                report.add(CANH_BAO, "K09", d.rel, no, f"Dùng {name} {major}.{minor}, bản hiện hành {current[name][0]}.{current[name][1]}")


def check_spec_tables(d, report):
    span = section(d, r"^9\.")
    if not span:
        return
    nodes, edges = {}, []
    for head, rows in tables(d, *span):
        if head[:2] == ["ID", "Loại"]:
            for no, cells in rows:
                if cells[0] in nodes:
                    report.add(LOI, "K10", d.rel, no, f"Node {cells[0]} trùng ID")
                nodes[cells[0]] = cells[1] if len(cells) > 1 else ""
        elif len(head) > 2 and head[1:3] == ["Nguồn", "Đích"]:
            kind = head.index("Loại quan hệ") if "Loại quan hệ" in head else None
            label = next((i for i, h in enumerate(head) if h.startswith("Nhãn")), None)
            bend = head.index("Điểm uốn") if "Điểm uốn" in head else None
            for no, cells in rows:
                get = lambda k: cells[k] if k is not None and k < len(cells) else ""
                edges.append((no, cells[0], cells[1], cells[2], get(kind), get(label), get(bend)))
    if not nodes or not edges:
        return
    incoming, outgoing = defaultdict(list), defaultdict(list)
    off_grid = []
    for no, eid, src, dst, kind, label, bend in edges:
        for end in (src, dst):
            if end not in nodes:
                report.add(LOI, "K10", d.rel, no, f"Cạnh {eid} trỏ tới node không tồn tại: {end}")
        if any(float(x) % 10 or float(y) % 10 for x, y in BEND.findall(bend)):
            off_grid.append((no, eid))
        if kind == "ControlFlow":
            incoming[dst].append((no, eid))
            outgoing[src].append((no, eid, label))
    if off_grid:
        report.add(CANH_BAO, "K10", d.rel, off_grid[0][0], f"{len(off_grid)} cạnh có điểm uốn không là bội số của 10, đầu tiên là {off_grid[0][1]}")
    for nid, kind in nodes.items():
        if len(incoming[nid]) > 1 and kind not in NON_ACTION_TARGETS and kind != "Decision":
            ids = ", ".join(e for _, e in incoming[nid])
            report.add(LOI, "K10", d.rel, incoming[nid][0][0], f"Node {nid} có nhiều cạnh vào ({ids}), phải đi qua Merge (join ngầm theo UML)")
        if len(outgoing[nid]) > 1 and kind not in CONTROL_FREE_SOURCES:
            report.add(LOI, "K10", d.rel, outgoing[nid][0][0], f"Node {nid} có nhiều cạnh ra, phải đi qua Decision hoặc Fork")
        if kind == "Decision":
            out = outgoing[nid]
            if len(out) < 2:
                report.add(LOI, "K10", d.rel, out[0][0] if out else 1, f"Decision {nid} cần ít nhất hai cạnh ra")
            guards = [g for _, _, g in out]
            for no, eid, guard in out:
                if not re.fullmatch(r"\[.+\]", guard):
                    report.add(LOI, "K10", d.rel, no, f"Cạnh {eid} ra từ {nid} thiếu guard trong ngoặc vuông")
            for guard, n in Counter(guards).items():
                if n > 1 and guard:
                    report.add(LOI, "K10", d.rel, out[0][0], f"Decision {nid} có guard trùng: {guard}")


def expand_reqs(text):
    found = set(re.findall(r"(?<![\w-])REQ-\d+", text))
    for a, b in REQ_RANGE.findall(text):
        width = len(a)
        found |= {f"REQ-{n:0{width}d}" for n in range(int(a), int(b) + 1)}
    return found


def check_spec_body(d, report):
    no, declared = header_value(d, "REQ")
    span1 = section(d, r"^1\.")
    if span1:
        for head, rows in tables(d, *span1):
            for line_no, cells in [(span1[0], head)] + rows:
                if len(cells) > 1 and cells[0] == "REQ":
                    no, declared = line_no, cells[1]
    main = section(d, r"^2\.")
    alt = section(d, r"^3\.")
    steps = set()
    for span in filter(None, (main, alt, section(d, r"^4\."))):
        for _, rows in tables(d, *span):
            steps |= {cells[0] for _, cells in rows}
    if main:
        for head, rows in tables(d, *main):
            for line_no, cells in rows:
                if re.search(r"(?<!\w)nếu(?!\w)", " ".join(cells), re.I):
                    report.add(LOI, "K12", d.rel, line_no, f'Bước {cells[0]} của luồng chính có "nếu" (Target 5)')
    if alt:
        for i in range(*alt):
            for target in re.findall(r"Quay lại bước ([0-9]+[a-z0-9]*)", d.lines[i]):
                if target not in steps:
                    report.add(LOI, "K12", d.rel, i + 1, f"Quay lại bước {target} không tồn tại")
    if declared is None:
        return
    allowed = expand_reqs(declared)
    start = main[0] if main else 0
    stop_span = section(d, r"^9\.")
    stop = stop_span[0] - 1 if stop_span else len(d.lines)
    used = {}
    for i in range(start, stop):
        for req in expand_reqs(d.lines[i]):
            used.setdefault(req, i + 1)
    for req, line_no in sorted(used.items()):
        if req not in allowed:
            report.add(CANH_BAO, "K11", d.rel, line_no, f"{req} được dẫn trong đặc tả nhưng thiếu ở hàng REQ (F1)")


def check_specs(docs, report, concurrency_on):
    for d in filter(is_spec, docs):
        for head, no, cells in control_rows(d, r"^6\."):
            if "Trong sổ BR" in head:
                k = head.index("Trong sổ BR")
                if k < len(cells) and cells[k] not in ("Mới", "Đã có"):
                    report.add(LOI, "K08", d.rel, no, f'{cells[0]}: "{cells[k]}" ngoài tập Mới, Đã có (F7.3)')
        check_spec_tables(d, report)
        check_spec_body(d, report)
        if concurrency_on and not any("Thao tác nguyên tử" in line for line in d.lines):
            report.add(CANH_BAO, "K14", d.rel, 1, "Hồ sơ bật TRANH_CHAP_TAI_NGUYEN nhưng đặc tả chưa có bảng Thao tác nguyên tử (M1)")


def check_profile(docs, report):
    """Trả về True khi hồ sơ bật mô-đun đồng thời."""
    profile = next((d for d in docs if d.name == "project-profile.md"), None)
    if not profile:
        return False
    values = {}
    line_of = {}
    for _, rows in tables(profile):
        for no, cells in rows:
            if len(cells) > 1:
                values[cells[0]] = cells[1]
                line_of[cells[0]] = no
    if find(docs, "P09-"):
        for key in ("NEN_TANG", "CONG_NGHE"):
            if "Chưa chốt" in values.get(key, ""):
                report.add(CANH_BAO, "K13", profile.rel, line_of[key], f"{key} vẫn Chưa chốt dù đã có P09 (cập nhật theo F11)")
    value = values.get("TRANH_CHAP_TAI_NGUYEN", "Không").strip()
    return bool(value) and not value.startswith(("Không", "{{"))


def check_register_ac(docs, report):
    register = next((d for d in docs if d.name == "_AC-register.md"), None)
    if not register:
        return
    responsibilities = defaultdict(set)
    seen = set()
    owners = {}
    for head, rows in tables(register):
        if head and head[0] == "AC":
            k = head.index("Trách nhiệm") if "Trách nhiệm" in head else None
            for no, cells in rows:
                if cells[0] in seen:
                    report.add(LOI, "K17", register.rel, no, f"{cells[0]} trùng trong sổ trách nhiệm")
                seen.add(cells[0])
                if k is not None and k < len(cells):
                    responsibilities[cells[0]] |= set(re.findall(r"//\s*(\w+)", cells[k]))
        elif head and head[0].startswith("Điều kiện"):
            for no, cells in rows:
                if cells[0] in owners:
                    report.add(LOI, "K17", register.rel, no, f'"{cells[0]}" có hai dòng, mỗi điều kiện chỉ một nơi định nghĩa')
                owners[cells[0]] = no
    for d in docs:
        if not (d.rel.startswith("P07-uc-analysis" + os.sep) and d.name.startswith("UC-")):
            continue
        for head, rows in tables(d):
            if head[:2] == ["AC", "Stereotype"] and "Trách nhiệm" in head:
                k = head.index("Trách nhiệm")
                for no, cells in rows:
                    for name in re.findall(r"//\s*(\w+)", cells[k] if k < len(cells) else ""):
                        if name not in responsibilities[cells[0]]:
                            report.add(CANH_BAO, "K17", d.rel, no, f"{cells[0]}.{name} chưa có trong sổ trách nhiệm")


def check_leftovers(root, report):
    for base, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for f in files:
            rel = os.path.relpath(os.path.join(base, f), root)
            if f.endswith(".bak"):
                report.add(LOI, "K15", rel, 1, "File sao lưu còn sót")
            elif f.endswith(".pending.md"):
                report.add(CANH_BAO, "K15", rel, 1, "Chưa gộp vào sổ dùng chung, chạy X3 (C10)")
            elif f.endswith(".drawio"):
                check_drawio(os.path.join(base, f), rel, report)


def check_drawio(path, rel, report):
    try:
        tree = ET.parse(path)
    except ET.ParseError as exc:
        report.add(LOI, "K18", rel, 1, f"XML không hợp lệ: {exc}")
        return
    off_grid = 0
    for page, diagram in enumerate(tree.getroot().iter("diagram"), 1):
        model = diagram.find("mxGraphModel")
        if model is None:
            report.add(LOI, "K18", rel, 1, f"Trang {page} bị nén hoặc thiếu mxGraphModel (C7.3)")
            continue
        ids = [c.get("id") for c in model.iter("mxCell")]
        for missing in {"0", "1"} - set(ids):
            report.add(LOI, "K18", rel, 1, f'Trang {page} thiếu cell gốc id="{missing}"')
        for cid, n in Counter(ids).items():
            if n > 1:
                report.add(LOI, "K18", rel, 1, f"Trang {page}: cell {cid} trùng ID")
        known = set(ids)
        for cell in model.iter("mxCell"):
            for attr in ("source", "target"):
                ref = cell.get(attr)
                if ref and ref not in known:
                    report.add(LOI, "K18", rel, 1, f"Trang {page}: cạnh {cell.get('id')} trỏ tới {ref} không tồn tại")
            geometry = cell.find("mxGeometry")
            if geometry is not None and cell.get("vertex") == "1" and geometry.get("relative") != "1":
                if any(float(geometry.get(attr, "0")) % 10 for attr in ("x", "y")):
                    off_grid += 1
    if off_grid:
        report.add(CANH_BAO, "K18", rel, 1, f"{off_grid} node có toạ độ không là bội số của 10")


def run(root):
    report = Report()
    docs = load_docs(root)
    concurrency_on = check_profile(docs, report)
    for check in (check_text, check_frame, check_codes, check_refs, check_register, check_versions, check_register_ac):
        check(docs, report)
    check_specs(docs, report, concurrency_on)
    check_leftovers(root, report)
    report.items.sort(key=lambda r: (r["severity"] != LOI, r["path"], r["line"], r["code"]))
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description="Kiểm tra hình thức artifact của pipeline.")
    parser.add_argument("root", help="THU_MUC_DAU_RA của dự án")
    parser.add_argument("--json", action="store_true", help="xuất JSON")
    parser.add_argument("--strict", action="store_true", help="CANH_BAO cũng làm mã thoát khác 0")
    args = parser.parse_args(argv)
    if not os.path.isdir(args.root):
        print(f"Không tìm thấy thư mục: {args.root}", file=sys.stderr)
        return 2
    report = run(args.root)
    counts = Counter(r["severity"] for r in report.items)
    if args.json:
        print(json.dumps(report.items, ensure_ascii=False, indent=2))
    else:
        for r in report.items:
            print(f'{r["severity"]} {r["code"]} {r["path"]}:{r["line"]} {r["message"]}')
        print(f"Tổng: {counts[LOI]} LOI, {counts[CANH_BAO]} CANH_BAO")
    failed = counts[LOI] or (args.strict and counts[CANH_BAO])
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
