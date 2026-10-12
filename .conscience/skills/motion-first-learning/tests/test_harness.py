import json
import tempfile
import unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parents[1] / "scripts"))
from core.state_machine import StateMachine
from core.state_store import create_session, create_checkpoint, resume_from_checkpoint, cleanup_session
from core.visualize import route
from core.documentation import check_freshness
from plugins.adaptation import propose_adaptation, promote_adaptation, rollback_adaptation
from plugins.manim_plugin import plan_render, command

class HarnessTests(unittest.TestCase):
    def test_valid_and_invalid_transition(self):
        sm = StateMachine(); state = create_session("learn", "demo")
        result = sm.apply(state, "configured")
        self.assertTrue(result.ok); self.assertEqual(result.state["current_state"], "ORIENT")
        bad = sm.apply(result.state, "not-real")
        self.assertFalse(bad.ok)

    def test_checkpoint_round_trip_and_cleanup(self):
        with tempfile.TemporaryDirectory() as d:
            state = create_session("learn", "demo")
            state["current_state"] = "MODEL"
            create_checkpoint(state, d)
            resumed = resume_from_checkpoint(d)
            self.assertTrue(resumed["ok"])
            (Path(d) / "adapter").mkdir(); (Path(d) / "evidence").mkdir()
            report = cleanup_session(d, {"completed": ["MODEL"]})
            self.assertTrue(report["verified"])

    def test_visual_route(self):
        with tempfile.TemporaryDirectory() as d:
            result = route("state_machine", {"title":"Flow", "nodes":[{"id":"a","label":"A"},{"id":"b","label":"B"}], "edges":[{"source":"a","target":"b","label":"next"}]}, d)
            self.assertTrue(result["ok"])
            self.assertIn("a", Path(result["source"]).read_text())
            self.assertTrue(Path(result["accessible_text"]).exists())

    def test_adaptation_and_manim(self):
        c = propose_adaptation("p1", [{"result":"better"}], "hypothesis", {"pause":True}, "better recall")
        self.assertEqual(promote_adaptation(c, [{"transfer":True}], "session").status, "promoted")
        self.assertEqual(rollback_adaptation(c, "failed").status, "rolled_back")
        plan = plan_render("scene.py", "out")
        self.assertEqual(plan.quality, "preview"); self.assertIn("-ql", command(plan))

    def test_documentation_freshness(self):
        with tempfile.TemporaryDirectory() as d:
            src = Path(d) / "x.py"; docs = Path(d) / "docs.md"
            src.write_text("def public_api(): pass\n", encoding="utf-8"); docs.write_text("public_api\n", encoding="utf-8")
            self.assertTrue(check_freshness([src], docs)["ok"])

if __name__ == "__main__": unittest.main()
