# Starting an FG-TIDA Working Group Charter

This guide explains how an FG-TIDA Working Group (WG) creates, maintains and publishes its charter using the FG-TIDA Working Group Charter template.

No prior Sphinx or reStructuredText experience is required. Working Group editors update the charter source files in GitHub, and the web version and PDF are generated automatically.

---

## 1. Purpose of a Working Group Charter

An FG-TIDA Working Group Charter defines the mandate of a Working Group.

It describes:

- the problem the Working Group is expected to address;
- the goals of the Working Group;
- what is in scope and what is explicitly out of scope;
- the deliverables the Working Group intends to produce;
- the expected milestones;
- dependencies and coordination with other groups;
- the criteria for completing the chartered work.

The charter is a scope and delivery agreement. It is not intended to be a tutorial, technical specification, research paper or detailed description of the solution.

A final charter should normally remain concise:

- approximately **600–1,200 words**;
- generally **two to three pages**, excluding the cover page and administrative tables where appropriate.

---

## 2. FG-TIDA Repository Model

FG-TIDA uses **one GitHub organization per Working Group**, plus a central
organization that holds the shared templates.

**Central organization — `FG-TIDA`.** Managed by the FG-TIDA management team, it
holds the templates that every Working Group copies:

- `FG-TIDA/wg-charter-template` — the charter template (this repository);
- `FG-TIDA/spec-template` — the specification template.

**One organization per Working Group**, for example `fg-tida-wg1`. Its **owners
(admins)** are the Working Group chairs together with an FG-TIDA management
representative. Organization and repository names may be adjusted by the FG-TIDA
management team, but should remain short, predictable, and clearly tied to the
Working Group.

Within its own organization, each Working Group keeps **one repository per
deliverable**, named `wg<n>-<acronym>-<name>`, where `<n>` is the Working Group
number and `<acronym>` is the Working Group's acronym:

- exactly **one charter** repository, created from `wg-charter-template`, named
  `wg<n>-<acronym>-charter` — for example `wg1-ra-charter`;
- **one repository per specification**, created from `spec-template`, named
  `wg<n>-<acronym>-<spec-name>` — for example `wg1-ra-aai`, `wg1-ra-<second-spec>`.

Keeping each deliverable in its own repository lets each one be versioned,
reviewed, built, and published independently.

Each repository provides:

- the editable source;
- version history through Git;
- Pull Request review;
- an automatically generated HTML publication, at
  `https://fg-tida-wg<n>.github.io/<repository-name>/`;
- an automatically generated PDF;
- an issue tracker for discussion;
- synchronization to the corresponding FG-TIDA GitLab repository where configured.

---

## 3. Create a New Working Group Charter

A new Working Group creates its **charter** repository from the charter template, inside the Working Group's own GitHub organization (created beforehand by the FG-TIDA management team — see section 2). Each specification is created the same way from `FG-TIDA/spec-template`.

### Step 1 — Open the template

Go to:

`https://github.com/FG-TIDA/wg-charter-template`

### Step 2 — Create the repository

Click:

**Use this template → Create a new repository**

Set:

**Owner**

Your Working Group's own organization, for example `fg-tida-wg1` — **not** the central `FG-TIDA` organization (that one holds only the templates).

**Repository name**

Follow the naming convention `wg<n>-<acronym>-charter` for the charter — for example:

`wg1-ra-charter`

Set the repository visibility according to FG-TIDA policy.

Then click:

**Create repository**

### Step 3 — Enable GitHub Pages

In the new repository, go to:

**Settings → Pages**

Under **Build and deployment**, set:

**Source → GitHub Actions**

No additional Save button is normally required.

### Step 4 — Verify the initial build

Go to:

**Actions → Build and deploy docs**

Run the workflow if necessary.

A successful run should complete both:

```text
Build
Deploy
```

The published charter site will normally be available at:

```text
https://fg-tida-wg<n>.github.io/<repository-name>/
```

The downloadable PDF is published as:

```text
wg-charter.pdf
```

For example:

```text
https://fg-tida-wg1.github.io/wg1-ra-charter/wg-charter.pdf
```

---

## 4. Main Files to Edit

