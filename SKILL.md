---
name: oci-starter-skill
description: Create application programs and OCI Starter projects for Oracle Cloud Infrastructure. Use when a user asks to create or build a program/project using OCI Starter, asks for an OCI Starter architecture, or says "deploy with OCI Starter" / "deploy with oci starter". Collect only the architecture choices needed, download the matching OCI Starter archive, and implement the requested application in its src/app directory.
---

# OCI Starter Skill

Decide whether the user requested an OCI Starter scaffold:

- When the user asks to create or build a program or project **using OCI Starter** (including "using the OCI Starter skill"), create the OCI Starter project and follow **Create with OCI Starter** below.
- When OCI Starter is not part of the requested project, create the requested application first. Treat a later request to deploy it with OCI Starter as an explicit transition to **Create with OCI Starter**.

Creating or downloading a scaffold never authorizes OCI provisioning, Terraform, or deployment of cloud resources.

## Build the application

1. Clarify the product only if the request lacks essential behavior, data, users, or interface information. Otherwise start building.
2. Choose the smallest appropriate application stack. When OCI Starter is already in scope, keep the implementation compatible with the selected language, framework, UI, database, and deployment target.
3. Create clean, runnable source code with an appropriate README and local validation. Do not pretend an OCI resource exists.

## Create with OCI Starter

The `$HOME/.oci_starter_profile` file is a Bash script, not a dotenv file. It commonly contains direct exports (for example, `export TF_VAR_yyy="123"`) and conditional exports (for example, `if [ "$TF_VAR_xxx" == "__TO_FILL__" ]; then export TF_VAR_xxx=...; fi`). Never source or execute it to inspect settings, and never print its values. OCI Starter tooling may source it when it runs.

To determine whether a setting is profile-backed, inspect the script structurally for an assignment or `export` to its exact name, checking both `setting` and `TF_VAR_setting`. Count direct and conditional exports as profile-backed. Do not try to evaluate shell conditions, expand variables, or infer the final value: a conditional export may deliberately preserve a value already supplied by the environment.

When the user requests an OCI Starter project, first identify whether an existing project already has a compatible OCI Starter scaffold. If not, conduct a short, conditional architecture interview. Ask only unresolved decisions:

- workload and exposure: public/private compute, Kubernetes, function, container instance, instance pool, HPC, data science, or OIC;
- language and framework; UI/API type; database requirement;
- for Kubernetes: managed vs virtual nodes;
- for Java: framework, JVM, and Java version;
- for database: type, licensing, and whether Kubernetes installation is needed;
- for public HTTPS: TLS strategy; and whether OpenID authentication is required;
- infrastructure delivery: local Terraform, Object Storage Terraform, Resource Manager, or imported Resource Manager; build host if relevant.

Apply the OCI Starter defaults in [references/options.md](references/options.md) unless the user requests an override. Ask only for `language` and `deploy_type` (and decisions genuinely required by the selected target).

### Scaffold and configure

1. Extract the contents of the generated `starter/` directory from `starter.zip` directly into the Coding Agent project root. The project root must contain the scaffold files themselves (for example, `src/`, `bin/`, and `README.md`), not a nested `starter/` wrapper. Do not create a separate `deployment/oci-starter` wrapper. Do not overwrite an existing nonempty project root: use a dated/suffixed directory or ask the user.
2. Resolve all OCI Starter options by combining user choices and defaults. Before downloading, show the customer every resolved option and its value, clearly marking values that came from defaults. Redact any real secret value. For a setting found through the profile-inspection rules above, label it profile-backed (or conditionally profile-backed when the export is conditional), rather than unset. Identify only values that are neither configured nor profile-backed as required-but-unset. Ask for explicit confirmation that this configuration should be used to download `starter.zip`.
3. Only after that confirmation, run `scripts/oci_starter_url.py` with the resolved values to validate them and print the OCI Starter archive URL. Pass values as `key=value`. Use `--format curl` to emit a safely quoted download command, then run that command to download the archive.
4. Unzip the archive into a temporary location, move the contents of its generated `starter/` directory into the project root, and run `git init` in the project root to create a local Git repository. Immediately create a baseline commit of the untouched scaffold (for example, `git add -A && git commit -m "Initial OCI Starter scaffold"`) before reading the root `README.md` or making application changes. Use the existing Git identity; if none is configured, report the failure and ask the user to configure it rather than setting an identity. Treat the OCI Starter scaffold as read-only whenever possible: never rename, delete, or broadly reformat generated files.
5. Treat the generated `bin/` directory as strictly read-only. Do not modify, delete, regenerate, or commit changes to it. If the application needs a change that appears to require `bin/`, first use documented configuration or application-layer extension points; explain the blocker if none exist.
6. Find the generated application directory (expected `src/app`; if absent, locate it from the README) and implement or copy the customer program there. Adapt only the files required for the customer application, such as its dependencies, configuration, tests, and health endpoints, following the scaffold's conventions.
7. Keep secrets out of source control. Use OCI variables, Vault/secret references, or documented local environment variables as appropriate. When a generated `terraform.tfvars` value is literally `__TO_FILL__`, use the profile-inspection rules above before treating it as undefined. If the profile has a direct or conditional export for either `setting` or `TF_VAR_setting`, report it as profile-backed without reading aloud, copying, or logging its value; let `starter.sh` source the profile rather than copying the secret into source control. If the profile has neither export, ask the user to configure the value before deployment.
8. Validate the app using the scaffold's documented local checks. After creating the project, explain concisely what was created, including the project root, scaffold/application layout, changed application files, and exact next deployment command from the generated README. State every resolved option used to create the project (including defaults), not only the options explicitly supplied by the user. Then ask whether the Terraform resource prefix should remain `starter` or be changed to a different lowercase alphanumeric prefix of at most eight characters that starts with a letter. This prefix is defined in `terraform.tfvars`; do not edit that file until the user answers. After confirmation, update only its prefix value and report the change.

