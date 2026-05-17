def analyze(code: str):
    flags = {
        "uses_chain": "CHAIN" in code.upper(),
        "uses_read": "READ" in code.upper(),
        "uses_indicator": "IF" in code.upper() and "*IN" in code.upper(),
        "uses_move": "MOVE" in code.upper(),
        "has_sql": "EXEC SQL" in code.upper()
    }

    return flags