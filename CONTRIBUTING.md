# Contributing

This repository holds an FG-TIDA Working Group charter. Anything you do here — an
edit, a commit, a pull request, an issue, or a comment — is a contribution offered
as input to the Working Group's work and may be incorporated into the charter.

You do not need to be a Git or reStructuredText expert to contribute. If in doubt,
open an issue and ask — the chairs and editors are usually happy to help a
contribution into shape.

## Ways to contribute

- **Pull request** — propose a concrete change to the charter text.
- **Issue** — raise a problem, question, or suggestion for discussion.
- **Mailing list** — discuss direction and larger questions with the Working Group.

### Propose a change with a pull request

The charter text lives in one file, `charter.md` (Markdown) in the repository root.
It is the single source of truth: `src/doc/index.rst` is generated from it during
the build and is not part of the repository.

**In your browser (easiest).** Open `charter.md` on GitHub, click the
pencil (✏️) icon, make your edit, write a short title, choose **Propose changes**,
then **Create pull request**.

**With Git locally.**

```shell
git checkout -b update-scope
# edit charter.md
git commit -am "Describe your change"
git push origin update-scope
```

Then open a pull request against `main`. Example branch names: `update-scope`,
`update-deliverables`, `charter-v0.2`, `review-milestones`.

### Open an issue

Use issues to report errors, raise open questions, or suggest changes you are not
ready to draft yourself. A clear title and a short description of the problem and
where it occurs is enough to start a discussion.

## Review and adoption

- Changes are made through pull requests against `main`; **do not push to `main`
  directly**, so every change keeps a review and decision history.
- Pull requests are reviewed by the Working Group before they are merged.
- Chairs merge approved changes and decide when to cut a new charter version
  (update the revision history when scope or deliverables change materially).

### Before you submit

- Replace any `<...>` placeholders you touched — the published charter should
  contain no unresolved template values.
- Keep the charter concise (approximately 600–1,200 words).
- Keep people's names only in the **Group Information** section.
- Check that the preview builds (GitHub Actions, or locally — see below).

## Conduct

Participation in this repository follows the ITU-T and FG-TIDA participation,
conduct, and IPR rules. Please be respectful and constructive in issues, pull
requests, and reviews.

---

The rest of this guide explains how to build, preview, and publish the charter.

# How to use this template

This guide explains how to start a charter from this template, build it locally, edit its content, and publish it.

Throughout, **"charter"** means the whole document you are producing. The charter is organised into numbered **sections** (Group Information, Background, Goals, and so on) — all held in a single source file.

## 1. Start your charter

Create your own copy of the template:

- On GitHub, click **Use this template → Create a new repository**, or
- clone this repository and push it to a repository of your own.

In this repository the charter is a single Markdown file:

- `charter.md` is the **charter itself**: the title, the Charter Information table (version, date, status), and all its numbered sections.
- `tools/md2charter_rst.py` generates `src/doc/index.rst` and `src/doc/charter-meta.json` from it. Both are generated files, listed in `.gitignore`, never edited by hand.
- `src/doc/conf.py` reads title, acronym, version and status from `charter-meta.json`, so they are changed in `charter.md` only.

Author guidance for each section is in [WG-ONBOARDING.md](WG-ONBOARDING.md) and in the [FG-TIDA charter template](https://github.com/FG-TIDA/wg-charter-template/blob/main/src/doc/index.rst).

Keep the finished charter short — approximately 600–1,200 words.

## 2. Set up a local build environment

You need this only to preview locally — the online build (step 5) needs no setup. To build on your own machine:

1. **Install Python 3.10+** (3.12 recommended).
2. **Create a virtual environment and install the dependencies.** The live-preview script (`preview.ps1`) expects a `.venv` in the repository root, so create it there. In PowerShell:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

3. **For diagrams — install Java and PlantUML** (optional; skip if your charter has no `.. uml::` diagrams):

   - Install Java 17 or newer.
   - Download `plantuml.jar` from <https://plantuml.com/download> and place it in the repository root.
   - Tell the build where it is by setting the `PLANTUML` environment variable. In PowerShell:

     ```powershell
     $env:PLANTUML = "java -jar $PWD/plantuml.jar"
     ```

   Without this, the build still succeeds but diagrams show as broken images locally. (The online build installs PlantUML automatically.)

## 3. Build and preview

**One-off build:**

```shell
python3 tools/md2charter_rst.py charter.md src/doc/index.rst
sphinx-build -b html src/doc target/html
```

Run the first command again after every change to `charter.md`.

Open `target/html/index.html` in a browser.

**Live preview (recommended)** — rebuilds and refreshes the browser as you save. On Windows:

```powershell
./preview.ps1
```

This starts a local server at <http://127.0.0.1:8000>, sets up PlantUML for you, and forces a full rebuild on every save so your changes always appear.

## 4. Edit the content

All of your content lives in `charter.md`. Edit it directly, the converter understands this Markdown:

- one `# ` title in the form `FG-TIDA WG1: <Full name> (<ACRONYM>)`, `## ` sections and `### ` subsections,
- paragraphs with one sentence per line,
- `* ` bullets, a second sentence of a bullet goes on an indented continuation line,
- pipe tables (`|a|b|`), including the Charter Information table, whose version and status also feed the PDF cover.
- **Add an image** — put it in `src/doc/images/` and reference it with a relative path. Use a single PNG so it works in both HTML and PDF.

## 5. Publish

Pushing to the `main` branch automatically generates `src/doc/index.rst` from `charter.md`, builds the HTML site and PDF and deploys them to GitHub Pages, via the workflow in `.github/workflows/docs.yml`.

To enable it on a new repository: in **Settings → Pages**, set **Source** to **GitHub Actions**. The published site then updates on every push.

## 6. Build the PDF locally (optional)

The online build produces the PDF for you. To build it yourself you need a LaTeX distribution (TeX Live or MiKTeX):

```shell
python3 tools/md2charter_rst.py charter.md src/doc/index.rst
sphinx-build -b latex src/doc target/latex
make -C target/latex
```
