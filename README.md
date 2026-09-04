# OCI Starter Skill

Use this skill to create applications and OCI Starter projects for Oracle Cloud Infrastructure. It guides an agent through choosing an OCI Starter architecture, downloading the appropriate scaffold, and implementing the application in it.

This is a skill that should work with all coding agents. Below, you will find how to instal it for Codex, ChatGPT Desktop and OpenCode.

> **Windows notice:** The Windows paths and PowerShell commands below are provided as a best-effort reference and have **not been tested on Windows**.

## Codex

### macOS and Linux

Clone the skill directly into your global Codex skills directory:

```sh
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cd "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/mgueury/oci-starter-skill.git
```

Restart Codex desktop, then ask it to use `$oci-starter-skill`, for example:

```text
Use $oci-starter-skill to create a Python application for Kubernetes with OCI Starter.
```

### Windows (untested)

In PowerShell, clone the skill into `%USERPROFILE%\\.codex\\skills`:

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\\.codex\\skills"
Set-Location "$env:USERPROFILE\\.codex\\skills"
git clone https://github.com/mgueury/oci-starter-skill.git
```

Restart Codex desktop and use the same prompt shown above.

## ChatGPT desktop

1. Download [oci-starter-skill-main.zip](https://github.com/mgueury/oci-starter-skill/archive/refs/heads/main.zip).
2. In ChatGPT desktop, open **Plugins** in the sidebar, open the **Skills** tab, then select **Create** → **Upload**.
3. Select the ZIP archive and complete the scan or review process, if prompted.
4. Start a new chat and ask ChatGPT to use `$oci-starter-skill`.

Skill uploads are available only for eligible accounts and may be disabled by your workspace administrator. Skills installed in ChatGPT desktop are managed separately from Codex skills.

## OpenCode

OpenCode discovers directory-based skills that contain `SKILL.md`. Keep the folder name `oci-starter-skill` so its skill ID remains `oci-starter-skill`.

### Global installation (macOS and Linux)

Clone the skill to make it available in all OpenCode projects:

```sh
mkdir -p "$HOME/.config/opencode/skills"
cd "$HOME/.config/opencode/skills"
git clone https://github.com/mgueury/oci-starter-skill.git
```

### Project installation (macOS and Linux)

Make the skill available only in one project. Replace `my-project` with your project directory:

```sh
mkdir -p my-project/.opencode/skills
cd my-project/.opencode/skills
git clone https://github.com/mgueury/oci-starter-skill.git
```

### Windows (untested)

Use the corresponding OpenCode skill directory, typically `%USERPROFILE%\\.config\\opencode\\skills` for a global installation, or `.opencode\\skills` within a project. For example, in PowerShell:

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\\.config\\opencode\\skills"
Set-Location "$env:USERPROFILE\\.config\\opencode\\skills"
git clone https://github.com/mgueury/oci-starter-skill.git
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
- When updating a cloned installation, run `git pull` from its `oci-starter-skill` directory, then restart the app.

For product-specific availability and upload permissions, see the official [Skills in ChatGPT guide](https://help.openai.com/en/articles/20001066-skills-in-chatgpt/) and the [OpenCode skills documentation](https://opencode.ai/v2/docs/skills).
