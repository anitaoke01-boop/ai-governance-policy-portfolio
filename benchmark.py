"""Reproducible toy benchmark for public-service enquiry routing.

All examples are templated and synthetic. This is a pipeline demonstration, not
a claim about real Nigerian service users or a production language model.
"""
from __future__ import annotations

import json
import platform
import time
from pathlib import Path

import numpy as np
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

SEED = 20261027
LABELS = ["benefits", "education", "health", "roads", "tax"]
ROOT = Path(__file__).resolve().parent

TEMPLATES = {
    "benefits": [
        "I have not received my {noun} payment for {time}",
        "Please check my {noun} application reference {ref}",
        "How do I appeal a rejected {noun} claim",
        "My household needs help with {noun} support",
        "Where can I update bank details for {noun}",
        "I want to ask about the status of my {noun}",
    ],
    "education": [
        "How can I apply for a {noun} scholarship",
        "My child needs help with {noun} school registration",
        "Please explain the {noun} examination timetable",
        "Where do I submit a {noun} school transfer request",
        "I need information about {noun} teacher recruitment",
        "The school has not received its {noun} grant",
    ],
    "health": [
        "Where is the nearest {noun} clinic in my area",
        "How do I book a {noun} vaccination appointment",
        "Please explain the {noun} health insurance enrollment",
        "I need information about {noun} clinic opening hours",
        "How can I replace my {noun} health card",
        "Where can I find {noun} maternal health services",
    ],
    "roads": [
        "Please report a pothole on the {noun} road near {place}",
        "The {noun} traffic light is not working at {place}",
        "How do I request repair of a {noun} bridge",
        "There is flooding on the {noun} street by {place}",
        "I want to report a damaged {noun} road sign",
        "When will the {noun} road construction be completed",
    ],
    "tax": [
        "How can I get a {noun} tax identification number",
        "Please explain my {noun} tax filing deadline",
        "I need a receipt for my {noun} tax payment",
        "Where do I update my {noun} taxpayer address",
        "How can I correct an error in my {noun} tax return",
        "Please check the status of my {noun} tax refund",
    ],
}
FILLERS = {
    "benefits": {"noun": ["monthly", "family", "social", "cash", "emergency"], "time": ["June", "last month", "this quarter"], "ref": ["A102", "B204", "C318"]},
    "education": {"noun": ["university", "primary", "state", "federal", "technical"]},
    "health": {"noun": ["public", "district", "community", "state", "local"]},
    "roads": {"noun": ["main", "federal", "state", "local", "access"], "place": ["the market", "the junction", "my village"]},
    "tax": {"noun": ["business", "personal", "company", "federal", "state"]},
}


def build_data() -> list[dict[str, str]]:
    rng = np.random.default_rng(SEED)
    rows = []
    for label, templates in TEMPLATES.items():
        for i in range(60):
            template = templates[i % len(templates)]
            phrase = template
            for slot, choices in FILLERS[label].items():
                phrase = phrase.replace("{" + slot + "}", str(rng.choice(choices)))
            # Light, deterministic surface variation; no personal data is used.
            if i % 3 == 1:
                phrase = "Hello, " + phrase.lower()
            elif i % 3 == 2:
                phrase += ". Please assist."
            rows.append({"text": phrase, "label": label})
    return rows


def main() -> None:
    rows = build_data()
    data_path = ROOT / "synthetic_enquiries.jsonl"
    data_path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows))
    texts = np.array([r["text"] for r in rows])
    labels = np.array([r["label"] for r in rows])
    train_idx, test_idx = train_test_split(
        np.arange(len(rows)), test_size=0.2, random_state=SEED, stratify=labels
    )
    specs = {
        "Multinomial Naive Bayes": MultinomialNB(alpha=0.5),
        "Logistic Regression": LogisticRegression(max_iter=500, C=2.0),
    }
    results = []
    for name, estimator in specs.items():
        model = make_pipeline(TfidfVectorizer(ngram_range=(1, 2), min_df=1), estimator)
        model.fit(texts[train_idx], labels[train_idx])
        # Warm up, then time repeated prediction on the same fixed held-out set.
        model.predict(texts[test_idx])
        start = time.perf_counter()
        for _ in range(100):
            predicted = model.predict(texts[test_idx])
        elapsed = (time.perf_counter() - start) / (100 * len(test_idx)) * 1000
        report = classification_report(labels[test_idx], predicted, labels=LABELS, output_dict=True, zero_division=0)
        results.append({
            "model": name,
            "accuracy": accuracy_score(labels[test_idx], predicted),
            "macro_f1": report["macro avg"]["f1-score"],
            "mean_cpu_latency_ms_per_enquiry": elapsed,
            "confusion_matrix_labels_order": LABELS,
            "confusion_matrix": confusion_matrix(labels[test_idx], predicted, labels=LABELS).tolist(),
            "per_class": {label: {"precision": report[label]["precision"], "recall": report[label]["recall"], "f1": report[label]["f1-score"]} for label in LABELS},
        })
    output = {
        "benchmark": "synthetic public-service enquiry classification",
        "seed": SEED,
        "examples": len(rows),
        "train_examples": len(train_idx),
        "test_examples": len(test_idx),
        "class_counts": {label: int((labels == label).sum()) for label in LABELS},
        "runtime": {"python": platform.python_version(), "scikit_learn": sklearn.__version__, "numpy": np.__version__},
        "cost_note": "No per-call cloud charge. CPU energy, machine depreciation, engineering, and support costs are not priced; latency is environment-dependent.",
        "results": results,
    }
    (ROOT / "results.json").write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
