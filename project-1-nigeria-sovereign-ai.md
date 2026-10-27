# Nigeria’s Sovereign AI Strategy

## Policy brief | 27 October 2026

**By Anita Adaugo Okezie**

### Executive recommendation

Nigeria should pursue **sovereign capability, not frontier-model autarky**. Useful sovereignty means the country can choose, adapt, host, evaluate, govern, and replace AI systems; it does not require training a model with hundreds of billions of parameters from scratch. Nigeria should prioritize shared language and evaluation assets, modest but dependable computing, open-weight models fine-tuned for bounded tasks, and public procurement that rewards measurable local value and accountability. This approach complements the National Artificial Intelligence Strategy published in 2025 and the Nigerian Atlas for Languages and AI at Scale (N-ATLAS), rather than duplicating them. The federal strategy already organizes action around infrastructure, talent, adoption, ethics, and governance; N-ATLAS establishes a multilingual model capability for Yoruba, Hausa, Igbo, and Nigerian-accented English.[1][2]

Use one test to judge a pilot: does it improve a specific service at an acceptable cost and level of risk? Nigerian institutions should retain authority over data, deployment, evaluation, and exit. They can develop models locally, adapt open weights, or procure hosted services based on the task and data sensitivity.

### Why this path fits Nigeria

Frontier pretraining is a continuing capital and energy commitment: it requires large curated corpora, specialist teams, advanced accelerators, reliable power and cooling, and repeated training runs. Even a successful national training run would not guarantee good performance in Nigerian languages, reliable answers about public rules, or safe behavior in a ministry workflow. A general model is a starting component, not a service outcome.

The opportunity is to invest in scarce complements that are reusable across models: lawful Nigerian datasets, language expertise, locally grounded tests, skilled practitioners, and secure hosting. This reduces dependence on any single vendor and helps public institutions negotiate from a position of knowledge. It also avoids a false choice between importing everything and building everything. Open weights can be adapted locally, while external tools remain useful for low-sensitivity tasks where their contractual and legal terms are acceptable.

### 1. Build a governed language-data commons

Create a federated national program for high-quality text, speech, terminology, and benchmark datasets in Hausa, Yoruba, Igbo, Nigerian English, Nigerian Pidgin, and additional languages selected with communities. Start with practical domains such as agriculture extension, health navigation, education, disaster information, and public-service enquiries. Prioritize cases with verified content and domain professionals who can check errors. Measure language coverage by regional accents, code-switching, spelling variation, oral registers, disability access, and low-literacy use, not just by the number of scraped words.

Each dataset should have a named steward, documented provenance and legal basis, a data statement describing collection and exclusions, a license, consent terms where applicable, quality checks, a retention schedule, and a route for correction or removal. Pay native speakers, translators, teachers, and community organizations to create and review examples; do not treat language work as free annotation. Separate public-domain or licensed material from personal data. Use de-identification, minimization, and access controls before any training or testing. The Nigeria Data Protection Act 2023 applies to personal-data processing, including relevant processing by organizations outside Nigeria, and its cross-border transfer provisions require an adequate level of protection through recognized legal mechanisms.[3][4]

Keep the commons federated where centralization would create privacy, security, or ownership problems. Publish safe artifacts such as metadata, aggregate quality reports, approved corpora, and test sets. Keep restricted data with the responsible institution. Include community representatives in access decisions and benefit-sharing arrangements. Language communities should be able to contest harmful or misleading representations.

### 2. Adapt smaller open-weight models to bounded jobs

For many public tasks, begin with the smallest model that passes the task-specific acceptance threshold. Candidate work includes classifying enquiries into service queues, retrieving passages from approved guidance, extracting fields from forms, translating low-risk notices, and drafting a response for a staff member to approve. Use retrieval-augmented generation (RAG) for changing policy content: the system finds current, approved source passages and cites them, rather than relying on model memory. Fine-tune only when an evaluation shows that retrieval, prompts, or conventional software are insufficient.

