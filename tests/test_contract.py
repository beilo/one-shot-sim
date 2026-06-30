from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT


def read(relative_path: str) -> str:
    return (SKILL_ROOT / relative_path).read_text(encoding="utf-8")


class OneShotSimContractTest(unittest.TestCase):
    def test_skill_references_every_stage_rule_file(self) -> None:
        skill = read("SKILL.md")

        for stage in ("brainstorm", "confirm", "plan", "execute", "finish"):
            reference = f"references/{stage}.md"
            with self.subTest(reference=reference):
                self.assertIn(reference, skill)
                self.assertTrue((SKILL_ROOT / reference).is_file())

    def test_confirm_keeps_public_name_and_requires_four_part_gate(self) -> None:
        skill = read("SKILL.md")
        confirm = read("references/confirm.md")

        self.assertIn('<stage id="confirm" name="执行确认">', skill)
        self.assertIn("confirm 执行确认", skill)
        self.assertIn("confirm 执行确认", confirm)

        for label in ("PRD", "research", "阻塞问题", "下一步"):
            with self.subTest(label=label):
                self.assertIn(label, confirm)

        self.assertIn("用户明确确认可以进入 `plan`", confirm)

    def test_task_first_flow_removes_no_task_execution_branch(self) -> None:
        skill = read("SKILL.md")
        plan = read("references/plan.md")
        execute = read("references/execute.md")
        finish = read("references/finish.md")

        self.assertIn("创建或定位 planning task", skill)
        self.assertRegex(plan, r"`?plan`? 不创建 task")
        self.assertIn("只支持 task-backed 路径", execute)
        self.assertIn("必须存在 active task", finish)

        forbidden = (
            "进入 no-task",
            "不创建 task：进入",
            "no-task `execute",
            "no-task 收尾",
        )
        combined = "\n".join((skill, plan, execute, finish))
        for phrase in forbidden:
            with self.subTest(phrase=phrase):
                self.assertNotIn(phrase, combined)

    def test_old_no_task_mentions_are_only_blockers(self) -> None:
        files = {
            "SKILL.md": read("SKILL.md"),
            "references/confirm.md": read("references/confirm.md"),
            "references/plan.md": read("references/plan.md"),
            "references/execute.md": read("references/execute.md"),
            "references/finish.md": read("references/finish.md"),
        }

        allowed_patterns = (
            re.compile(r"旧 no-task 状态"),
            re.compile(r"不支持 no-task 路径"),
            re.compile(r"不走 no-task 路径"),
        )

        for path, text in files.items():
            for line in text.splitlines():
                if "no-task" not in line:
                    continue
                with self.subTest(path=path, line=line):
                    self.assertTrue(
                        any(pattern.search(line) for pattern in allowed_patterns),
                        line,
                    )


if __name__ == "__main__":
    unittest.main()
