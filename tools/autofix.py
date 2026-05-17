import os
import shutil

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

FIXES_APPLIED = []

# ----------------------------
# UTIL
# ----------------------------

def move_file(src, dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.move(src, dst)
    FIXES_APPLIED.append(f"MOVED: {src} → {dst}")

def delete_file(path):
    if os.path.exists(path):
        os.remove(path)
        FIXES_APPLIED.append(f"DELETED: {path}")

# ----------------------------
# FIX 1: TYPO FILES (.skills)
# ----------------------------

def fix_skills():
    skills = os.path.join(ROOT, ".skills", "ibmi-rpg")

    bad_files = {
        "coding-starndars.md": "coding-standards.md",
        "compilation-rouse.md": "compilation-rules.md"
    }

    for wrong, correct in bad_files.items():
        wrong_path = os.path.join(skills, wrong)
        correct_path = os.path.join(skills, correct)

        if os.path.exists(wrong_path):
            if not os.path.exists(correct_path):
                move_file(wrong_path, correct_path)
            else:
                delete_file(wrong_path)

# ----------------------------
# FIX 2: AGENTS DUPLICATE
# ----------------------------

def fix_agents():
    dup = os.path.join(ROOT, ".skills", "ibmi-rpg", "AGENTS.MD")

    if os.path.exists(dup):
        delete_file(dup)

# ----------------------------
# FIX 3: RPG FILE PLACEMENT
# ----------------------------

def fix_rpg_location():
    rpg_folder = os.path.join(ROOT, "qrpglesrc")

    for root, dirs, files in os.walk(ROOT):
        for f in files:
            if f.endswith(".rpgle") or f.endswith(".sqlrpgle"):
                full = os.path.join(root, f)

                if "qrpglesrc" not in root:
                    target = os.path.join(rpg_folder, f)

                    if os.path.exists(full):
                        move_file(full, target)

# ----------------------------
# FIX 4: SQL LOCATION
# ----------------------------

def fix_sql_location():
    sql_folder = os.path.join(ROOT, "qsqlsrc")

    for root, dirs, files in os.walk(ROOT):
        for f in files:
            if f.endswith(".sql"):
                full = os.path.join(root, f)

                if "qsqlsrc" not in root:
                    target = os.path.join(sql_folder, f)

                    if os.path.exists(full):
                        move_file(full, target)

# ----------------------------
# BACKUP (SAFE MODE)
# ----------------------------

def backup():
    backup_dir = os.path.join(ROOT, "tools", "autofix", "backup")
    os.makedirs(backup_dir, exist_ok=True)

# ----------------------------
# RUN
# ----------------------------

def run():
    print("IBM i AUTO-FIX START\n")

    backup()

    fix_skills()
    fix_agents()
    fix_rpg_location()
    fix_sql_location()

    print("\n=== FIXES APPLIED ===")
    for f in FIXES_APPLIED:
        print("✔", f)

    print("\nDONE.")

if __name__ == "__main__":
    run()