Test a range of compact open-weight models and simple non-generative baselines. Compare quality by language, region, input length, code-switching, and user group; track latency, total cost, privacy exposure, failure modes, and review burden. A small model may be cheaper to host and easier to constrain, but it can also be weaker, more brittle, or less safe. Keep a human escalation path for uncertainty and any decision affecting eligibility, benefits, health, legal status, or enforcement. Procurement should specify model and dataset versions, acceptable use, security update duties, logging, independent evaluation access, service levels, and portability to a replacement model.

### 3. Fund shared, resilient computing for practical workloads

Treat compute as a portfolio of capacity, power, connectivity, operations, and access. Government and universities should inventory existing public cloud and data-centre resources, including the NCAIR/Galaxy Backbone capacity described by NCAIR, and publish available service tiers, queue times, security controls, utilization, and operating costs.[2] That baseline is more useful than announcing a GPU count without electricity, cooling, maintenance, or an accountable user program.

Provide a shared national research and public-interest AI environment with CPU capacity for data work and small models, GPU pools for fine-tuning and evaluation, secure enclaves for sensitive workloads, and burst access to commercial cloud when justified. Use workload classification: public data can use open research infrastructure; sensitive personal records require approved controls, encryption, access logging, and a documented transfer assessment. Require energy-efficient scheduling and report energy and water use for large workloads. Prioritize uptime, backups, incident response, network reach, and trained operators. Use transparent access grants for universities, startups, civil society, and agencies, with independent allocation and published utilization data.

### 4. Demonstrate value in carefully chosen public services

Select pilots with a service owner, a baseline, a safe fallback, and a measurable public outcome. Good first candidates include routing non-sensitive enquiries to the right agency; searching public circulars and program guidance; assisting staff to draft routine correspondence; translating approved information; and helping agricultural extension workers retrieve locally relevant advice from verified sources. A pilot should report resolution time, referral accuracy, accessibility, user satisfaction, staff workload, error severity, operating cost, and performance gaps across language and geography. Compare against the existing process and a non-AI alternative.

Do not start with autonomous decisions on welfare eligibility, policing, immigration, credit, hiring, diagnosis, or judicial outcomes. In these settings, errors can restrict rights or be difficult to reverse. If AI supports staff, the human must have the information, time, authority, and training to reject the output. Nigeria should require an impact assessment and an accessible complaint and appeal path before any deployment that can materially affect a person's rights or access to essential services. UNESCO's Recommendation stresses proportionality, privacy, human oversight, traceability, and the need for human determination in irreversible or life-and-death cases.[5]

### 5. Make data sovereignty practical and lawful

Define sovereignty as enforceable control over purpose, access, retention, security, audit, and exit. Avoid a blanket rule that every byte must remain physically in Nigeria. Data residency may support security or legal obligations, but location alone cannot prevent misuse, foreign legal access, insecure configuration, or vendor lock-in. A lawful transfer can sometimes be safer and more reliable than poorly operated local infrastructure.

For each system, document the data controller and processors, lawful basis, data categories, storage and processing locations, subprocessors, transfer mechanism, retention and deletion, breach responsibilities, and independent audit rights. Apply the Nigeria Data Protection Act and obtain specialist advice for cross-border processing; the NDPC identifies adequacy decisions, approved cross-border instruments, and specified legal grounds among the transfer pathways.[3][4] Keep encryption keys and identity controls under accountable Nigerian institutional control where feasible. Ensure procurement terms permit export of records, prompts, logs, and configuration in usable formats, and require a tested transition plan.

### 6. Create independent evaluation and incident learning

Establish a publicly funded but operationally independent evaluation function, linked to universities and civil society and able to test vendor and government systems. Publish benchmark protocols before testing, maintain a protected holdout set, disclose funding and conflicts, and permit replication. Assess factuality against authoritative Nigerian sources; language and dialect performance; privacy leakage; security and prompt injection; discriminatory outcomes; robustness to misspellings and code-switching; latency; cost; and human-review load. An evaluation should state what it did not test and the population to which findings may not generalize. My experience reviewing AI outputs has shown me that test results matter only when teams use them to improve rubrics, staff guidance, and the service.

