#!/usr/bin/env python3
"""Validate catalog data and experimental intent artifacts without network access."""

from __future__ import annotations

from datetime import date
import json
from pathlib import Path
import sys
from typing import Any, Iterable
from urllib.parse import urlparse

try:
    import yaml
except ImportError as exc:
    raise SystemExit(
        "PyYAML is required. Run: python -m pip install -r requirements-dev.txt"
    ) from exc

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError as exc:
    raise SystemExit(
        "jsonschema is required. Run: python -m pip install -r requirements-dev.txt"
    ) from exc

ROOT = Path(__file__).resolve().parents[1]

ALLOWED_CATEGORIES = {
    "core",
    "provenance",
    "adjacent",
    "research",
    "learning",
    "experimental",
}
ALLOWED_LIFECYCLE = {
    "capture",
    "represent",
    "propagate",
    "enforce",
    "verify",
    "evolve",
    "provenance",
    "governance",
}
ALLOWED_AVAILABILITY = {
    "waitlist",
    "open-format",
    "commercial",
    "open-source",
    "research",
    "book",
    "experimental",
}
ALLOWED_MATURITY = {
    "operational",
    "emerging",
    "planned",
    "research",
    "discussion-draft",
}
ALLOWED_PREDICTION_STATUS = {
    "open",
    "confirmed",
    "partially-confirmed",
    "falsified",
    "expired",
    "superseded",
}


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path}: top level must be a mapping")
    return data


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path}: top level must be an object")
    return data


def valid_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def validate_resources(errors: list[str]) -> int:
    path = ROOT / "data" / "resources.yml"
    data = load_yaml(path)
    resources = data.get("resources")
    if not isinstance(resources, list) or not resources:
        errors.append("resources.yml: resources must be a non-empty list")
        return 0

    required = {
        "id",
        "name",
        "url",
        "category",
        "lifecycle",
        "availability",
        "maturity",
        "representation",
        "description",
        "limitation",
        "last_verified",
        "evidence",
    }
    ids: set[str] = set()
    urls: set[str] = set()

    for index, item in enumerate(resources, start=1):
        label = f"resources[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{label}: must be a mapping")
            continue
        missing = sorted(required - item.keys())
        if missing:
            errors.append(f"{label}: missing {', '.join(missing)}")
            continue

        item_id = item["id"]
        if not isinstance(item_id, str) or not item_id:
            errors.append(f"{label}.id: must be a non-empty string")
        elif item_id in ids:
            errors.append(f"{label}.id: duplicate {item_id}")
        else:
            ids.add(item_id)

        url = item["url"]
        if not isinstance(url, str) or not valid_url(url):
            errors.append(f"{label}.url: must be an https URL")
        elif url in urls:
            errors.append(f"{label}.url: duplicate canonical URL {url}")
        else:
            urls.add(url)

        if item["category"] not in ALLOWED_CATEGORIES:
            errors.append(f"{label}.category: unsupported value {item['category']!r}")

        lifecycle = item["lifecycle"]
        if not isinstance(lifecycle, list) or not lifecycle:
            errors.append(f"{label}.lifecycle: must be a non-empty list")
        else:
            invalid = sorted(set(lifecycle) - ALLOWED_LIFECYCLE)
            if invalid:
                errors.append(f"{label}.lifecycle: unsupported tags {invalid}")
            if len(lifecycle) != len(set(lifecycle)):
                errors.append(f"{label}.lifecycle: duplicate tags")

        if item["availability"] not in ALLOWED_AVAILABILITY:
            errors.append(
                f"{label}.availability: unsupported value {item['availability']!r}"
            )
        if item["maturity"] not in ALLOWED_MATURITY:
            errors.append(f"{label}.maturity: unsupported value {item['maturity']!r}")

        verified = item["last_verified"]
        if not isinstance(verified, date):
            errors.append(f"{label}.last_verified: must be an unquoted YYYY-MM-DD date")

        for text_key in ("representation", "description", "limitation"):
            value = item[text_key]
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{label}.{text_key}: must be a non-empty string")

        evidence = item["evidence"]
        if not isinstance(evidence, list) or not evidence:
            errors.append(f"{label}.evidence: must be a non-empty list")
        else:
            for evidence_index, evidence_item in enumerate(evidence, start=1):
                evidence_label = f"{label}.evidence[{evidence_index}]"
                if not isinstance(evidence_item, dict):
                    errors.append(f"{evidence_label}: must be a mapping")
                    continue
                if not valid_url(str(evidence_item.get("url", ""))):
                    errors.append(f"{evidence_label}.url: must be an https URL")
                if not str(evidence_item.get("supports", "")).strip():
                    errors.append(f"{evidence_label}.supports: required")


    return len(resources)


def validate_terms(errors: list[str]) -> int:
    path = ROOT / "data" / "terms.yml"
    data = load_yaml(path)
    terms = data.get("terms")
    if not isinstance(terms, list) or not terms:
        errors.append("terms.yml: terms must be a non-empty list")
        return 0

    ids: set[str] = set()
    for index, item in enumerate(terms, start=1):
        label = f"terms[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{label}: must be a mapping")
            continue
        for key in ("id", "label", "status", "working_definition", "signals"):
            if key not in item:
                errors.append(f"{label}: missing {key}")

        item_id = item.get("id")
        if not isinstance(item_id, str) or not item_id:
            errors.append(f"{label}.id: must be a non-empty string")
        elif item_id in ids:
            errors.append(f"{label}.id: duplicate {item_id}")
        else:
            ids.add(item_id)

        status = item.get("status")
        if not isinstance(status, str) or not status.strip():
            errors.append(f"{label}.status: must be a non-empty string")

        signals = item.get("signals", [])
        if not isinstance(signals, list) or not signals:
            errors.append(f"{label}.signals: must be non-empty")
        else:
            for signal in signals:
                if not valid_url(str(signal)):
                    errors.append(f"{label}.signals: invalid URL {signal!r}")


    return len(terms)


