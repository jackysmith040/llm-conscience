"""Deterministic state-machine kernel for motion-first learning sessions."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Callable

STATES = {
    "INIT", "ORIENT", "DIAGNOSE", "MODEL", "TUTORIAL", "PRACTICE",
    "RETRIEVE", "TRANSFER", "REFLECT", "ADAPT", "REPAIR", "CONSOLIDATE",
    "PAUSE_CHECKPOINT", "RECOVER", "MASTERED", "CLOSE_CLEANUP",
    "OBSERVE_PATTERN", "FORM_HYPOTHESIS", "TEST_POLICY", "PROMOTE_POLICY",
    "ROLLBACK_POLICY",
}

@dataclass
class Transition:
    source: str
    event: str
    destination: str
    guard: str = "always"
    evidence_required: tuple[str, ...] = ()
    checkpoint: bool = False

@dataclass
class TransitionResult:
    ok: bool
    state: dict[str, Any]
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

DEFAULT_TRANSITIONS = [
    Transition("INIT", "configured", "ORIENT"),
    Transition("ORIENT", "target_defined", "DIAGNOSE"),
    Transition("DIAGNOSE", "baseline_ready", "MODEL"),
    Transition("MODEL", "model_validated", "TUTORIAL"),
    Transition("TUTORIAL", "state_change_explained", "PRACTICE"),
    Transition("PRACTICE", "supported_task_passed", "RETRIEVE"),
    Transition("RETRIEVE", "reconstruction_passed", "TRANSFER", ("reconstruction",)),
    Transition("RETRIEVE", "bottleneck_found", "REFLECT"),
    Transition("TRANSFER", "variation_passed", "MASTERED", ("transfer",)),
    Transition("TRANSFER", "brittle_performance", "REFLECT"),
    Transition("REFLECT", "adaptation_needed", "ADAPT"),
    Transition("REFLECT", "repair_needed", "REPAIR"),
    Transition("ADAPT", "candidate_ready", "TUTORIAL"),
    Transition("REPAIR", "repair_validated", "RETRIEVE"),
    Transition("MASTERED", "next_target", "ORIENT"),
    Transition("MASTERED", "session_end", "CLOSE_CLEANUP"),
    Transition("CONSOLIDATE", "checkpoint_written", "MASTERED"),
    Transition("PAUSE_CHECKPOINT", "checkpoint_written", "RECOVER"),
    Transition("RECOVER", "continuity_passed", "REFLECT"),
    Transition("RECOVER", "conflict_found", "REPAIR"),
    Transition("OBSERVE_PATTERN", "pattern_specific", "FORM_HYPOTHESIS"),
    Transition("FORM_HYPOTHESIS", "hypothesis_testable", "TEST_POLICY"),
    Transition("TEST_POLICY", "candidate_validated", "PROMOTE_POLICY"),
    Transition("TEST_POLICY", "candidate_failed", "ROLLBACK_POLICY"),
    Transition("PROMOTE_POLICY", "scope_selected", "REFLECT"),
    Transition("ROLLBACK_POLICY", "previous_restored", "REFLECT"),
]

class StateMachine:
    def __init__(self, transitions: list[Transition] | None = None, retry_limit: int = 3):
        self.transitions = transitions or DEFAULT_TRANSITIONS
        self.retry_limit = retry_limit

    def allowed(self, state: str, event: str | None = None) -> list[Transition]:
        result = [t for t in self.transitions if t.source == state]
        return [t for t in result if event is None or t.event == event]

    def apply(self, state: dict[str, Any], event: str, evidence: dict[str, Any] | None = None) -> TransitionResult:
        evidence = evidence or {}
        current = state.get("current_state")
        if current not in STATES:
            return TransitionResult(False, state, [f"Unknown current state: {current}"])
        candidates = self.allowed(current, event)
        if not candidates:
            return TransitionResult(False, state, [f"Invalid transition: {current} --{event}--> ?"])
        transition = candidates[0]
        missing = [key for key in transition.evidence_required if not evidence.get(key)]
        if missing:
            return TransitionResult(False, state, [f"Missing evidence: {', '.join(missing)}"])
        history = list(state.get("transition_history", []))
        history.append({"from": current, "event": event, "to": transition.destination, "evidence": evidence})
        new_state = dict(state)
        new_state["current_state"] = transition.destination
        new_state["transition_history"] = history
        new_state["retry_counts"] = dict(state.get("retry_counts", {}))
        return TransitionResult(True, new_state)

    def inspect(self, state: dict[str, Any]) -> dict[str, Any]:
        current = state.get("current_state")
        return {"ok": current in STATES, "current_state": current,
                "allowed_events": [t.event for t in self.allowed(current)],
                "history_length": len(state.get("transition_history", [])),
                "retry_limit": self.retry_limit}
