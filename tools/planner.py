def plan(flags):
    plan = []

    if flags["uses_chain"]:
        plan.append("Replace CHAIN with SQL SELECT INTO")

    if flags["uses_read"]:
        plan.append("Replace READ loop with cursor or SQL FETCH")

    if flags["uses_indicator"]:
        plan.append("Remove indicators, use structured logic")

    if flags["uses_move"]:
        plan.append("Replace MOVE with assignment")

    return plan