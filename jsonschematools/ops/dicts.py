import operator

from functools import reduce
from collections.abc import Mapping
from typing import Callable, Any


def f_map(d: dict | list | Any, f: Callable) -> dict | list:
    """Maps a function over a dictionary or list recursively"""

    if isinstance(d, Mapping):
        return {k: f_map(v, f) for k, v in d.items()}

    elif isinstance(d, list):
        return [f_map(v, f) for v in d]

    else:
        return f(d)


def count_leafs(d: dict) -> int:
    """Counts the number of leafs in a dictionary
    A leaf is either a primitive value or a list of primitive values
    in case of a list, we add the length of the list to the count
    """
    def loop(d, acc=0):
        
        if isinstance(d, Mapping):
            return acc + sum(loop(v) for v in d.values())
        elif isinstance(d, list):
            return acc + sum(loop(v) for v in d)
        else:
            return acc + 1
    return loop(d)
    


def safe_get(d: dict, keys: list[str]) -> Any:
    """Safely gets a value from a nested dictionary"""
    # try:
    #     return reduce(operator.getitem, keys, d)
    # except KeyError:
    #     return None
    for key in keys:
        if key in d:
            d = d[key]
        else:
            return None
    return d
