import pytest
from src.ops.string import match_strings_pairs, match_strings_pairs_indices, most_similar_string


def test_match_strings_pairs():

    xs = []
    ys = []
    assert match_strings_pairs(xs, ys) == []

    xs = []
    ys = ["a"]
    assert match_strings_pairs(xs, ys) == []

    xs = ["a"]
    ys = []
    assert match_strings_pairs(xs, ys) == []

    xs = ["a"]
    ys = ["b"]
    assert match_strings_pairs(xs, ys) == [("a", "b")]

    xs = ["seat"]
    ys = ["door", "seated"]
    assert match_strings_pairs(xs, ys) == [("seat", "seated")]

    xs = ["arm chair 20x10", "laptop M1 2021"]
    ys = ["laptop", "book shelf", "arm chair", "arm chair 20x10"]
    assert match_strings_pairs(xs, ys) == [
        ("arm chair 20x10", "arm chair 20x10"),
        ("laptop M1 2021", "laptop"),
    ]


def test_match_strings_pairs_indices():

    xs = []
    ys = []
    assert match_strings_pairs_indices(xs, ys) == []

    xs = []
    ys = ["a"]
    assert match_strings_pairs_indices(xs, ys) == []

    xs = ["a"]
    ys = []
    assert match_strings_pairs_indices(xs, ys) == []

    xs = ["a"]
    ys = ["b"]
    assert match_strings_pairs_indices(xs, ys) == [(0, 0)]

    xs = ["seat"]
    ys = ["door", "seated"]
    assert match_strings_pairs_indices(xs, ys) == [(0, 1)]

    xs = ["arm chair 20x10", "laptop M1 2021"]
    ys = ["laptop", "book shelf", "arm chair", "arm chair 20x10"]
    assert match_strings_pairs_indices(xs, ys) == [(0, 3), (1, 0)]


def test_most_similar_string():
    assert most_similar_string("arm chair", ["arm chair", "door", "seated"]) == "arm chair"
    assert most_similar_string("arm chair", ["door", "seated", "chair"]) == "chair"
    assert most_similar_string("arm chair", ["XX"]) == "XX"
    with pytest.raises(ValueError):
        most_similar_string("arm chair", [])
