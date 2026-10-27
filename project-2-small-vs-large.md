# Small Models vs. Large Models: Public-Service Enquiry Routing

**By Anita Adaugo Okezie**

## Question

This project asks a narrow question: can compact local classifiers help route short English enquiries to one of five service desks before staff review? It is a small, reproducible demonstration. It does not compare a compact model with a frontier-scale LLM, and it does not establish performance on real Nigerian citizens' messages.

In my AI evaluation work, I have reviewed multi-step model reasoning and agent actions against task instructions. That work has shown me why accuracy alone is not enough. Teams also need to understand error types, reviewer corrections, and whether feedback improves the next round. This benchmark does not measure those live-workflow outcomes. It demonstrates a basic classifier comparison and a reproducible evaluation process.

## Data and method

The benchmark creates 300 templated synthetic enquiries, balanced across benefits, education, health, roads, and tax. It uses no citizen records, scraping, or personal data. A stratified 80/20 split with seed `20261027` produces 240 training and 60 test examples. TF-IDF word unigrams and bigrams feed two conventional classifiers: Multinomial Naive Bayes and logistic regression. The benchmark reports exact-match accuracy, macro-F1, class metrics, confusion matrices, and repeated warm CPU prediction latency. Test accuracy is a point estimate over only 60 examples; one error changes it by 1.67 percentage points.

## Reproduce

Requires Python 3.10+ and `numpy`, `scikit-learn`.

```sh
python -m pip install -r requirements.txt
python benchmark.py
```

The script rewrites `synthetic_enquiries.jsonl` and `results.json`. Latency varies with CPU, process load, Python and library versions. `results.json` records the versions used for the run. Cloud API costs are not applicable; the reported local per-call cost is zero marginal cloud spend, not zero total cost. Hardware, power, engineering, security, and maintenance remain real costs.

## Results

See [`results.json`](results.json) for the machine-readable output. The reference run used Python 3.13.9, scikit-learn 1.7.2, and NumPy 2.3.5. Both classifiers scored 60/60 (100%) accuracy and 1.00 macro-F1; each class had 12/12 correct predictions. Mean CPU prediction latency in the repeated warm microbenchmark was 0.014 ms/enquiry for Naive Bayes and 0.023 ms/enquiry for logistic regression. Local marginal cloud cost is zero; total operating cost was not measured. Results show the models learning templated distinctions, not real-world language. This dataset has repeated phrase structures and clean labels, so high scores should be expected and should not be mistaken for realistic field accuracy. The timing is a microbenchmark, not an end-to-end service measurement.

### Error analysis

The reference run made no test errors, so it cannot reveal meaningful error types. The code emits per-class results and confusion matrices for future runs. The dataset does not contain Nigerian-language requests, speech transcription errors, code-switching, ambiguous multi-service requests, misspellings from real users, or adversarial inputs. A proper follow-up would recruit service staff and language reviewers to create a consented, de-identified evaluation set, keep a protected holdout, and label ambiguity and severity explicitly.

## Decision

For this narrowly specified, low-risk **internal routing suggestion**, a small local classifier is a plausible candidate for a shadow-mode pilot because it is fast, inexpensive at inference time, simple to inspect operationally, and can keep input on the institution's machine. This experiment alone does not justify deployment. Human-review time and quality were not measured; keep all cases in staff-controlled queues and require review for ambiguous or high-risk messages. Compare with a rules baseline and a larger multilingual model on the same real, lawfully collected test set; measure per-language accuracy, high-severity misroutes, staff correction/review time, abstention quality, and end-to-end costs. If any message could change eligibility or a person's rights, require human review and retain ordinary routing as fallback.

## Limitations

- Synthetic templated data are much easier than natural enquiries and can leak template patterns across train and test.
- The sample is small, English-only, balanced, and not representative of any agency's case mix.
- Two traditional classifiers are compared; no generative or open-weight LLM is evaluated.
- Latency is measured in-process on a single machine without concurrency, network, service overhead, or energy metering.
- Cost excludes compute ownership, electricity, staff, integration, monitoring, and security.
- No human-review study, accessibility study, privacy attack, fairness assessment, or deployment trial was performed.

These results support a reproducible prototype and a test plan, not a broad claim that smaller models outperform larger models.
