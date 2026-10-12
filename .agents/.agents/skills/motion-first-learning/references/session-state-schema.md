# Session state schema

## Required state fields

```json
{
  "schema_version": "1.0",
  "session_id": "stable identifier",
  "domain": "subject",
  "objective": "target outcome",
  "learner_profile": {},
  "current_state": "INIT",
  "adapter_version": "baseline",
  "mastery": {},
  "evidence": [],
  "transition_history": [],
  "unresolved_questions": [],
  "next_action": "resume instruction"
}
```

## Checkpoint fields

Add `checkpoint_label`, `checkpointed_at`, source identifiers, concept-graph changes, terminology changes, adaptations, risks, and resume instructions. Mark claims as `source-derived`, `learner-derived`, `inferred`, `verified`, or `uncertain`.

## Cleanup report

A cleanup result must contain `ok`, `removed`, `summary_path`, `verified`, `errors`, and `warnings`. Cleanup must be explicit; never delete a session merely because a state transition occurred.
