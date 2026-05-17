from analyzer import analyze
from planner import plan
from transformer import transform
from validator import validate

def run(code):
    print("ANALYZING...")
    flags = analyze(code)

    print("PLANNING...")
    steps = plan(flags)

    print("TRANSFORMING...")
    new_code = transform(code)

    print("VALIDATING...")
    errors = validate(new_code)

    return {
        "plan": steps,
        "output": new_code,
        "errors": errors
    }