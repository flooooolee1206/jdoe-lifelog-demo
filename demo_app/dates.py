from datetime import datetime


def format_report_anchor(report_date: datetime) -> str:
    return report_date.strftime("%Y-%m-%d")
