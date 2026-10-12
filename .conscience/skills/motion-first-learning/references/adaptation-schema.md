# Adaptation schema

A candidate teaching improvement must include:

```json
{
  "pattern_id": "stable temporary identifier",
  "observations": [],
  "hypothesis": "what may improve, for whom, and under what conditions",
  "candidate_policy": {},
  "predicted_effect": "observable expected benefit",
  "comparison_method": "how prior and candidate methods will be compared",
  "evidence": [],
  "confidence": "low|medium|high",
  "scope": "candidate|lesson|session|domain|core-proposal",
  "status": "candidate|promoted|rolled_back",
  "rollback_condition": "condition that invalidates the policy"
}
```

Promotion requires observable evidence such as improved reconstruction, delayed retrieval, transfer, fewer repeated errors, or greater independence. Core-skill proposals require explicit user review. Ordinary sessions may create, test, and roll back candidates but may not rewrite Core code.
