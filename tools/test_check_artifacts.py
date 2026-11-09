import contextlib
import io
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(__file__))
import check_artifacts as ca

P00 = """# P00 - Yêu cầu - X

| Thuộc tính | Giá trị |
|---|---|
| Phiên bản | 1.2 |

| Mã | Câu |
|---|---|
| REQ-01 | a |
| REQ-02 | b |

## Câu hỏi mở
| Mã | Câu hỏi | Ảnh hưởng tới | Nguồn gây mơ hồ | Người quyết | Đề xuất |
|---|---|---|---|---|---|
| Q-01 | Hỏi gì | UC-001 | REQ-01 | Bên nghiệp vụ | A |

## Đề xuất sửa artifact trước
Không có

## Vấn đề còn mở
Không có
"""

P02 = P00.replace("# P00", "# P02").replace("REQ-01 | a", "UC-001 | a").replace("| REQ-02 | b |\n", "").replace("| Q-01 ", "| Q-02 ")

SPEC = """# P04 - UC-001 - X

| Thuộc tính | Giá trị |
|---|---|
| Phiên bản | 1.0 |
| Đầu vào đã dùng | P00-problem-brief.md 1.2 |

## 1. Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| REQ | REQ-01 |

## 2. Luồng sự kiện chính

| STT | Thực hiện bởi | Hành động |
|---|---|---|
| 1 | Khách | Chọn phòng (REQ-01) |
| 2 | Hệ thống | Giữ phòng |

## 3. Luồng sự kiện thay thế và ngoại lệ

| STT | Điều kiện | Hành động | Quay lại / Kết thúc |
|---|---|---|---|
| 2a | Hết phòng | Báo hết | Quay lại bước 1 |

## 6. Quy tắc nghiệp vụ

| BR | Quy tắc | Loại | Bước áp dụng | REQ | Trong sổ BR |
|---|---|---|---|---|---|
| BR-01 | r | Ràng buộc | 2 | REQ-01 | Mới |

## 9. Activity diagram

Bảng Node

| ID | Loại | Nhãn | Stereotype | Thuộc về (container) | Bước UC | Ghi chú |
|---|---|---|---|---|---|---|
| INIT | Initial | - | - | P-SYS | - | - |
| A-1 | Action | a | - | P-SYS | 1 | - |
| D-2 | Decision | - | - | P-SYS | 2 | - |
| FINAL-1 | ActivityFinal | - | - | P-SYS | - | - |

Bảng Edge

| ID | Nguồn | Đích | Loại quan hệ | Nhãn / multiplicity | Ghi chú | Điểm uốn |
|---|---|---|---|---|---|---|
| E-01 | INIT | A-1 | ControlFlow | - | - | - |
| E-02 | A-1 | D-2 | ControlFlow | - | - | (150,260) |
| E-03 | D-2 | FINAL-1 | ControlFlow | [còn] | - | - |
| E-04 | D-2 | FINAL-1 | ControlFlow | [hết] | - | - |

## Câu hỏi mở
Không có

## Đề xuất sửa artifact trước
Không có

## Vấn đề còn mở
Không có
"""

REGISTER = """# Sổ

| BR | Quy tắc | Loại | UC áp dụng | REQ | Cấp lần đầu tại | Trạng thái | Ghi chú |
|---|---|---|---|---|---|---|---|
| BR-01 | r | Ràng buộc | UC-001 | REQ-01 | P04 UC-001 | Hiệu lực | - |
"""

GOOD_DRAWIO = """<mxfile><diagram name="a"><mxGraphModel><root><mxCell id="0"/><mxCell id="1" parent="0"/>
<mxCell id="n1" vertex="1" parent="1"><mxGeometry x="10" y="20" as="geometry"/></mxCell>
</root></mxGraphModel></diagram></mxfile>"""


class CheckArtifactsTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = tmp.name
        self.write("P00-problem-brief.md", P00)
        self.write("P02-usecases.md", P02)
        self.write("P04-uc-specs/UC-001-book.md", SPEC)
        self.write("P04-uc-specs/_BR-register.md", REGISTER)
        self.write("diagrams/P04-activity-UC-001.drawio", GOOD_DRAWIO)

    def write(self, rel, text):
        path = os.path.join(self.root, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)

    def edit_spec(self, old, new):
        self.assertIn(old, SPEC)
        self.write("P04-uc-specs/UC-001-book.md", SPEC.replace(old, new))

    def codes(self, severity=None):
        return [r["code"] for r in ca.run(self.root).items if severity in (None, r["severity"])]

    def test_clean_project_has_no_findings(self):
        self.assertEqual(ca.run(self.root).items, [])

    def test_temporary_code_is_an_error(self):
        self.edit_spec("| Khách | Chọn phòng", "| Khách | Chọn phòng theo mã tạm Q-U001-xx")
        self.assertIn("K01", self.codes(ca.LOI))

    def test_review_prompts_may_keep_temporary_codes(self):
        self.write("P02R-review.md", P00.replace("# P00", "# P02R").replace("a |", "Mã tạm A1 |").replace("Q-01", "Q-09"))
        self.assertNotIn("K01", self.codes())

    def test_em_dash_is_an_error(self):
        self.edit_spec("Giữ phòng", "Giữ — phòng")
        self.assertIn("K02", self.codes(ca.LOI))

    def test_process_notes_warn(self):
        self.edit_spec("Không có\n\n## Vấn đề còn mở\nKhông có", "Không có\n\n## Vấn đề còn mở\nĐã chạy diakempt")
        self.assertIn("K03", self.codes(ca.CANH_BAO))

    def test_missing_control_section_is_an_error(self):
        self.edit_spec("## Vấn đề còn mở\nKhông có\n", "")
        self.assertIn("K04", self.codes(ca.LOI))

    def test_same_question_code_with_different_text_is_an_error(self):
        self.write("P02-usecases.md", P02.replace("| Q-02 | Hỏi gì", "| Q-01 | Khác"))
        self.assertIn("K05", self.codes(ca.LOI))

    def test_rephrased_copy_of_a_question_is_not_a_conflict(self):
        self.write("P00-problem-brief.md", P00.replace("Hỏi gì", "Khách có được hoàn tiền khi huỷ phòng không"))
        self.write("P02-usecases.md", P02.replace("| Q-02 | Hỏi gì", "| Q-01 | Khách có được hoàn tiền khi huỷ phòng trước hạn không"))
        self.assertNotIn("K05", self.codes())

    def test_artifact_listing_its_own_previous_version_is_not_stale(self):
        self.write("P00-problem-brief.md", P00.replace("| Phiên bản | 1.2 |", "| Phiên bản | 1.2 |\n| Đầu vào đã dùng | P00-problem-brief.md 1.1 |"))
        self.assertNotIn("K09", self.codes())

    def test_removed_rule_may_name_its_replacement(self):
        self.write("P04-uc-specs/_BR-register.md", REGISTER.replace("Hiệu lực", "Loại (thay bởi BR-02)"))
        self.assertNotIn("K07", self.codes())

    def test_temporary_as_an_ordinary_word_is_allowed(self):
        self.edit_spec("Giữ phòng", "Giữ phòng bằng mã tạm thời của cổng")
        self.assertNotIn("K01", self.codes())

    def test_off_grid_nodes_are_summarised_per_file(self):
        cells = "".join(f'<mxCell id="v{i}" vertex="1" parent="1"><mxGeometry x="15" y="20" as="geometry"/></mxCell>' for i in range(5))
        self.write("diagrams/c.drawio", GOOD_DRAWIO.replace("</root>", cells + "</root>"))
        self.assertEqual(self.codes().count("K18"), 1)

    def test_invalid_decider_is_an_error(self):
        self.write("P00-problem-brief.md", P00.replace("Bên nghiệp vụ", "Ai đó"))
        self.assertIn("K16", self.codes(ca.LOI))

    def test_dangling_reference_warns(self):
        self.edit_spec("Giữ phòng", "Giữ phòng (BR-99)")
        self.assertIn("K06", self.codes(ca.CANH_BAO))

    def test_invalid_register_status_is_an_error(self):
        self.write("P04-uc-specs/_BR-register.md", REGISTER.replace("Hiệu lực", "Đề xuất (chờ Q-01)"))
        self.assertIn("K07", self.codes(ca.LOI))

    def test_invalid_register_marker_in_spec_is_an_error(self):
        self.edit_spec("| REQ-01 | Mới |", "| REQ-01 | Mới (sổ chung) |")
        self.assertIn("K08", self.codes(ca.LOI))

    def test_stale_input_version_warns(self):
        self.edit_spec("P00-problem-brief.md 1.2", "P00-problem-brief.md 1.1")
        self.assertIn("K09", self.codes(ca.CANH_BAO))

    def test_implicit_join_is_an_error(self):
        self.edit_spec("| E-04 | D-2 | FINAL-1 | ControlFlow | [hết] | - | - |", "| E-04 | D-2 | A-1 | ControlFlow | [hết] | - | - |")
        self.assertIn("K10", self.codes(ca.LOI))

    def test_decision_edge_without_guard_is_an_error(self):
        self.edit_spec("| ControlFlow | [hết] |", "| ControlFlow | - |")
        self.assertIn("K10", self.codes(ca.LOI))

    def test_bend_point_off_grid_warns(self):
        self.edit_spec("(150,260)", "(155,260)")
        self.assertIn("K10", self.codes(ca.CANH_BAO))

    def test_requirement_missing_from_header_warns(self):
        self.edit_spec("| 2 | Hệ thống | Giữ phòng |", "| 2 | Hệ thống | Giữ phòng (REQ-02) |")
        self.assertIn("K11", self.codes(ca.CANH_BAO))

    def test_requirement_range_in_header_covers_members(self):
        self.edit_spec("| REQ | REQ-01 |", "| REQ | REQ-01 đến REQ-02 |")
        self.write("P04-uc-specs/UC-001-book.md", SPEC.replace("| REQ | REQ-01 |", "| REQ | REQ-01 đến REQ-02 |").replace("Giữ phòng |", "Giữ phòng (REQ-02) |"))
        self.assertNotIn("K11", self.codes())

    def test_conditional_in_main_flow_is_an_error(self):
        self.edit_spec("| Hệ thống | Giữ phòng |", "| Hệ thống | Giữ phòng nếu còn |")
        self.assertIn("K12", self.codes(ca.LOI))

    def test_return_to_unknown_step_is_an_error(self):
        self.edit_spec("Quay lại bước 1", "Quay lại bước 7")
        self.assertIn("K12", self.codes(ca.LOI))

    def test_undecided_stack_after_architecture_warns(self):
        self.write("project-profile.md", "| Trường | Giá trị |\n|---|---|\n| CONG_NGHE | Chưa chốt |\n")
        self.write("P09-architecture.md", P00.replace("# P00", "# P09").replace("Q-01", "Q-07"))
        self.assertIn("K13", self.codes(ca.CANH_BAO))

    def test_concurrency_profile_requires_atomic_table(self):
        self.write("project-profile.md", "| Trường | Giá trị |\n|---|---|\n| TRANH_CHAP_TAI_NGUYEN | Có: phòng |\n")
        self.assertIn("K14", self.codes(ca.CANH_BAO))

    def test_concurrency_off_does_not_require_atomic_table(self):
        self.write("project-profile.md", "| Trường | Giá trị |\n|---|---|\n| TRANH_CHAP_TAI_NGUYEN | Không |\n")
        self.assertNotIn("K14", self.codes())

    def test_leftover_backup_is_an_error(self):
        self.write("diagrams/a.drawio.bak", "x")
        self.assertIn("K15", self.codes(ca.LOI))

    def test_pending_register_warns(self):
        self.write("P04-uc-specs/_BR-register.UC-002.pending.md", "# Sổ\n")
        self.assertIn("K15", self.codes(ca.CANH_BAO))

    def test_responsibility_missing_from_register_warns(self):
        self.write("P07-uc-analysis/_AC-register.md", "# Sổ\n\n| AC | Stereotype | Tên | Trách nhiệm |\n|---|---|---|---|\n| AC-E-Room | entity | Room | // holdRoom: giữ |\n")
        analysis = P00.replace("# P00", "# P07").replace("Q-01", "Q-05") + "\n| AC | Stereotype | Tên | Trách nhiệm |\n|---|---|---|---|\n| AC-E-Room | entity | Room | // holdRoom: giữ<br>// reserveRoom: giữ |\n"
        self.write("P07-uc-analysis/UC-001-book-analysis.md", analysis)
        messages = [r["message"] for r in ca.run(self.root).items if r["code"] == "K17"]
        self.assertEqual(len(messages), 1)
        self.assertIn("reserveRoom", messages[0])

    def test_shared_condition_with_two_owners_is_an_error(self):
        self.write("P07-uc-analysis/_AC-register.md", "# Sổ\n\n| Điều kiện hoặc sự kiện | Lớp |\n|---|---|\n| Còn hiệu lực | A |\n| Còn hiệu lực | B |\n")
        self.assertIn("K17", self.codes(ca.LOI))

    def test_invalid_drawio_is_an_error(self):
        self.write("diagrams/b.drawio", "<mxfile>")
        self.assertIn("K18", self.codes(ca.LOI))

    def test_compressed_diagram_is_an_error(self):
        self.write("diagrams/b.drawio", "<mxfile><diagram>eJxz</diagram></mxfile>")
        self.assertIn("K18", self.codes(ca.LOI))

    def test_edge_to_unknown_cell_is_an_error(self):
        self.write("diagrams/b.drawio", GOOD_DRAWIO.replace('<mxCell id="n1"', '<mxCell id="e1" edge="1" target="zz"/><mxCell id="n1"'))
        self.assertIn("K18", self.codes(ca.LOI))

    def test_exit_code_reflects_errors_and_strict_mode(self):
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(ca.main([self.root]), 0)
            self.edit_spec("(150,260)", "(155,260)")
            self.assertEqual(ca.main([self.root]), 0)
            self.assertEqual(ca.main([self.root, "--strict"]), 1)
            self.edit_spec("Giữ phòng", "Giữ — phòng")
            self.assertEqual(ca.main([self.root]), 1)

    def test_missing_directory_returns_usage_error(self):
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(ca.main([os.path.join(self.root, "khong-co")]), 2)


if __name__ == "__main__":
    unittest.main()
