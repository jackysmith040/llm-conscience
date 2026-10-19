# Content Model

Use typed data so educational content stays separate from rendering logic. Keep source references on every high-stakes claim whenever the source format allows it.

```ts
type LearningZone = {
  id: string;
  title: string;
  prerequisites: string[];
  visual: string;
  definition: string;
  examples: {
    label: string;
    explanation: string;
    sourceSection?: string;
  }[];
  reviewSteps: string[];
  commonMistakes: string[];
  masteryRule: {
    minimumAccuracy: number;
    requiredSteps: string[];
  };
  questionBank: Question[];
};

type Question = {
  id: string;
  prompt: string;
  answers: string[];
  correct: number;
  explanation: string;
  hint: string;
  difficulty: "Recall" | "Understand" | "Apply" | "Exam move";
  skillTag: string;
  sourceSection?: string;
};
```

## Modeling rules

A zone should contain at least one visual mental model, one precise definition or rule, one anchor example, two nearby examples, four review steps, three questions at increasing difficulty, and an explicit recovery path after a miss. Do not hide important assumptions in the explanation. For proof-heavy subjects, represent hypotheses and conclusion separately so the interface can display a theorem checklist.

Keep generated variants distinct from source-derived questions. A variant may change numbers, objects, or wording, but it must preserve the same skill tag and include a fresh explanation. Avoid placing the correct option in a fixed position.

## Selection rules

Use the active zone ID to select local practice. Use skill tags to build performance summaries. Use prerequisite IDs to determine whether to recommend a prior zone rather than simply marking a learner as wrong. Reserve cross-zone questions for a deliberate diagnostic or mock-exam mode.
