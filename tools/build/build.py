import subprocess
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

print("BUILD START")

# RPG compile
subprocess.call(
    "system CRTBNDRPG PGM(MYLIB/CUSTMAIN) SRCFILE(MYLIB/QRPGLESRC)",
    shell=True
)

# SQLRPGLE compile
subprocess.call(
    "system CRTSQLRPGI OBJ(MYLIB/CUSREPO) SRCFILE(MYLIB/QRPGLESRC)",
    shell=True
)

print("BUILD DONE")