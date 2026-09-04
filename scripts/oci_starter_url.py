#!/usr/bin/env python3
"""Validate OCI Starter options and print its download URL or curl command."""
import argparse
import json
import re
import shlex
from urllib.parse import urlencode

ALLOWED = {
    "language": {"java", "node", "python", "dotnet", "go", "php", "ords", "apex", "none"},
    "deploy_type": {"public_compute", "private_compute", "instance_pool", "kubernetes", "function", "container_instance", "hpc", "datascience", "oic"},
    "java_framework": {"springboot", "helidon", "helidon4", "tomcat", "micronaut"},
    "java_vm": {"jdk", "graalvm", "graalvm-native"}, "java_version": {"8", "11", "17", "21", "25"},
    "python_framework": {"fastapi", "langgraph", "responses"}, "kubernetes": {"oke", "docker"},
    "ui_type": {"html", "jet", "angular", "reactjs", "jsp", "php", "api", "apex", "none"},
    "db_type": {"atp", "autonomous", "database", "dbsystem", "rac", "db_free", "pluggable", "pdb", "mysql", "psql", "opensearch", "nosql", "none"},
    "license_model": {"LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"},
    "infra_as_code": {"terraform_local", "terraform_object_storage", "resource_manager", "from_resource_manager"},
    "app_mode": {"terraform", "app"}, "mode": {"CLI", "GIT", "ZIP"},
    "shape": {"amd", "freetier_amd", "ampere", "arm"}, "db_install": {"default", "kubernetes"},
    "tls": {"none", "new_http_01", "new_dns_01", "existing_ocid", "existing_dir"},
    "oke_type": {"managed", "virtual_node"}, "security": {"none", "openid"},
    "build_host": {"terraform", "bastion"},
}
DEFAULTS = {
    "prefix": "starter", "java_framework": "springboot", "java_vm": "graalvm",
    "java_version": "25", "python_framework": "fastapi", "ui_type": "html",
    "db_type": "atp", "license_model": "LICENSE_INCLUDED", "app_mode": "terraform",
    "mode": "CLI", "infra_as_code": "terraform_local",
    "db_password": "TO_FILL", "oke_type": "managed", "security": "none",
    "build_host": "terraform",
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("options", nargs="*", metavar="key=value")
    parser.add_argument("--prefix", default=DEFAULTS["prefix"])
    parser.add_argument("--format", choices=("url", "curl", "json"), default="url")
    args = parser.parse_args()
    if not re.fullmatch(r"[a-z][a-z0-9]{0,7}", args.prefix):
        parser.error("--prefix must contain 1-8 lowercase letters or numbers and start with a letter")
    values = DEFAULTS.copy()
    for item in args.options:
        if "=" not in item:
            parser.error(f"expected key=value, got {item!r}")
        key, value = item.split("=", 1)
        if key in {"prefix", "db_password"}:
            parser.error(f"{key!r} is configured by defaults or a dedicated flag, not key=value")
        if key not in ALLOWED:
            parser.error(f"unknown option {key!r}")
        if value not in ALLOWED[key]:
            parser.error(f"invalid {key}={value!r}; allowed: {', '.join(sorted(ALLOWED[key]))}")
        values[key] = value
    values["prefix"] = args.prefix
    missing = [key for key in ("language", "deploy_type", "ui_type", "db_type") if key not in values]
    if missing:
        parser.error("required for download URL: " + ", ".join(missing))
    query = {"prefix": values["prefix"]}
    query.update({key: values[key] for key in ALLOWED if key in values})
    url = "https://www.ocistarter.com/app/zip?" + urlencode(query)
    if args.format == "url":
        print(url)
    elif args.format == "curl":
        print(f"curl -k {shlex.quote(url)} --output starter.zip")
    else:
        print(json.dumps({"url": url, "options": values}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
