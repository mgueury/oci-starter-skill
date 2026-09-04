# OCI Starter options

Use these canonical `key=value` inputs with `scripts/oci_starter_url.py`.

## Defaults

Apply these values unless the user explicitly overrides them:

| Input key | Default |
| --- | --- |
| `prefix` | `starter` (1–8 lowercase letters or numbers; must start with a letter) |
| `java_framework` | `springboot` |
| `java_vm` | `graalvm` |
| `java_version` | `25` |
| `python_framework` | `fastapi` |
| `ui_type` | `html` |
| `db_type` | `atp` |
| `license_model` | `LICENSE_INCLUDED` |
| `app_mode` | `terraform` |
| `mode` | `CLI` |
| `infra_as_code` | `terraform_local` |
| `db_password` | `TO_FILL` |
| `oke_type` | `managed` |
| `security` | `none` |
| `build_host` | `terraform` |

`language` and `deploy_type` intentionally have no defaults. `db_password=TO_FILL` is a placeholder only: request or generate a secure value only at the step that needs it, and never write that value to version control or a deployment manifest.

| Input key | Allowed values |
| --- | --- |
| `language` | `java`, `node`, `python`, `dotnet`, `go`, `php`, `ords`, `apex`, `none` |
| `deploy_type` | `public_compute`, `private_compute`, `instance_pool`, `kubernetes`, `function`, `container_instance` |
| `java_framework` | `springboot`, `helidon`, `helidon4`, `tomcat`, `micronaut` |
| `java_vm` | `jdk`, `graalvm`, `graalvm-native` |
| `java_version` | `8`, `11`, `17`, `21`, `25` |
| `python_framework` | `fastapi`, `langgraph`, `responses` |
| `ui_type` | `html`, `jet`, `angular`, `reactjs`, `jsp`, `php`, `api`, `apex`, `none` |
| `db_type` | `atp`, `autonomous`, `database`, `dbsystem`, `rac`, `db_free`, `pluggable`, `pdb`, `mysql`, `psql`, `opensearch`, `nosql`, `none` |
| `license_model` | `LICENSE_INCLUDED`, `BRING_YOUR_OWN_LICENSE` |
| `infra_as_code` | `terraform_local`, `terraform_object_storage`, `resource_manager`, `from_resource_manager` |
| `app_mode` | `terraform`, `app` |
| `mode` | `CLI`, `GIT`, `ZIP` |
| `shape` | `amd`, `freetier_amd`, `ampere`, `arm` |
| `db_install` | `default`, `kubernetes` |
| `tls` | `none`, `new_http_01`, `new_dns_01`, `existing_ocid`, `existing_dir` |
| `oke_type` | `managed`, `virtual_node` |
| `security` | `none`, `openid` |
| `build_host` | `terraform`, `bastion` |

`prefix` is supported configuration fields. `db_password` is deliberately not accepted as a helper argument; manage the real secret using the generated scaffold's supported secret mechanism.

Every key in the helper's `ALLOWED` set is a supported download endpoint query parameter. The helper sends every resolved allowed option, using its canonical key as the query name.

For example: `https://www.ocistarter.com/app/zip?prefix=starter&language=java&deploy_type=public_compute&ui_type=html&db_type=atp`.
