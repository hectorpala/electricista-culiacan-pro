#!/usr/bin/env python3
"""
Validate JSON-LD schemas in all HTML files
Electricista Culiacán Pro - Schema Validator
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Tuple


def extract_json_ld(html_content: str) -> List[str]:
    """Extract JSON-LD scripts from HTML content"""
    pattern = r'<script type="application/ld\+json">(.*?)</script>'
    matches = re.findall(pattern, html_content, re.DOTALL)
    return matches


def validate_json(json_str: str) -> Tuple[bool, str]:
    """Validate JSON syntax"""
    try:
        json.loads(json_str)
        return True, "Valid JSON"
    except json.JSONDecodeError as e:
        return False, f"Invalid JSON: {str(e)}"


def check_required_fields(data: dict, required: List[str]) -> List[str]:
    """Check if required fields are present"""
    missing = []
    for field in required:
        if field not in data:
            missing.append(field)
    return missing


def validate_schema(data: dict) -> List[str]:
    """Validate schema structure and required fields"""
    errors = []

    # Check @context
    if "@context" not in data:
        errors.append("Missing @context")

    # Check @type or @graph
    if "@graph" in data:
        # Validate @graph structure
        if not isinstance(data["@graph"], list):
            errors.append("@graph must be an array")
        else:
            for i, node in enumerate(data["@graph"]):
                if "@type" not in node:
                    errors.append(f"@graph[{i}]: Missing @type")
    elif "@type" not in data:
        errors.append("Missing @type")

    # Validate specific types
    schema_type = data.get("@type", "")

    if schema_type == "Electrician" or "Electrician" in str(data):
        required = ["name", "address", "telephone"]
        missing = check_required_fields(data, required)
        if missing:
            errors.append(f"Electrician schema missing: {', '.join(missing)}")

    if schema_type == "Service" or "Service" in str(data):
        required = ["name", "provider"]
        missing = check_required_fields(data, required)
        if missing:
            errors.append(f"Service schema missing: {', '.join(missing)}")

    if schema_type == "FAQPage" or "FAQPage" in str(data):
        if "mainEntity" not in data:
            errors.append("FAQPage missing mainEntity")

    return errors


def validate_file(file_path: Path) -> Dict:
    """Validate a single HTML file"""
    result = {
        "file": str(file_path),
        "schemas_found": 0,
        "valid": True,
        "errors": []
    }

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        json_ld_scripts = extract_json_ld(content)
        result["schemas_found"] = len(json_ld_scripts)

        if not json_ld_scripts:
            result["errors"].append("No JSON-LD schema found")
            result["valid"] = False
            return result

        for i, script in enumerate(json_ld_scripts):
            # Validate JSON syntax
            is_valid, message = validate_json(script)
            if not is_valid:
                result["errors"].append(f"Schema {i + 1}: {message}")
                result["valid"] = False
                continue

            # Validate schema structure
            data = json.loads(script)
            schema_errors = validate_schema(data)
            if schema_errors:
                result["errors"].extend([f"Schema {i + 1}: {err}" for err in schema_errors])
                result["valid"] = False

    except Exception as e:
        result["errors"].append(f"Error reading file: {str(e)}")
        result["valid"] = False

    return result


def main():
    """Main execution"""
    print("🔍 Validating JSON-LD schemas in HTML files...\n")

    # Find all HTML files
    html_files = list(Path(".").rglob("*.html"))
    html_files = [f for f in html_files if not any(
        part.startswith(".") for part in f.parts
    ) and "node_modules" not in f.parts]

    print(f"📄 Found {len(html_files)} HTML files\n")

    # Validate each file
    results = []
    valid_count = 0
    error_count = 0

    for file_path in sorted(html_files):
        result = validate_file(file_path)
        results.append(result)

        if result["valid"]:
            valid_count += 1
            print(f"✅ {result['file']} - {result['schemas_found']} schema(s)")
        else:
            error_count += 1
            print(f"❌ {result['file']}")
            for error in result["errors"]:
                print(f"   ⚠️  {error}")

    # Summary
    print("\n" + "=" * 60)
    print("📊 Validation Summary")
    print("=" * 60)
    print(f"Total files: {len(results)}")
    print(f"✅ Valid: {valid_count}")
    print(f"❌ Errors: {error_count}")
    print("=" * 60)

    # Exit with error if any validation failed
    if error_count > 0:
        exit(1)
    else:
        print("\n🎉 All schemas are valid!")


if __name__ == "__main__":
    main()
