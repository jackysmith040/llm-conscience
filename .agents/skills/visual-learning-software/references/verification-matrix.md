# Verification Matrix

Use this matrix before saving a checkpoint. Record failures in `todo.md` and do not deliver an experience with known broken core navigation.

| Area | Verify | Evidence |
| --- | --- | --- |
| Source fidelity | Definitions, examples, and theorem statements match the provided source | Page or section trace in content data or project notes |
| Learning sequence | Visual, definition, example, review, and quiz states exist for every zone | Screenshot plus content audit |
| Navigation | Every tab, back button, next button, retry action, and weak-topic link changes state correctly | Interaction test or deterministic code path |
| Quiz scope | Local quiz only selects the active zone; mock exam is clearly separate | Question-bank selection logic |
| Feedback | Every answer has an explanation and a route back to review after a miss | UI inspection |
| Difficulty | Questions progress from recall to understanding to application or exam reasoning | Difficulty labels and ordering |
| Timing | Countdown starts, decrements, signals urgency, submits or locks correctly at zero | Timer test |
| Analytics | Score, unanswered items, time used, zone accuracy, and priorities calculate correctly | Deterministic calculation check |
| Accessibility | Buttons are keyboard reachable, focus-visible, readable against backgrounds, and labels are meaningful | Responsive screenshot and DOM review |
| Responsiveness | Lesson, quiz, and results layouts work at desktop and mobile widths | Screenshot pass |
| Technical health | Type-check, build, dev-server, and browser console checks pass | Command output and logs |
| Delivery | Checkpoint exists and user receives only the intended project attachment | Checkpoint version ID |

## Minimum interaction pass

Run through one representative zone completely: open the zone, switch each tab, proceed through the review, answer correctly, answer incorrectly and recover, complete the local question bank, enter the mock exam, submit with an unanswered item, click a weak-topic recommendation, and verify that the target zone opens at its visual starting point.

If full browser automation is unavailable, implement deterministic state logic, run type-checking, inspect logs, and capture screenshots. Tell the user which interaction checks were automated and which require their manual confirmation.