Most Working Group editors only need to work with two files:

```text
src/doc/index.rst
src/doc/conf.py
```

The build infrastructure should normally not be modified by Working Group authors.

---

## 5. Complete the Charter in `src/doc/index.rst`

The actual Working Group Charter is contained in:

```text
src/doc/index.rst
```

The template contains all mandatory and optional charter sections.

These include:

1. Group Information
2. Background and Problem Statement
3. Goals
4. Scope and Non-Goals
5. Programme of Work and Deliverables
6. Milestones
7. Coordination, Dependencies and Liaisons
8. Terminology
9. Working Methods
10. Security and Privacy Considerations
11. Success Criteria and Conclusion
12. Revision History

Sections identified as mandatory should remain in the charter.

Optional sections may be removed when they do not contain useful information.

---

## 6. Replace All Placeholders

Template values are written using angle brackets.

For example:

```text
<WG acronym>
<Full name of the Working Group>
<v0.x>
<YYYY-MM-DD>
<Deliverable 1>
```

Replace every placeholder with the information for the actual Working Group.

Before submitting the charter for approval, search the source for:

```text
<
```

to help identify any remaining placeholders.

The published charter should not contain unresolved template values.

---

## 7. Author Guidance

The charter template contains instructions for editors using reStructuredText comments.

For example:

```rst
..
   AUTHOR GUIDANCE:

   State what the Working Group will produce and why.

   Keep this section concise.
```

These comments are visible in the source file but are **not rendered in the HTML or PDF**.

Therefore, authors should normally leave the guidance comments in the source repository.

There is no need to delete the guidance before publication.

The final HTML and PDF contain only the completed charter content.

---

## 8. Writing Style

The charter should be concise and operational.

Use the future tense and third person.

Preferred:

```text
The Working Group will develop a technical report describing...
```

Avoid:

```text
We plan to develop...
```

Avoid marketing language, promotional claims and unnecessary product or company names.

The charter should explain **what the Working Group will do**, not provide a detailed implementation of how the technical solution will work.

---

## 9. Scope and Non-Goals

The **Scope and Non-Goals** section is one of the most important parts of the charter.

The charter should clearly identify both:

```text
In Scope
```

and:

```text
Out of Scope / Non-Goals
```

Non-goals help prevent scope creep and clarify boundaries with:

- other FG-TIDA Working Groups;
- ITU-T SG17 Questions;
- other ITU-T groups;
- external standards-development organizations;
- other relevant initiatives.

Where another group owns a neighbouring topic, identify that group explicitly.

---

## 10. Deliverables

Each deliverable should have:

- a clear title;
- a short description;
- relevant input documents, where applicable.

A contribution or existing draft may be identified as an input to the work.

It should not automatically be described as adopted Working Group text unless the appropriate FG-TIDA process has taken place.

Avoid open-ended deliverables such as:

```text
Ongoing analysis
```

Every deliverable should represent something that can eventually be considered complete.

---

## 11. Milestones

Milestones should be:

- dated;
- measurable;
- realistic;
- aligned with the FG-TIDA meeting calendar.

Typical milestones include:

```text
First draft available in the repository
Working Group agreement
Submission to the FG-TIDA plenary
```

Milestones should not extend beyond the expected lifetime of the Focus Group.

Where a milestone depends on an external organization, make that dependency explicit.

---

## 12. Coordination and Dependencies

Identify only groups and organizations with a real dependency or coordination requirement.

These may include:

- another FG-TIDA Working Group;
- an ITU-T SG17 Question;
- another ITU-T Study Group or Focus Group;
- an external standards-development organization;
- a relevant industry or research initiative.

For each entry, explain briefly what the coordination concerns.

Do not list organizations merely because they work in a related field.

Do not imply that a formal liaison relationship exists unless one has actually been established.

---

## 13. Update `src/doc/conf.py`

Document and PDF metadata is configured near the top of:

```text
src/doc/conf.py
```

Working Group editors should update the metadata values only.

For example:

