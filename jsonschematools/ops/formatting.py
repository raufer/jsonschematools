import json
from string import Formatter


def format_jsonlines(data: list[dict]) -> str:
    """Format a row of an item"""
    return "\n".join([json.dumps(x) for x in data])


def format_variables(string: str) -> list[str]:
    """Extracts the formatting variables from a string"""
    names = [
        fn for _, fn, _, _ in Formatter().parse(string) 
        if fn is not None
    ]
    return names
