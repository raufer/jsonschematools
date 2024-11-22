from itertools import chain, islice, groupby
from typing import Callable, Iterable, Iterator, Sequence, TypeVar, List
from operator import itemgetter

from jsonschematools.ops.functions import identity


T = TypeVar("T")
K = TypeVar("K")


def deduplicate_list(items: list[T], key: Callable[[T], K]) -> list[T]:
    unique_values: dict[K, T] = {}
    for item in items:
        k = key(item)
        if k not in unique_values:
            unique_values[k] = item
    return list(unique_values.values())


def dedup(seq, f: Callable = identity):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (f(x) in seen or seen_add(f(x)))]


def non_duplicate_indices(seq):
    seen = set()
    seen_add = seen.add
    return [i for i, x in enumerate(seq) if not (x in seen or seen_add(x))]


def flatten(it: Iterator) -> Iterator:
    """
    Flattens a iterator one level
    """
    return chain.from_iterable(it)


def chunked(it: Iterator, n: int) -> Iterator[Iterator]:
    """
    Split a generator in chunks of `n` size
    """
    it = iter(it)
    while True:
        chunk = list(islice(it, n))
        if not chunk:
            break
        yield chunk


def repeated_elements(xs: List[Iterable]) -> List:
    """
    Returns the elements that are repeated in the sequences
    """
    if not xs:
        return []
    
    n = len(xs[0])

    repeated = []

    for i in range(n):
        op = itemgetter(i)
        groups = {k: list(v) for k, v in groupby(sorted(xs, key=op), key=op)}
        repeated.extend(sum([v for k, v in groups.items() if len(v) > 1], []))
        
    repeated = dedup(repeated, f=str)
    return repeated
        

