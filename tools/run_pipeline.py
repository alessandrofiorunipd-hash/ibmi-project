import subprocess

def run(cmd):
    print(f"\n>> {cmd}")
    result = subprocess.call(cmd, shell=True)
    return result

print("IBM i DEVOPS PIPELINE START\n")

# 1. VALIDATE
if run("python tools/validator/validator.py") != 0:
    print("❌ Validation failed")
    exit(1)

# 2. AUTO FIX
run("python tools/autofix/autofix.py")

# 3. VALIDATE AGAIN
if run("python tools/validator/validator.py") != 0:
    print("❌ Still invalid after fix")
    exit(1)

# 4. BUILD
run("python tools/build/build.py")

# 5. DEPLOY
run("python tools/deploy/deploy.py")

# 6. FINAL CHECK
print("\n✅ PIPELINE COMPLETE")