# Human Oversight and AI Verification Framework

## Workflow: routing and drafting responses to public-service enquiries

**Purpose.** Help a public-service contact centre identify the responsible service team, retrieve approved guidance, and prepare a draft response. The AI may assist staff; it does not determine a person's eligibility, entitlement, legal status, or priority for scarce services.

**Basis.** This operational framework adapts the NIST AI RMF lifecycle functions (Govern, Map, Measure, Manage) and the UNESCO principles of proportionality, privacy, traceability, human oversight, and remedy.[1][2] It must be applied alongside the Nigeria Data Protection Act 2023 and relevant sector rules.[3]

## 1. Risk tier and authority

| Tier | Examples in this workflow | System authority | Required control |
|---|---|---|---|
| Low | Categorize a public, non-personal FAQ; retrieve an approved public page | May label or retrieve; cannot send a message | Staff can inspect source and correct routing; sample review each week |
| Moderate | Classify a citizen enquiry; draft a routine response from current official guidance | May suggest a queue and draft; cannot send or change a record | Staff approval before sending; show cited source, confidence/abstention, and date; review all early pilot outputs |
| High | Enquiry involving benefits, health, safety, legal rights, identity documents, a complaint, appeal, or a threat of harm | No autonomous decision, prioritization, rejection, or adverse action | Immediate trained human review; specialist referral when needed; preserve original wording and timestamps |
| Prohibited for this system | Determine eligibility, deny a benefit, diagnose, make a law-enforcement referral, or close a complaint without staff decision | No authority | Remove capability; technical and procedural block |

Risk follows the possible harm, not the model's claimed confidence. Confidence scores are not proof of correctness. A high-confidence output can still be wrong.

## 2. Before use: authorize and verify

1. Name a service owner accountable for outcomes, a system owner for operation, a data protection contact, and a staff lead for escalations. Record the approved purpose and forbidden uses in the system inventory.
2. Map data flows and legal basis. Minimize personal data; redact identity numbers and unrelated details before model input where possible. Document every processor, storage location, retention period, transfer mechanism, and deletion route. Complete required privacy and impact assessments.
3. Maintain an approved, versioned knowledge source. Each response draft must link to the passage used, with its publication or review date. If no current source is found, the system must abstain and route to staff.
4. Test with representative, consented or synthetic enquiries across languages, code-switching, spelling variation, accessibility needs, and high-risk edge cases. Test routing accuracy, unsupported claims, privacy leakage, security, latency, and subgroup gaps. An independent reviewer signs off before the pilot.
5. Train staff to check the source and meaning, reject unsuitable drafts, recognize automation bias, explain delays, and use manual procedures. Staff must have time and authority to override the system without penalty.

## 3. During use: decision and approval gates

The system may perform reversible internal steps: suggest a category, retrieve approved content, and draft a response. It must display that content is AI-assisted, quote or link the source, mark uncertainty, and preserve the original enquiry. The system may not send a response, modify a citizen record, infer eligibility, or close a case.

For moderate-risk cases, an authorized staff member checks that the draft answers the actual question, cites current policy, does not invent a requirement or promise, and is understandable in the requested language. The staff member approves, edits, or rejects the draft; approval is an affirmative action recorded against their identity. For high-risk cases, staff review the original enquiry and make the decision themselves; AI output is optional background only. Where specialist judgment is necessary, route to the appropriate professional. Where the system cannot understand a language or user intent, it must preserve the original and route for language-capable review.

## 4. Required records

Record, with access controls and retention limits: system and model version; prompt/configuration version; knowledge-base version and retrieved source identifiers; timestamp; input reference (store the original only where lawful and necessary); proposed category and draft; uncertainty or abstention state; automated checks; staff reviewer and approval/edit/rejection; final action; escalation reason; and incident or appeal reference. Do not log chain-of-thought or unnecessary sensitive text. Keep logs tamper-evident and searchable for authorized audit, correction, and incident response. Tell users when AI assistance materially shapes a response and provide a human contact and complaint route.

## 5. Failure handling and safe fallback

Trigger a safe fallback when the source is missing, outdated, contradictory, or not retrievable; the model abstains or produces an unsupported statement; a language or subgroup metric breaches its threshold; a security or privacy event is suspected; or staff identify a harmful or repeated error. Stop automated drafting for the affected task, retain the case in the ordinary queue, and do not discard or overwrite the citizen's original message.

Staff report the issue to the service owner. The system owner preserves relevant version and event records, disables the affected model or feature if needed, and switches to the documented manual process. The data protection contact assesses notification and response duties for a personal-data breach. The owner informs affected people when appropriate, offers correction or appeal, and records remediation. Re-enable only after root-cause analysis, corrected testing, and sign-off by the service owner and independent reviewer. Serious incidents go to the responsible oversight body under applicable law and policy.

## 6. Monitoring and review

During the pilot, review every AI-assisted draft before sending and sample the underlying routing. After launch, continue full review of high-risk cases, weekly review of a stratified moderate-risk sample, and monthly reporting of routing accuracy, unsupported-draft rate, staff override and correction rates, language-level performance, response time, complaints, privacy/security incidents, and review time. Set thresholds before deployment with the service owner; pause if a threshold is breached or if monitoring data are inadequate. Reassess after a model, prompt, data, workflow, or policy change and at least quarterly. Publish a plain-language summary of purpose, limits, performance, complaints, and corrective actions.

## 7. Accountability and sign-off

| Role | Accountable action |
|---|---|
| Service owner | Approves use, thresholds, staffing, manual fallback, and restart after an incident |
| System owner | Versions components, operates access/logging, monitors performance, and executes rollback |
| Frontline reviewer | Checks source and draft, decides whether to send, records edits, and escalates |
| Data protection contact | Reviews lawful basis, minimization, retention, transfers, rights requests, and breach response |
| Independent evaluator | Reviews test protocol and results; challenges subgroup gaps and claims before launch and after material change |
| Oversight body | Receives required notifications, investigates serious concerns, and checks remedy and compliance |

**Go-live conditions:** named owners; lawful and minimized data flows; current source corpus; passing task-specific evaluation; trained reviewers and tested fallback; accessible human appeal route; approved logging and retention; independent review; and a signed deployment record. Missing any condition means no deployment.

### Sources

1. NIST, [AI Risk Management Framework Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/).
2. UNESCO, [Recommendation on the Ethics of Artificial Intelligence](https://www.unesco.org/en/legal-affairs/recommendation-ethics-artificial-intelligence).
3. Nigeria Data Protection Commission, [Nigeria Data Protection Act 2023](https://ndpc.gov.ng/Files/Nigeria_Data_Protection_Act_2023.pdf).
