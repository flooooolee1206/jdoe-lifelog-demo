from demo_app.greeter import greet
from demo_app.math_util import safe_div


def test_greet_strips():
    assert greet("  Ada  ") == "Hello, Ada!"


def test_safe_div_zero():
    assert safe_div(1, 0) == 0
