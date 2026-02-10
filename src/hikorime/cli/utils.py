from datetime import date, time


def parse_date(valor: str) -> date:
    return date.fromisoformat(valor)


def parse_time(valor: str) -> time:
    return time.fromisoformat(valor)
