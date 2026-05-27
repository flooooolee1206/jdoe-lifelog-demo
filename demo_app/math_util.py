def safe_div(a: float, b: float) -> float:
    if b == 0:
        return 0
    return a / b
