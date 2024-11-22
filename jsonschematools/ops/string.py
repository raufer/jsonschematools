import re
import difflib
from typing import Iterable
from difflib import SequenceMatcher
from heapq import nlargest as _nlargest


def elipsis_trim(x: str, n: int = 100) -> str:
    if len(x) > n:
        return x[:n] + "..."
    return x


def get_close_matches_indexes(word, possibilities, n=3, cutoff=0.6):
    """Use SequenceMatcher to return a list of the indexes of the best 
    "good enough" matches. word is a sequence for which close matches 
    are desired (typically a string).
    possibilities is a list of sequences against which to match word
    (typically a list of strings).
    Optional arg n (default 3) is the maximum number of close matches to
    return.  n must be > 0.
    Optional arg cutoff (default 0.6) is a float in [0, 1].  Possibilities
    that don't score at least that similar to word are ignored.
    """

    if not n > 0:
        raise ValueError("n must be > 0: %r" % (n,))
    if not 0.0 <= cutoff <= 1.0:
        raise ValueError("cutoff must be in [0.0, 1.0]: %r" % (cutoff,))
    result = []
    s = SequenceMatcher()
    s.set_seq2(word)
    for idx, x in enumerate(possibilities):
        s.set_seq1(x)
        if (
            s.real_quick_ratio() >= cutoff
            and s.quick_ratio() >= cutoff
            and s.ratio() >= cutoff
        ):
            result.append((s.ratio(), idx))

    # Move the best scorers to head of list
    result = _nlargest(n, result)

    # Strip scores for the best n matches
    return [x for score, x in result]


def match_strings_pairs_indices(xs: list[str], ys: list[str]) -> list[tuple[int, int]]:
    """Matches string pairs from two lists by string similarity
    
    That the output length is the length of the first list
    so if the second list is longer, the extra elements are ignored.

    Returns indices instead of the strings.
    """
    if not ys:
        return []

    pairs = []
    seen = set()

    for i, x in enumerate(xs):
        indices = get_close_matches_indexes(x, ys, n=len(ys), cutoff=0.0)
        match = next((i for i in indices if i not in seen), None)
        # all of ys have been used
        if match is None:
            break
        pairs.append((i, match))

    return pairs


def match_strings_pairs(xs: list[str], ys: list[str]) -> list[tuple[str, str]]:
    """Matches string pairs from two lists by string similarity
    
    That the output length is the length of the first list
    so if the second list is longer, the extra elements are ignored.
    """
    indices = match_strings_pairs_indices(xs, ys)
    return [(xs[i], ys[j]) for i, j in indices]


def only_alpha_numeric(x: str) -> str:
    return re.sub('[^A-Za-z0-9]+', '', x)


def only_alpha_numeric_and_space(x: str) -> str:
    return re.sub('[^A-Za-z0-9 ]+', '', x)


def capitalize_snake_case(x: str) -> str:
    return x.replace("_", " ").title().strip()


def int_to_capital_letter(x: int) -> str:
    """Returns a capital letter from an integer"""
    x = x % 26
    return chr(x + ord('A'))


def most_similar_string(x: str, possibilities: Iterable[str]) -> str:
    if not possibilities:
        raise ValueError("No possibilities to compare to")
    return difflib.get_close_matches(x, possibilities, n=1, cutoff=0)[0]
