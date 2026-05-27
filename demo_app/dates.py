def format_report_anchor(report_date: str) -> str:
    return (report_date or "").strip() or "1970-01-01"
