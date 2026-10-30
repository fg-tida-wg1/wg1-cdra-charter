#!/usr/bin/env python3
"""Generate the Sphinx sources of the charter from charter.md.

charter.md is the single source of truth of this charter.
This script writes two generated files, both listed in .gitignore:

  src/doc/index.rst          the charter in the format of the FG-TIDA charter template
  src/doc/charter-meta.json  title, acronym, version and status, read by src/doc/conf.py

Usage:
  python3 tools/md2charter_rst.py charter.md src/doc/index.rst [--template TEMPLATE_INDEX_RST]

--template copies the AUTHOR GUIDANCE comment blocks of the FG-TIDA template into
the generated file (optional, comments never appear in the HTML or PDF).

Supported Markdown: one "# " title, "## " sections, "### " subsections, paragraphs
(one sentence per line), "* " bullets with indented continuation lines, and pipe
tables. Standard library only.
"""
import json, os, re, sys

WIDTHS = {
    'charter information': '30 70',
    'group information': '38 62',
    'programme of work and deliverables': '6 29 45 20',
    'milestones': '30 70',
    'coordination, dependencies and liaisons': '35 65',
    'revision history': '18 22 60',
}


def norm(title):
    title = title.replace('\\.', '.').strip()
    return re.sub(r'^\d+\.\s*', '', title).strip().lower()


def cells(row):
    return [c.strip() for c in row.strip().strip('|').split('|')]


def guidance_blocks(path):
    tpl = open(path, encoding='utf8').read().splitlines()
    found = {}
    for i in range(len(tpl) - 1):
        if re.match(r'^[-~=]{3,}\s*$', tpl[i + 1]) and tpl[i].strip() and not tpl[i].startswith('..'):
            j = i + 2
            while j < len(tpl) and not tpl[j].strip():
                j += 1
            if j < len(tpl) and tpl[j].strip() == '..':
                k = j + 1
                while k < len(tpl) and (not tpl[k].strip() or tpl[k].startswith('   ')):
                    k += 1
                block = tpl[j:k]
                while block and not block[-1].strip():
                    block.pop()
                found[norm(tpl[i])] = block
    return found


def list_table(rows, widths, header):
    out = ['.. list-table::', f'   :header-rows: {1 if header else 0}', f'   :widths: {widths}', '']
    for r in rows:
        for n, c in enumerate(cells(r)):
            out.append(('   * - ' if n == 0 else '     - ') + c)
        out.append('')
    return out


def convert(md_text, guidance):
    lines = [l.rstrip() for l in md_text.splitlines()]
    meta = {}
    out = ['.. raw:: latex', '', '   \\pagestyle{plain}', '   \\thispagestyle{plain}', '', '.. _wg-charter:', '']
    i, section = 0, None
    while i < len(lines):
        l = lines[i]
        if l.startswith('# '):
            t = l[2:].strip()
            m = re.match(r'^FG-TIDA\s+(WG\d+):\s+(.+?)\s+\(([^()]+)\)$', t)
            if not m:
                sys.exit(f'charter.md: title must look like "# FG-TIDA WG1: <Name> (<ACRONYM>)", found: {t}')
            meta.update(wg=m.group(1), name=m.group(2), acronym=m.group(3))
            out += [t, '=' * len(t), '']
            i += 1
            continue
        m = re.match(r'^(#{2,3})\s+(.*)$', l)
        if m:
            level, t = m.groups()
            t = t.replace('\\.', '.').strip()
            section = norm(t)
            out += [t, ('-' if level == '##' else '~') * len(t), '']
            out += guidance.get(section, []) + ([''] if section in guidance else [])
            i += 1
            continue
        if l.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                if not re.match(r'^\|[\s|:-]*\|?\s*$', lines[i]):
                    rows.append(lines[i])
                i += 1
            if section == 'charter information':
                rows = [r for r in rows if any(cells(r))]
                for r in rows:
                    meta[cells(r)[0].lower()] = cells(r)[1]
                rows = ['|**' + cells(r)[0] + '**|' + cells(r)[1] + '|' for r in rows]
                out += list_table(rows, WIDTHS[section], False)
            else:
                out += list_table(rows, WIDTHS.get(section, '50 50'), True)
            continue
        if l.startswith('* '):
            while i < len(lines) and (lines[i].startswith('* ') or lines[i].startswith('  ')):
                out.append(lines[i])
                if i + 1 < len(lines) and lines[i + 1].startswith('* '):
                    out.append('')
                i += 1
            out.append('')
            continue
        if not l.strip():
            if out and out[-1] != '':
                out.append('')
            i += 1
            continue
        out.append(l)
        i += 1
    for key in ('acronym', 'charter version', 'status'):
        if key not in meta:
            sys.exit(f'charter.md: missing "{key}" (title line or Charter Information table)')
    rst = re.sub(r'\n{3,}', '\n\n', '\n'.join(out).rstrip() + '\n')
    status = meta['status'].split(',')[0].strip()
    conf = {
        'project': meta['acronym'],
        'release': meta['charter version'],
        'html_title': f"{meta['acronym']} Charter",
        'cover_title': f"{meta['wg']}: {meta['name']}",
        'cover_subject': meta['acronym'],
        'cover_subtitle': f"Charter version {meta['charter version']}, {status}",
    }
    return rst, conf


def main(argv):
    args = [a for a in argv if not a.startswith('--')]
    template = None
    if '--template' in argv:
        template = argv[argv.index('--template') + 1]
        args.remove(template)
    if len(args) != 2:
        sys.exit(__doc__)
    md_path, out_path = args
    guidance = guidance_blocks(template) if template else {}
    rst, conf = convert(open(md_path, encoding='utf8').read(), guidance)
    with open(out_path, 'w', encoding='utf8') as f:
        f.write(rst)
    meta_path = os.path.join(os.path.dirname(out_path) or '.', 'charter-meta.json')
    with open(meta_path, 'w', encoding='utf8') as f:
        json.dump(conf, f, indent=2, ensure_ascii=False)
        f.write('\n')
    print(f'{md_path} -> {out_path} ({len(rst.splitlines())} lines) and {meta_path}: '
          f"{conf['project']} {conf['release']}, {conf['cover_subtitle']}")


if __name__ == '__main__':
    main(sys.argv[1:])
