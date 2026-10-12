---
name: vibesec
description: >-
  Security auditing and vulnerability scanning skill for AI-generated code, application security,
  and secrets detection. Trigger: /vibesec.
---

# /vibesec

Audits AI-generated code for common security pitfalls, vulnerabilities, and secret leakage.

## Core Checks
1. **Secret Leakage**: Hardcoded API keys, JWT secrets, database credentials, internal endpoints.
2. **Injection Vulnerabilities**: SQL injection, command execution, template injection, eval patterns.
3. **Authentication & Authorization**: Missing policy checks, IDOR, improper session validation.
4. **Data Handling & Privacy**: Sensitive PII exposure, unvalidated deserialization, insecure cryptographic defaults.
5. **Dependency Audit**: Known CVEs, outdated packages, unpinned dependencies.

## Output Structure
- Executive Summary of posture.
- High, Medium, Low vulnerability breakdown with remediation diffs.
- Verifiable remediation test cases.
