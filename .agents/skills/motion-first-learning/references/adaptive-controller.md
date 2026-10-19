# Adaptive controller reference

## State record

Maintain: `session_id`, `domain_adapter_version`, `current_state`, `objective`, `evidence`, `mastery_layer`, `allowed_transitions`, `transition_history`, `candidate_policy`, `validated_policy`, `checkpoint_id`, `unresolved_questions`, and `next_action`.

## State machine

Core path:

`INIT → ORIENT → DIAGNOSE → MODEL → TUTORIAL → PRACTICE → RETRIEVE → TRANSFER → MASTERED`

Supporting states:

`REFLECT`, `ADAPT`, `REPAIR`, `CONSOLIDATE`, `PAUSE_CHECKPOINT`, `RECOVER`, `CLOSE_CLEANUP`, `OBSERVE_PATTERN`, `FORM_HYPOTHESIS`, `TEST_POLICY`, `PROMOTE_POLICY`, `ROLLBACK_POLICY`.

Use explicit guards based on evidence. Prevent invalid transitions, infinite loops, and premature mastery. After repeated failure with one intervention, force a representation change or prerequisite diagnosis.

## Pattern registry

For every candidate improvement, record:

- pattern ID;
- observed learner or instructional context;
- hypothesis;
- predicted effect;
- candidate policy;
- comparison method;
- evidence collected;
- confidence and scope;
- promotion decision;
- rollback condition.

## Promotion ladder

`candidate → local lesson → session → domain adapter → core-skill proposal`

Promote only when the relevant evidence threshold is met. A core-skill proposal always requires explicit user review; ordinary sessions cannot edit the permanent skill.

## Checkpoint schema

A checkpoint should contain the objective, current state, last completed task, next task, concept graph delta, source identifiers, terminology changes, learner evidence, adaptations, open risks, adapter version, and resume instruction. Mark each item as source-derived, learner-derived, inferred, verified, or uncertain.

## Recovery

On interruption or context drift:

1. load the newest validated checkpoint;
2. run a continuity handshake;
3. compare current assumptions with checkpoint assumptions;
4. route conflicts to `REPAIR`;
5. resume only after a small orientation or recall check.

## Cleanup

At close, export only an explicitly approved progress summary. Delete the temporary adapter, raw evidence, candidate policies, and temporary artifacts. Verify deletion where possible and report limitations honestly.
