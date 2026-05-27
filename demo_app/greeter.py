def greet(name: str) -> str:
    cleaned = (name or "").strip()
    return f"Hello, {cleaned}!"
