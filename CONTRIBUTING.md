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

**In your browser (easiest).** Open `src/doc/index.rst` on GitHub, click the
pencil (✏️) icon, make your edit, write a short title, choose **Propose changes**,
then **Create pull request**.

**With Git locally.**

```shell
git checkout -b update-scope
# edit src/doc/index.rst
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

The charter is a single source file:

- `src/doc/index.rst` — the **charter itself**: the title, the front matter (version, date, status), and all its numbered sections. Replace the text in `<...>` with your own content.

Author guidance is built into that file: **source comments** (blocks beginning with `..`) above each section explain what to write, and never appear in the published HTML or PDF.

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
sphinx-build -b html src/doc target/html
```

Open `target/html/index.html` in a browser.

**Live preview (recommended)** — rebuilds and refreshes the browser as you save. On Windows:

```powershell
./preview.ps1
```

This starts a local server at <http://127.0.0.1:8000>, sets up PlantUML for you, and forces a full rebuild on every save so your changes always appear.

## 4. Edit the content

All of your content lives in `src/doc/index.rst`. Edit it directly:

- **Replace the placeholders.** Every `<...>` is a prompt for text you supply. Follow the per-section author guidance in the source comments, and delete sections marked *optional* if they do not apply.
- **Text, tables, lists, admonitions** — the file itself is the best reference for the markup. For example, the Charter Information and section tables are reStructuredText `list-table` directives you can copy and adapt.
- **Add an image** — put it in `src/doc/images/` and reference it with a relative path. Use a single PNG so it works in both HTML and PDF.

## 5. Publish

Pushing to the `main` branch automatically builds the HTML site and PDF and deploys them to GitHub Pages, via the workflow in `.github/workflows/docs.yml`.

To enable it on a new repository: in **Settings → Pages**, set **Source** to **GitHub Actions**. The published site then updates on every push.

## 6. Build the PDF locally (optional)

The online build produces the PDF for you. To build it yourself you need a LaTeX distribution (TeX Live or MiKTeX):

```shell
sphinx-build -b latex src/doc target/latex
make -C target/latex
```
