"""Session-scoped candidate policy records; no Core mutation."""
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Any

@dataclass
class PatternCandidate:
    pattern_id: str
    hypothesis: str
    candidate_policy: dict[str, Any]
    predicted_effect: str
    scope: str = "candidate"
    evidence: list[dict[str, Any]] | None = None
    status: str = "candidate"
    rollback_condition: str = "later evidence contradicts the predicted effect"

    def to_dict(self) -> dict[str, Any]: return asdict(self)

def propose_adaptation(pattern_id: str, observations: list[dict[str, Any]], hypothesis: str, candidate_policy: dict[str, Any], predicted_effect: str) -> PatternCandidate:
    if not observations: raise ValueError("At least one observation is required")
    return PatternCandidate(pattern_id, hypothesis, candidate_policy, predicted_effect, evidence=observations)

def promote_adaptation(candidate: PatternCandidate, evidence: list[dict[str, Any]], scope: str) -> PatternCandidate:
    if not evidence: raise ValueError("Promotion requires evidence")
    candidate = PatternCandidate(**candidate.to_dict())
    candidate.evidence = (candidate.evidence or []) + evidence
    candidate.scope, candidate.status = scope, "promoted"
    return candidate

def rollback_adaptation(candidate: PatternCandidate, reason: str) -> PatternCandidate:
    candidate = PatternCandidate(**candidate.to_dict())
    candidate.status, candidate.scope = "rolled_back", "candidate"
    candidate.rollback_condition = reason
    return candidate
