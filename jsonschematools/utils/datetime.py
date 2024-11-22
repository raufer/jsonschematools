import dateparser
from datetime import date


def parse_date(x: date | str) -> date | str:
    if isinstance(x, date):
        return x
    elif isinstance(x, str):
        dt = dateparser.parse(x)
        if dt is not None:
            return dt.date()
        else:
            return x
    else:
        return str(x)