```python
project = 'WG-TF'
release = '0.1'
html_title = 'WG-TF Charter'
author = 'FG-TIDA'

cover_title = 'WG1: Trust Frameworks'
cover_series = 'FG-TIDA Working Group Charter'
cover_subject = 'WG-TF'
cover_subtitle = 'Charter version 0.1 — Draft'
```

These values are reused in the HTML publication and PDF cover.

Do not modify the Sphinx, Furo, PlantUML or LaTeX infrastructure unless there is a specific template-maintenance requirement.

---

## 14. Charter Status

Recommended charter statuses include:

```text
Draft
Under Review
Approved
```

Where useful, FG-TIDA may use more detailed stages such as:

```text
Draft
WG Review
WG Approved
FG-TIDA Review
FG-TIDA Approved
```

Use whichever lifecycle is formally adopted by FG-TIDA management.

The status should be reflected consistently in:

- `src/doc/index.rst`;
- `src/doc/conf.py`;
- the PDF cover;
- the revision history.

---

## 15. Revision History

Every charter should maintain its revision history.

Example:

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-10-21 | First draft |
| 0.2 | 2026-11-15 | Scope updated following WG review |
| 1.0 | 2026-11-30 | Approved by FG-TIDA |

When the scope or deliverables materially change, create a new charter version rather than silently expanding the existing charter.

Routine milestone updates may be managed without a full rechartering process where FG-TIDA procedures allow it.

---

## 16. Recommended Git Workflow

Working Group contributors should normally not edit the published `main` branch directly.

Recommended workflow:

```text
Create branch
      ↓
Edit charter
      ↓
Commit changes
      ↓
Open Pull Request
      ↓
WG review
      ↓
Resolve comments
      ↓
Approve
      ↓
Merge into main
      ↓
HTML and PDF rebuilt automatically
```

Example branch names:

```text
update-scope
update-deliverables
charter-v0.2
review-milestones
```

Pull Requests provide a clear review and decision history for charter changes.

---

## 17. Publishing

Every push or approved merge to `main` triggers the documentation workflow.

The workflow:

```text
Source files
     ↓
Sphinx
     ↓
HTML
     +
PDF
     ↓
GitHub Pages
```

The PDF filename is:

```text
wg-charter.pdf
```

Do not manually edit the generated HTML or PDF.

The `.rst` source is the authoritative editable source of the charter.

---

## 18. GitHub to GitLab Synchronization

Where synchronization is configured, changes pushed to GitHub are mirrored automatically to the corresponding FG-TIDA GitLab project.

GitHub remains the primary authoring repository unless FG-TIDA management establishes a different process.

Synchronization should use repository-specific credentials following the principle of least privilege.

A token used for one Working Group repository should not unnecessarily grant write access to unrelated FG-TIDA repositories.

---

## 19. Previewing the Charter

### Option A — GitHub Pages

The easiest method is to push the changes and inspect the generated GitHub Pages publication.

This requires no local installation.

### Option B — Local preview

For contributors who want to build the document locally, see:

```text
CONTRIBUTING.md
```

The local build can be used to preview HTML and PDF output before creating a Pull Request.

---

## 20. Before Submitting a Charter

Check the following before requesting approval:

- [ ] Is the charter approximately 600–1,200 words?
- [ ] Is every mandatory section complete?
- [ ] Have optional sections with no useful content been removed?
- [ ] Does every deliverable have at least one milestone?
- [ ] Is there an explicit list of non-goals?
- [ ] Are overlaps with other FG-TIDA WGs identified?
- [ ] Are relevant SG17 Questions identified?
- [ ] Are people's names confined to the Group Information section?
- [ ] Are vendor-specific or promotional statements avoided?
- [ ] Have all `<placeholder>` values been replaced?
- [ ] Is the charter version correct?
- [ ] Is the charter status correct?
- [ ] Has the revision history been updated?
- [ ] Does the HTML build successfully?
- [ ] Does `wg-charter.pdf` build successfully?

---

## 21. Getting Help

For questions about the content of a particular Working Group Charter, open an issue in that Working Group's charter repository.

For problems with the common template, PDF generation, Sphinx configuration or GitHub Actions workflow, open an issue in:

`FG-TIDA/wg-charter-template`

For local build instructions and technical authoring details, see:

`CONTRIBUTING.md`
