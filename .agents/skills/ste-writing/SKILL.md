---
name: ste-writing
description: >-
  Rewrite prose (docs, READMEs, PRs, comments) into ASD-STE100 Simplified Technical English
  to eliminate AI slop, passive voice, and conversational bloat. Trigger: /ste-writing.
---

# /ste-writing

Write prose in ASD-STE100 Simplified Technical English. Applies to documentation, READMEs, pull requests, error messages, and comments.

## Rules
- **Words**: One word for one thing. Use short common words: *start* (not initiate), *use* (not utilize/leverage), *help* (not facilitate), *make sure* (not ensure), *before* (not prior to). No marketing adjectives (*seamless, robust, cutting-edge*).
- **Verbs**: Active voice only. Use action verbs directly ("analyze the log", not "perform an analysis"). No stacked auxiliaries.
- **Sentences**: Max 20 words per instruction, max 25 words descriptive. No contractions.
- **Punctuation**: No semicolons. Split into two clear sentences.
- **Structure**: One topic per paragraph, max 6 sentences. Use numbered vertical lists for procedures.

## Self-Lint Checklist
1. Sentence over 20 words? Split it.
2. Semicolon? Replace with a period.
3. Contraction? Expand it.
4. Passive voice? Make it active.
5. Nominalization ("perform an analysis") or phrasal verb ("spin up")? Replace with a simple verb.
