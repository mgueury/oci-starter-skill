# OCI Starter Skill

Use this skill to create applications and OCI Starter projects for Oracle Cloud Infrastructure. It guides an agent through choosing an OCI Starter architecture, downloading the appropriate scaffold, and implementing the application in it.

## Before you install

Install the **entire** `oci-starter-skill` folder, not only `SKILL.md`. The skill depends on the files in `scripts/` and `references/`; retaining `agents/` and `helper/` is also recommended.

The commands below assume that the folder you downloaded or cloned is named `oci-starter-skill` and that your terminal is in its parent directory.

> **Windows notice:** The Windows paths and PowerShell commands below are provided as a best-effort reference and have **not been tested on Windows**.

## Codex desktop

### macOS and Linux

Copy the complete folder into your global Codex skills directory:

```sh
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R oci-starter-skill "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Restart Codex desktop, then ask it to use `$oci-starter-skill`, for example:

```text
Use $oci-starter-skill to create a Python application for Kubernetes with OCI Starter.
```

### Windows (untested)

In PowerShell, copy the complete folder to `%USERPROFILE%\\.codex\\skills`:

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\\.codex\\skills"
Copy-Item -Recurse -Path .\\oci-starter-skill -Destination "$env:USERPROFILE\\.codex\\skills\\oci-starter-skill"
```

Restart Codex desktop and use the same prompt shown above.

## ChatGPT desktop

1. Create a ZIP archive whose root contains `SKILL.md` alongside `scripts/`, `references/`, `agents/`, and `helper/`. Do not zip an extra enclosing `oci-starter-skill/` directory.

   On macOS or Linux, from inside the `oci-starter-skill` folder:

   ```sh
   zip -r ../oci-starter-skill.zip SKILL.md scripts references agents helper
   ```

   On Windows, create the equivalent archive in File Explorer or PowerShell. This workflow is untested on Windows.

2. In ChatGPT desktop, open **Plugins** in the sidebar, open the **Skills** tab, then select **Create** → **Upload**.
3. Select `oci-starter-skill.zip` and complete the scan or review process, if prompted.
4. Start a new chat and ask ChatGPT to use `$oci-starter-skill`.

Skill uploads are available only for eligible accounts and may be disabled by your workspace administrator. Skills installed in ChatGPT desktop are managed separately from Codex skills.

## OpenCode

OpenCode discovers directory-based skills that contain `SKILL.md`. Keep the folder name `oci-starter-skill` so its skill ID remains `oci-starter-skill`.

### Global installation (macOS and Linux)

Make the skill available in all OpenCode projects:

```sh
mkdir -p "$HOME/.config/opencode/skills"
cp -R oci-starter-skill "$HOME/.config/opencode/skills/"
```

### Project installation (macOS and Linux)

Make the skill available only in one project. Run this from the parent directory containing both the target project and `oci-starter-skill`:

```sh
mkdir -p my-project/.opencode/skills
cp -R oci-starter-skill my-project/.opencode/skills/
```

### Windows (untested)

Use the corresponding OpenCode skill directory, typically `%USERPROFILE%\\.config\\opencode\\skills` for a global installation, or `.opencode\\skills` within a project. For example, in PowerShell:

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\\.config\\opencode\\skills"
Copy-Item -Recurse -Path .\\oci-starter-skill -Destination "$env:USERPROFILE\\.config\\opencode\\skills\\oci-starter-skill"
```

Restart OpenCode, then request the skill by name:

```text
Use the oci-starter-skill to create a Python application for Kubernetes with OCI Starter.
```

## Verify and troubleshoot

- Confirm the installed directory is named `oci-starter-skill` and directly contains `SKILL.md`.
- Confirm the installed copy also contains `scripts/oci_starter_url.py` and `references/options.md`.
- Restart the relevant desktop app after installing or updating the skill.
- If the skill is not discovered, check for an accidentally nested path such as `oci-starter-skill/oci-starter-skill/SKILL.md`.
- When updating an existing installation, replace the complete installed skill folder so supporting files stay in sync with `SKILL.md`.

For product-specific availability and upload permissions, see the official [Skills in ChatGPT guide](https://help.openai.com/en/articles/20001066-skills-in-chatgpt/) and the [OpenCode skills documentation](https://opencode.ai/v2/docs/skills).
