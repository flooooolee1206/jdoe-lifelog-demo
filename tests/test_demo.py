import pytest
from datetime import datetime
from demo_app.greeter import greet
from demo_app.math_util import safe_div
from demo_app.dates import format_report_anchor


def test_greet_strips():
    assert greet("  Ada  ") == "Hello, Ada!"


def test_safe_div_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        safe_div(1, 0)


def test_safe_div_normal():
    assert safe_div(10, 2) == 5.0


def test_format_report_anchor_iso():
    assert format_report_anchor(datetime(2023, 1, 15)) == "2023-01-15"