def validate_predictions(errors: list[str]) -> int:
    path = ROOT / "data" / "predictions.yml"
    data = load_yaml(path)
    predictions = data.get("predictions")
    if not isinstance(predictions, list) or not predictions:
        errors.append("predictions.yml: predictions must be a non-empty list")
        return 0

    ids: set[str] = set()
    for index, item in enumerate(predictions, start=1):
        label = f"predictions[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{label}: must be a mapping")
            continue
        required = {
            "id",
            "claim",
            "window_end",
            "confidence",
            "status",
            "evidence_at_creation",
            "resolution_rule",
            "falsification",
        }
        missing = sorted(required - item.keys())
        if missing:
            errors.append(f"{label}: missing {', '.join(missing)}")
            continue

        item_id = item["id"]
        if not isinstance(item_id, str) or not item_id:
            errors.append(f"{label}.id: must be a non-empty string")
        elif item_id in ids:
            errors.append(f"{label}.id: duplicate {item_id}")
        else:
            ids.add(item_id)

        if item["status"] not in ALLOWED_PREDICTION_STATUS:
            errors.append(
                f"{label}.status: unsupported value {item['status']!r}"
            )

        confidence = item["confidence"]
        if not isinstance(confidence, (int, float)) or isinstance(confidence, bool):
            errors.append(f"{label}.confidence: must be numeric")
        elif not 0 <= confidence <= 1:
            errors.append(f"{label}.confidence: must be between 0 and 1")

        if not isinstance(item["window_end"], date):
            errors.append(f"{label}.window_end: must be an unquoted YYYY-MM-DD date")

        evidence = item["evidence_at_creation"]
        if not isinstance(evidence, list) or not evidence:
            errors.append(f"{label}.evidence_at_creation: must be non-empty")
        else:
            for url in evidence:
                if not valid_url(str(url)):
                    errors.append(f"{label}.evidence_at_creation: invalid URL {url!r}")

    return len(predictions)


def iter_record_items(record: dict[str, Any], key: str) -> Iterable[dict[str, Any]]:
    value = record.get(key, [])
    if isinstance(value, list):
        for item in value:
            if isinstance(item, dict):
                yield item


def validate_intent_example(errors: list[str]) -> None:
    schema_path = ROOT / "schemas" / "intent-record.v0.1.schema.json"
    example_path = ROOT / "examples" / "intent-record.yml"
    schema = load_json(schema_path)
    example = load_yaml(example_path)

    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:  # jsonschema exposes several schema exception types
        errors.append(f"{schema_path}: invalid JSON Schema: {exc}")
        return

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for error in sorted(validator.iter_errors(example), key=lambda item: list(item.path)):
        location = ".".join(str(part) for part in error.absolute_path) or "<root>"
        errors.append(f"{example_path}:{location}: {error.message}")

    intent = example.get("intent")
    if not isinstance(intent, dict):
        return

    id_sections = (
        "evidence",
        "outcomes",
        "constraints",
        "edge_cases",
        "decisions",
        "verification",
    )
    seen_ids: dict[str, str] = {}
    for section in id_sections:
        for item in iter_record_items(intent, section):
            item_id = item.get("id")
            if not isinstance(item_id, str):
                continue
            previous = seen_ids.get(item_id)
            if previous is not None:
                errors.append(
                    f"{example_path}: duplicate stable id {item_id!r} in {previous} and {section}"
                )
            else:
                seen_ids[item_id] = section

    evolution = intent.get("evolution")
    if isinstance(evolution, dict):
        for section in ("findings", "rejected_paths"):
            for item in iter_record_items(evolution, section):
                item_id = item.get("id")
                if not isinstance(item_id, str):
                    continue
                previous = seen_ids.get(item_id)
                if previous is not None:
                    errors.append(
                        f"{example_path}: duplicate stable id {item_id!r} in {previous} and evolution.{section}"
                    )
                else:
                    seen_ids[item_id] = f"evolution.{section}"

    valid_targets = {"objective"}
    valid_targets.update(
        f"outcome:{item['id']}"
        for item in iter_record_items(intent, "outcomes")
        if isinstance(item.get("id"), str)
    )
    valid_targets.update(
        f"constraint:{item['id']}"
        for item in iter_record_items(intent, "constraints")
        if isinstance(item.get("id"), str)
    )
    valid_targets.update(
        f"edge-case:{item['id']}"
        for item in iter_record_items(intent, "edge_cases")
        if isinstance(item.get("id"), str)
    )

    for section in ("evidence", "verification"):
        for item in iter_record_items(intent, section):
            supports = item.get("supports", [])
            if not isinstance(supports, list):
                continue
            for target in supports:
                if isinstance(target, str) and target not in valid_targets:
                    errors.append(
                        f"{example_path}:{section}.{item.get('id', '?')}.supports: unknown target {target!r}"
                    )


def main() -> int:
    errors: list[str] = []
    counts = {"resources": 0, "terms": 0, "predictions": 0}
    try:
        counts["resources"] = validate_resources(errors)
        counts["terms"] = validate_terms(errors)
        counts["predictions"] = validate_predictions(errors)
        validate_intent_example(errors)
    except (OSError, ValueError, json.JSONDecodeError, yaml.YAMLError) as exc:
        errors.append(str(exc))

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Validation passed: "
        f"{counts['resources']} resources, "
        f"{counts['terms']} terms, "
        f"{counts['predictions']} predictions, "
        "schema, and intent example."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
