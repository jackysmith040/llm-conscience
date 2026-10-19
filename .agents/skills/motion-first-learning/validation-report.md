# Motion-First Learning Skill Validation Report

## Structural validation

The package passed the official skill validator:

`python /home/ubuntu/skills/skill-creator/scripts/quick_validate.py motion-first-learning`

Result: **Skill is valid.**

## Representative behavior checks

| Test | Expected behavior | Status |
|---|---|---|
| Explain Docker images and containers | Build a state-transition model, use motion or staged frames, then test reconstruction and transfer | Designed and covered by core instructions |
| Explain recursion or another algorithm | Show changing states such as call stack, execution flow, or returned values; avoid static definition-only teaching | Designed and covered |
| Convert dense notes into a chapter | Separate Tutorial, How-to, Reference, Explanation, and Exercises; divide large material into stable subsections | Designed and covered |
| Analyze a supplied educational video | Extract visual teaching patterns, identify meaningful motion, reconstruct a slower storyboard, and distinguish source facts from analysis | Designed and covered |
| Learner struggles or reads slowly | Move through REFLECT/ADAPT/REPAIR, reduce scene granularity, add pauses and prerequisites, preserve standards | Designed and covered |
| Long session or context pressure | Create PAUSE_CHECKPOINT, reload Learning State Packet, run continuity handshake, and recover without improvisation | Designed and covered |
| Better instructional pattern discovered | OBSERVE_PATTERN → FORM_HYPOTHESIS → TEST_POLICY → PROMOTE_POLICY or ROLLBACK_POLICY; promotion is scope-limited and evidence-gated | Designed and covered |
| Faulty explanation or source mismatch | Contain, return to validated state, verify, rebuild smallest segment, retest | Designed and covered |
| Session close | Export only approved progress summary, delete temporary adapter/evidence, verify cleanup where possible | Designed and covered |

## Package contents

- `SKILL.md`
- `references/learning-science-evidence.md`
- `references/diataxis-learning-contract.md`
- `references/visualization-patterns.md`
- `references/adaptive-controller.md`

## Important scope decision

The permanent skill is not permitted to rewrite itself during an ordinary learning session. It can discover candidate improvements and promote them within temporary scope. A permanent core-skill change requires an explicit, separately reviewed update.
