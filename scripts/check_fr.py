#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contrôle mécanique d'une traduction WordPress EN → FR.

Vérifie typographie, termes interdits, variables gettext, balises HTML et
présence des termes du glossaire officiel Polyglots fr_FR.

Usage :
  python check_fr.py --source en.txt --target fr.txt [--mode polyglots|admin-client] [--json]
  python check_fr.py --po fichier.po [--mode ...] [--json]
  python check_fr.py --source en.txt --target fr.txt --project-glossary glossaire-projet.md

Fichiers .txt : une chaîne par ligne, source et cible alignées.
Code de sortie : 1 s'il reste au moins un défaut bloquant, 0 sinon.
"""
import argparse
import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_GLOSSARY = os.path.join(HERE, "..", "references", "glossaire.md")

FORBIDDEN = [
    (r"\bplug-?ins?\b", "« plugin » interdit, utiliser « extension »"),
    (r"\bgreffons?\b", "« greffon » interdit, utiliser « extension »"),
    (r"\b(tu|te|toi|ton|ta|tes)\b", "tutoiement détecté, vouvoyer"),
    (r"\b(es-tu|as-tu|veux-tu|peux-tu|souhaites-tu)\b", "tutoiement détecté, vouvoyer"),
    (r"\bsauvegard", "« sauvegarder » : le glossaire attend « enregistrer » pour save"),
    (r"\buploade", "« uploader » interdit, utiliser « téléverser »"),
    (r"\bmail\b", "« mail » : le glossaire attend « e-mail »"),
]

PLACEHOLDER_RE = re.compile(r"%(?:\d+\$)?[sdfu]|%%|\{\{?\s*[\w.]+\s*\}?\}")
HTML_TAG_RE = re.compile(r"</?[a-zA-Z][^>]*>")
PUNCT_NEEDS_NBSP_RE = re.compile(r"(?<![  ])[:;?!»%]")


def strip_accents(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def load_pairs_txt(src_path, tgt_path):
    with open(src_path, encoding="utf-8") as f:
        src = f.read().splitlines()
    with open(tgt_path, encoding="utf-8") as f:
        tgt = f.read().splitlines()
    if len(src) != len(tgt):
        print(f"ERREUR : {len(src)} lignes source contre {len(tgt)} lignes cible, fichiers non alignés.", file=sys.stderr)
        sys.exit(2)
    return [(i + 1, s, t) for i, (s, t) in enumerate(zip(src, tgt))]


def unquote_po(s):
    s = s.strip()
    if s.startswith('"') and s.endswith('"'):
        s = s[1:-1]
    return s.replace('\\"', '"').replace("\\n", "\n").replace("\\t", "\t").replace("\\\\", "\\")


def load_pairs_po(po_path):
    pairs = []
    with open(po_path, encoding="utf-8") as f:
        lines = f.read().splitlines()
    msgid, msgstr, current, start = None, None, None, 0
    for idx, raw in enumerate(lines, 1):
        line = raw.strip()
        if line.startswith("msgid "):
            if msgid is not None and msgstr is not None and msgid != "":
                pairs.append((start, msgid, msgstr))
            msgid, msgstr, current, start = unquote_po(line[6:]), None, "id", idx
        elif line.startswith("msgstr"):
            rest = line.split(" ", 1)[1] if " " in line else '""'
            msgstr, current = unquote_po(rest), "str"
        elif line.startswith('"') and current:
            if current == "id":
                msgid += unquote_po(line)
            else:
                msgstr += unquote_po(line)
        elif line == "" or line.startswith("#"):
            current = None
    if msgid is not None and msgstr is not None and msgid != "":
        pairs.append((start, msgid, msgstr))
    return pairs


def load_glossary(path):
    """Retourne {en_lower: [(fr, nature, notes), ...]} à partir des tableaux markdown."""
    gl = {}
    if not path or not os.path.exists(path):
        return gl
    # Accepte les tableaux à 4 colonnes (glossaire officiel : Anglais | Français | Nature | Notes)
    # et à 3 colonnes (glossaire projet §9 : Anglais | Français retenu | Contexte / Note).
    with open(path, encoding="utf-8") as f:
        for line in f:
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 2:
                continue
            en = cells[0].strip("`").strip()
            fr = cells[1].strip("`").strip()
            if not en or not fr or en.lower() in ("anglais", "terme", "english") or set(en) <= set("-: "):
                continue
            nature = cells[2] if len(cells) == 4 else ""
            notes = cells[3] if len(cells) == 4 else (cells[2] if len(cells) == 3 else "")
            gl.setdefault(en.lower(), []).append((fr, nature, notes))
    return gl


def fr_stem(term):
    """Radicaux grossiers pour tolérer les flexions (enregistrer/enregistrez, étiquette/étiquettes)."""
    t = strip_accents(term.lower())
    t = re.sub(r"[^a-z0-9 ]", " ", t).strip()
    stop = ("les", "des", "une", "aux", "sur", "dans", "the")
    words = [w for w in t.split() if len(w) > 2 and w not in stop]
    return [w[: max(4, len(w) - 2)] for w in words]


def term_in_source(en, src_norm):
    return re.search(r"(?<![a-z])" + re.escape(en) + r"s?(?![a-z])", src_norm) is not None


def check_pair(no, src, tgt, glossary, project_glossary, mode):
    out = []
    typo_sev = "bloquant" if mode == "polyglots" else "avertissement"

    def add(code, sev, msg):
        if any(f["code"] == code and f["message"] == msg for f in out):
            return
        out.append({"ligne": no, "code": code, "severite": sev, "source": src, "traduction": tgt, "message": msg})

    if tgt.strip() == "":
        add("vide", "bloquant", "traduction vide")
        return out

    # --- Typographie ---
    if "'" in tgt:
        add("apostrophe-droite", typo_sev, "apostrophe droite U+0027, utiliser l’apostrophe courbe U+2019")
    if "..." in tgt:
        add("points-suspension", typo_sev, "trois points ASCII, utiliser le caractère … U+2026")
    if re.search(r'"[^"]*"', HTML_TAG_RE.sub("", tgt)):
        add("guillemets-anglais", typo_sev, "guillemets anglais, utiliser « … » avec espaces insécables")
    probe = HTML_TAG_RE.sub("", tgt).replace("://", "")
    probe = re.sub(r"%(?:\d+\$)?[sdfu]|%%", "", probe)
    if PUNCT_NEEDS_NBSP_RE.search(probe):
        add("insecable-manquante", typo_sev, "espace insécable manquante avant : ; ? ! » ou %")
    if re.search(r"«(?![  ])", tgt):
        add("insecable-manquante", typo_sev, "espace insécable manquante après «")
    if re.search(r"\s[.,)\]]", tgt):
        add("espace-avant-ponctuation", typo_sev, "espace avant . , ) ou ]")
    if re.search(r"\b[A-Z][a-zé]+ [A-Z][a-zé]+", tgt) and "WordPress" not in tgt:
        add("majuscules-calque", "avertissement", "majuscules en cascade, calque possible de l’anglais (Title Case)")

    # --- Termes interdits ---
    for pattern, msg in FORBIDDEN:
        if re.search(pattern, tgt, re.IGNORECASE):
            add("terme-interdit", "bloquant", msg)

    # --- Variables gettext ---
    ps, pt = sorted(PLACEHOLDER_RE.findall(src)), sorted(PLACEHOLDER_RE.findall(tgt))
    if ps != pt:
        add("gettext", "bloquant", f"variables modifiées : source {ps} contre traduction {pt}")

    # --- Balises HTML ---
    hs, ht = HTML_TAG_RE.findall(src), HTML_TAG_RE.findall(tgt)
    if [h.lower() for h in hs] != [h.lower() for h in ht]:
        add("html", "bloquant", f"balises HTML modifiées : source {hs} contre traduction {ht}")

    # --- Glossaire officiel ---
    src_norm = " " + strip_accents(src.lower()) + " "
    tgt_norm = " " + strip_accents(tgt.lower()) + " "
    matched = [en for en in glossary if term_in_source(en, src_norm)]
    # ne garde que les termes les plus longs (« featured image » masque « featured », « settings » masque « setting »)
    matched = [en for en in matched if not any(other != en and en in other for other in matched)]
    for en in matched:
        entries = glossary[en]
        candidates = [fr for fr, _, _ in entries]
        if any(strip_accents(fr.lower()) == en for fr in candidates):
            continue  # terme conservé tel quel (slug, widget…)
        ok = any(fr_stem(fr) and all(s in tgt_norm for s in fr_stem(fr)) for fr in candidates)
        if not ok:
            add("glossaire", "bloquant", f"« {en} » présent en source, équivalent officiel absent : attendu « {' / '.join(candidates)} »")

    # --- Glossaire projet (dev client) ---
    for en, entries in project_glossary.items():
        if not term_in_source(en, src_norm):
            continue
        candidates = [fr for fr, _, _ in entries]
        ok = any(fr_stem(fr) and all(s in tgt_norm for s in fr_stem(fr)) for fr in candidates)
        if not ok:
            add("glossaire-projet", "bloquant", f"« {en} » : terme projet attendu « {' / '.join(candidates)} »")

    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", help="fichier EN, une chaîne par ligne")
    ap.add_argument("--target", help="fichier FR aligné")
    ap.add_argument("--po", help="fichier .po (msgid/msgstr)")
    ap.add_argument("--glossary", default=DEFAULT_GLOSSARY, help="glossaire officiel (markdown)")
    ap.add_argument("--project-glossary", help="glossaire projet client (markdown, même format de tableau)")
    ap.add_argument("--mode", choices=["polyglots", "admin-client"], default="polyglots")
    ap.add_argument("--json", action="store_true", help="sortie JSON")
    args = ap.parse_args()

    if args.po:
        pairs = load_pairs_po(args.po)
    elif args.source and args.target:
        pairs = load_pairs_txt(args.source, args.target)
    else:
        ap.error("fournir --po ou --source et --target")

    glossary = load_glossary(args.glossary)
    project_glossary = load_glossary(args.project_glossary) if args.project_glossary else {}

    findings = []
    for no, s, t in pairs:
        findings.extend(check_pair(no, s, t, glossary, project_glossary, args.mode))

    blocking = [f for f in findings if f["severite"] == "bloquant"]
    verdict = "NON CONFORME" if blocking else "CONFORME"
    if args.json:
        print(json.dumps({"mode": args.mode, "chaines": len(pairs), "defauts": findings,
                          "bloquants": len(blocking), "verdict": verdict}, ensure_ascii=False, indent=2))
    else:
        print(f"Mode : {args.mode} | Chaînes : {len(pairs)} | Glossaire : {len(glossary)} entrées")
        if not findings:
            print("Aucun défaut mécanique détecté.")
        for f in findings:
            print(f"L{f['ligne']:>4} [{f['severite']:^13}] {f['code']:<24} {f['message']}")
            print(f"      EN : {f['source']}")
            print(f"      FR : {f['traduction']}")
        print(f"\nVerdict mécanique : {verdict} ({len(blocking)} bloquant(s), {len(findings) - len(blocking)} avertissement(s))")
    sys.exit(1 if blocking else 0)


if __name__ == "__main__":
    main()
