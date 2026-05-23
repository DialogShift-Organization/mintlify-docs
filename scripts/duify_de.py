#!/usr/bin/env python3
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Rule:
    pattern: re.Pattern[str]
    repl: str


def apply_rules(text: str, rules: list[Rule]) -> str:
    for r in rules:
        text = r.pattern.sub(r.repl, text)
    return text


def build_rules() -> list[Rule]:
    # The goal is to remove *formal address* (Sie-Form) in German support docs
    # and convert to consistent singular informal (du-Form).
    #
    # We intentionally focus on high-precision patterns common in support docs:
    # - Verb + "Sie" (imperative)
    # - Sentence starts with "Sie" + common user-action verbs/modals
    # - Polite pronouns: Ihnen, Ihr/Ihre/Ihren/Ihrem/Ihrer
    #
    # We do *not* blanket-replace every "Sie", because it can also mean "she/it"
    # at sentence start (e.g., "Sie nimmt ..."). Those are handled separately
    # by targeted rewrites after the codemod scan.
    rules: list[Rule] = []

    def r(pat: str, repl: str, flags: int = 0) -> None:
        rules.append(Rule(re.compile(pat, flags), repl))

    # Common imperative patterns: "<Verb> Sie" -> "<Verb (du)>"
    imperative_map: dict[str, str] = {
        "Aktivieren": "Aktiviere",
        "Deaktivieren": "Deaktiviere",
        "Öffnen": "Öffne",
        "Nutzen": "Nutze",
        "Klicken": "Klicke",
        "Wählen": "Wähle",
        "Geben": "Gib",
        "Fügen": "Füge",
        "Kopieren": "Kopiere",
        "Navigieren": "Navigiere",
        "Prüfen": "Prüfe",
        "Starten": "Starte",
        "Installieren": "Installiere",
        "Bestätigen": "Bestätige",
        "Senden": "Sende",
        "Kontaktieren": "Kontaktiere",
        "Teilen": "Teile",
        "Ersetzen": "Ersetze",
        "Speichern": "Speichere",
        "Definieren": "Definiere",
        "Planen": "Plane",
        "Stellen": "Stell",
        "Bitten": "Bitte",
        "Melden": "Melde",
        "Wenden": "Wende",
        "Überprüfen": "Überprüfe",
        "Behalten": "Behalte",
        "Schalten": "Schalte",
        "Richten": "Richte",
        "Verbinden": "Verbinde",
        "Vereinbaren": "Vereinbare",
        "Folgen": "Folge",
        "Gehen": "Geh",
        "Tippen": "Tippe",
        "Informieren": "Informiere",
        "Sichern": "Sichere",
        "Warten": "Warte",
        "Ändern": "Ändere",
        "Wechseln": "Wechsle",
        "Kontrollieren": "Kontrolliere",
        "Filtern": "Filtere",
        "Suchen": "Suche",
        "Erstellen": "Erstelle",
        "Schreiben": "Schreibe",
        "Ignorieren": "Ignoriere",
    }
    for formal, informal in imperative_map.items():
        # Examples:
        # "Klicken Sie ..." -> "Klicke ..."
        # "Melden Sie sich ..." -> "Melde dich ..."
        r(rf"\b{formal}\s+Sie\b", informal)

    # Reflexive constructions commonly used with Sie.
    # "Melden Sie sich" -> "Melde dich"
    r(r"\bMelde\s+sich\b", "Melde dich")
    r(r"\bMelden\s+Sie\s+sich\b", "Melde dich")
    r(r"\bLoggen\s+Sie\s+sich\b", "Logge dich")
    r(r"\bRegistrieren\s+Sie\s+sich\b", "Registriere dich")

    # "Stellen Sie sicher" -> "Stell sicher"
    r(r"\bStellen\s+Sie\s+sicher\b", "Stell sicher")

    # Sentence-start patterns: "Sie <verb>" -> "Du <verb>"
    # Limit to common user-action/modals to avoid "Sie nimmt ..." (Phone AI etc).
    start_verbs = [
        "müssen",
        "können",
        "sollten",
        "möchten",
        "brauch(en|st)",
        "benötigen",
        "finden",
        "sehen",
        "erhalten",
        "bekommen",
        "verwenden",
        "nutzen",
        "hast",
        "habe(n)?",
        "bist",
        "sind",
        "wirst",
        "werden",
        "zahl(en|st)",
        "erfahr(en|st)",
        "bearbeit(en|est|st)",
        "konfigurier(en|st)",
        "verwalt(en|est|st)",
        "integrier(en|st)",
        "verfolg(en|st)",
        "prüfen",
        "kopieren",
        "wählen",
        "öffnen",
        "klicken",
        "geben",
        "fügen",
        "starten",
        "installieren",
        "kontaktieren",
        "teilen",
        "ersetzen",
        "speichern",
        "definieren",
        "planen",
        "navigieren",
        "überprüfen",
    ]
    start_verbs_re = "|".join(start_verbs)
    r(rf"(^|\n)\s*Sie\s+({start_verbs_re})\b", r"\1Du \2", flags=re.IGNORECASE)

    # Polite pronouns -> du-form pronouns
    r(r"\bIhnen\b", "dir")
    r(r"\bIhres\b", "deines")
    r(r"\bIhrem\b", "deinem")
    r(r"\bIhren\b", "deinen")
    r(r"\bIhrer\b", "deiner")
    r(r"\bIhre\b", "deine")
    r(r"\bIhr\b", "dein")

    # Lowercase variants that sometimes appear in examples
    r(r"\bIhnen\b", "dir")

    # Clean up: "Du benötigen" etc. Fix a few common conjugations.
    r(r"\bDu benötigen\b", "Du benötigst")
    r(r"\bDu brauchen\b", "Du brauchst")
    r(r"\bDu müssen\b", "Du musst")
    r(r"\bDu können\b", "Du kannst")
    r(r"\bDu sollten\b", "Du solltest")
    r(r"\bDu erhalten\b", "Du erhältst")
    r(r"\bDu finden\b", "Du findest")
    r(r"\bDu sehen\b", "Du siehst")
    r(r"\bDu werden\b", "Du wirst")
    r(r"\bDu sind\b", "Du bist")
    r(r"\bDu erfahren\b", "Du erfährst")

    # Common "wenden Sie sich an" -> "wende dich an"
    r(r"\bwenden\s+Sie\s+sich\s+an\b", "wende dich an", flags=re.IGNORECASE)
    r(r"\bWenden\s+Sie\s+sich\s+an\b", "Wende dich an")

    # Fix mixed-case "Du"/"du" after newline bullets sometimes.
    r(r"(^|\n)\s*du\s+", r"\1Du ", flags=re.IGNORECASE)

    return rules


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    de_dir = repo_root / "de"
    if not de_dir.exists():
        raise SystemExit(f"Expected directory not found: {de_dir}")

    rules = build_rules()
    changed_files: list[Path] = []

    for path in sorted(de_dir.rglob("*.mdx")):
        original = path.read_text(encoding="utf-8")
        updated = apply_rules(original, rules)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed_files.append(path)

    print(f"Updated {len(changed_files)} files.")
    for p in changed_files:
        print(f"- {p.relative_to(repo_root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