Do not run Terraform apply, Resource Manager apply, or any OCI provisioning command without a separate explicit instruction to deploy resources.

## Run OCI Starter commands

When running any `./starter.sh ...` command, follow its execution until it reaches a terminal outcome: success or error. Do not stop monitoring merely because the command is quiet, appears stalled, or runs for a long time. Continue waiting and reporting meaningful output as it becomes available; only report completion after the process exits.

Treat a request to run `./starter.sh build` or `./starter.sh destroy` as a request for a privileged cloud operation, not as implicit permission to execute it. Before either command:

1. Inspect the generated `README.md`, `terraform.tfvars`, and relevant Terraform configuration to identify the configured resource types and scope. Do not expose credentials or secret values.
2. Tell the end user that the command will connect to OCI over the network and use their locally configured OCI credentials. For `build`, explain that it will run Terraform and create the configured OCI resources, then configure the database and build/deploy the application and UI where the scaffold supports those steps. List the specific resource types expected from the generated configuration. For `destroy`, explain that it will connect to OCI and use those credentials to destroy the Terraform-managed resources associated with the configured prefix; list the resource types expected to be removed.
3. For `./starter.sh build`, request one combined elevated sandbox approval for `./starter.sh build --auto-approve`. The approval question must state both that it performs the cloud operation described above and that it needs outbound network access to OCI using the user's locally configured credentials. State that Terraform changes will be applied noninteractively. Treat approval of this single escalation as the user's explicit permission for the build; do not ask a separate, sequential cloud-operation confirmation. Run it with `require_escalated`; do not first run it in the restricted sandbox, including as a connectivity check. Elevated execution is required so OCI and provider-registry connectivity uses the user's available network access.
4. For `./starter.sh destroy`, ask for explicit cloud-operation permission immediately before running it. Do not run `terraform destroy` or another command that removes OCI resources until the user grants that permission. Then request elevated sandbox permission for the exact `./starter.sh destroy` command, explaining that it needs outbound internet access to OCI. Run the relevant command with `require_escalated` only after its required approval or approvals are granted; do not first attempt it in the restricted sandbox. Report its result and any resource changes it reports.

## Redeploy application changes

After the project has been successfully created and deployed, use the application-only redeploy path when the only changes since the last deployment are under `src/app/`:

1. Verify the changed-file scope with version-control status/diff when available. If it cannot be verified, ask the user to confirm that only `src/app/` changed; do not assume this is true.
2. Explain that `./starter.sh build app` redeploys only the application portion from `src/app/` and does not run the full Terraform/database/UI build. State that it still needs network access to OCI and uses the user's locally configured OCI credentials to update the deployed application.
3. Request one combined elevated sandbox approval for the exact `./starter.sh build app` command. The approval question must state both that it redeploys the application to OCI using the user's locally configured credentials and that it needs outbound network access. Treat approval of this single escalation as the user's explicit permission for the redeploy; do not ask a separate, sequential cloud-operation confirmation. Run it with `require_escalated` only after that approval is granted; do not first attempt it in the restricted sandbox, including as a connectivity check. Report the result.

## URL helper

Run from the skill directory or give an absolute path:

```sh
python3 scripts/oci_starter_url.py \
  language=java deploy_type=public_compute
```

The helper applies defaults, sends every resolved allowed option as a starter endpoint parameter, and rejects unsupported overrides. It retains the resolved configuration in the output manifest so it can be applied after inspecting the generated README.

## Failure handling

- If the endpoint download fails, show the HTTP error and retain the intended URL; do not substitute a different template.
- If the generated layout differs from expectations, follow its README and report the difference.
- If an option needed by the desired architecture has no endpoint mapping, state that limitation and inspect the generated README before setting it manually.
