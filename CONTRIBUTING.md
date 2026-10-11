# Maintaining the NOIR profile

This repository supplies the README shown on [NoirPrimordial7's profile](https://github.com/NoirPrimordial7). Changes should preserve factual project descriptions, working links, accessible image descriptions and the illustrated visual direction.

## Check a change locally

From the repository root, use Python 3.12:

```sh
python -m venv .venv
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r scripts/requirements.txt
python scripts/validate_assets.py
```

The validator reads the committed files without network access. It checks local references, SVG structure, project cards, the README/preview match, and the hero animation's frame count, duration, loop and size budget. GitHub Actions runs the same validator on pull requests and pushes to `main`.

## Update project facts and generated content

The current project descriptions and URLs are defined in [`scripts/refresh_profile.py`](scripts/refresh_profile.py). To change them, edit its `PROJECTS` entries and run:

```sh
python scripts/refresh_profile.py
python scripts/validate_assets.py
```

The builder updates the README, project cards, case studies, resume, archive metadata and [`preview/index.html`](preview/index.html). Include those related generated files in the same pull request. Editing only a generated file can lose the change the next time the builder runs.

Open `preview/index.html` locally and check the affected content at desktop and phone widths, in both themes, and with reduced motion. Keep the hero still image available. Record the factual source for changes to education, experience, project status or model-performance claims.

## Propose a focused improvement

Use an issue to describe a broken link, inaccurate description, accessibility problem or reproducible validation failure. Include the affected path, expected behavior and evidence; avoid private documents, credentials and personal information about other people.

Keep each pull request focused on one useful improvement. Explain the resulting behavior and report validation honestly. Credit actual collaborators using Git's `Co-authored-by` trailer only when they contributed to the commit.

An illustrative trailer is:

```text
Co-authored-by: Collaborator Name <their-github-associated-email>
```

Replace the placeholders with the collaborator's agreed identity; do not add people who did not contribute. No open-source license has been selected for this repository. Check [`assets/tech/ATTRIBUTION.md`](assets/tech/ATTRIBUTION.md) and the accompanying license before reusing third-party logos.