Require pre-deployment testing, a named accountable official, monitoring thresholds, version control, an incident channel, and a pause or rollback procedure. Report significant incidents and corrective actions in a privacy-preserving public register. NIST's AI Risk Management Framework offers a useful operational structure with four functions: Govern, Map, Measure, and Manage. It calls for lifecycle risk management, contextual testing, documented limitations, and independent review where useful.[6] It is a method reference, not a substitute for Nigerian law or local accountability.

### 7. Develop the workforce around real delivery

Expand AI capability beyond model researchers. Fund paid apprenticeships and procurement-linked placements for data stewards, language technologists, MLOps and infrastructure engineers, privacy professionals, auditors, product managers, frontline service workers, and public-interest researchers. Pair universities with ministries and local firms on open, bounded projects; reward reproducible datasets, evaluation methods, and maintained software as well as papers. Teach civil servants how to verify outputs, identify automation bias, protect data, communicate uncertainty, and escalate failures. Build local-language community review into project budgets.

Training should lead to maintained services and transferable skills, not only short courses. Public tenders should require supplier knowledge transfer, documentation, and staff mentoring. Support Nigerian startups through small, staged contracts that reward measured improvement and allow termination if evidence or safeguards fail.

### Implementation sequence and measures

**First 12 months:** establish a cross-government AI delivery and assurance unit; publish a public-sector use-case inventory and risk tiers; select three low-risk pilots; adopt common dataset documentation, procurement, and evaluation templates; and fund language-data partnerships. Publish baselines and pilot results, including failures.

**Months 12 to 36:** extend shared compute and secure data services based on audited demand; create the independent evaluation program and multilingual benchmark suite; scale pilots only after external review; and build a continuing talent pipeline with public institutions and local firms.

Measure success by service outcomes and institutional capability: fewer misrouted enquiries, faster and more accurate access to public information, reduced staff time without increased exclusion, coverage and error rates by language, tested recovery time, locally available evaluators and maintainers, dataset reuse under clear permissions, and the ability to switch model providers. Set baselines before targets and publish annual progress. Avoid treating model size, GPU counts, or model launch announcements as proof of public value.

### Conclusion

Nigeria can build useful and trustworthy AI by owning the capabilities that make AI accountable and fit for Nigerian needs: lawful data, language expertise, modest adaptable models, dependable infrastructure, evaluation, and skilled public servants. Frontier-scale pretraining is one possible research ambition, not a prerequisite for sovereignty. The strategic choice is to turn national strategy and emerging assets such as N-ATLAS into a portfolio of tested services that improve outcomes, protect rights, and remain under meaningful Nigerian control.

### Sources

1. Federal Ministry of Communications, Innovation and Digital Economy, [National Artificial Intelligence Strategy 2025](https://ncair.nitda.gov.ng/wp-content/uploads/2025/09/National-Artificial-Intelligence-Strategy-19092025.pdf).
2. National Centre for Artificial Intelligence and Robotics, [NCAIR official site](https://ncair.nitda.gov.ng/), including its published N-ATLAS description and infrastructure overview.
3. Nigeria Data Protection Commission, [Nigeria Data Protection Act 2023](https://ndpc.gov.ng/wp-content/uploads/2024/03/Nigeria_Data_Protection_Act_2023.pdf).
4. Nigeria Data Protection Commission, [FAQs on cross-border transfers](https://ndpc.gov.ng/faqs/).
5. UNESCO, [Recommendation on the Ethics of Artificial Intelligence](https://www.unesco.org/en/legal-affairs/recommendation-ethics-artificial-intelligence).
6. U.S. National Institute of Standards and Technology, [AI Risk Management Framework Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/).
