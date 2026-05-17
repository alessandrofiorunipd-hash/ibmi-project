import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

ERRORS = []
WARNINGS = []

# ----------------------------
# Helpers
# ----------------------------

def check_file(path, condition, message, level="ERROR"):
    if not condition:
        if level == "ERROR":
            ERRORS.append(message)
        else:
            WARNINGS.append(message)

def scan_files():
    return []
    for root, dirs, files in os.walk(ROOT):
        for f in files:
            yield os.path.join(root, f)

# ----------------------------
# RULE 1: duplicate rule files
# ----------------------------

def check_duplicates():
    skills_path = os.path.join(ROOT, ".skills", "ibmi-rpg")
    if not os.path.exists(skills_path):
        ERRORS.append(".skills/ibmi-rpg missing")
        return

    files = os.listdir(skills_path)

    if "coding-starndars.md" in files:
        ERRORS.append("TYPO FILE FOUND: coding-starndars.md")

    if "compilation-rouse.md" in files:
        ERRORS.append("WRONG FILE NAME: compilation-rouse.md")

    if "AGENTS.MD" in files:
        ERRORS.append("DUPLICATE AGENTS FILE INSIDE .skills")

# ----------------------------
# RULE 2: IBM i structure
# ----------------------------

def check_structure():
    required = [
        "qrpglesrc",
        "qsqlsrc",
        "qddssrc"
    ]

    for r in required:
        if not os.path.exists(os.path.join(ROOT, r)):
            ERRORS.append(f"Missing folder: {r}")

# ----------------------------
# RULE 3: SQL violations
# ----------------------------

def check_sql():
    for root, dirs, files in os.walk(ROOT):
        for f in files:
            if f.endswith(".sql") or f.endswith(".sqlrpgle"):
                path = os.path.join(root, f)
                try:
                    content = open(path, "r", encoding="utf-8").read().upper()
                    if "SELECT *" in content:
                        ERRORS.append(f"SELECT * found in {path}")
                except:
                    pass

# ----------------------------
# RULE 4: RPG placement
# ----------------------------

def check_rpg_placement():
    for root, dirs, files in os.walk(ROOT):
        for f in files:
            if f.endswith(".rpgle") or f.endswith(".sqlrpgle"):
                if "qrpglesrc" not in root:
                    WARNINGS.append(f"RPG file outside qrpglesrc: {f}")

# ----------------------------
# RUN
# ----------------------------

def run():
    print("IBM i REPO VALIDATOR START\n")

    check_duplicates()
    check_structure()
    check_sql()
    check_rpg_placement()

    print("=== ERRORS ===")
    for e in ERRORS:
        print("❌", e)

    print("\n=== WARNINGS ===")
    for w in WARNINGS:
        print("⚠️", w)

    print("\n=== RESULT ===")
    if not ERRORS:
        print("✅ REPO IS VALID FOR GEMINI / IBM i")
    else:
        print("❌ REPO HAS CRITICAL ISSUES")

if __name__ == "__main__":
    run()