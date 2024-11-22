from src.ops.dicts import f_map
from src.ops.dicts import count_leafs


def test_f_map():
    xs = []
    f = lambda x: x + 1
    assert f_map(xs, f) == []

    xs = [1, 2]
    f = lambda x: x + 1
    assert f_map(xs, f) == [2, 3]

    xs = {"a": 1, "b": 2}
    f = lambda x: x + 1
    assert f_map(xs, f) == {"a": 2, "b": 3}

    xs = {"a": 1, "b": [2, 3]}
    f = lambda x: x + 1
    assert f_map(xs, f) == {"a": 2, "b": [3, 4]}

    xs = {"a": 1, "b": [2, 3], "c": {"d": 4, "e": 5}}
    f = lambda x: x + 1
    assert f_map(xs, f) == {"a": 2, "b": [3, 4], "c": {"d": 5, "e": 6}}

    
def test_count_leafs():

    assert count_leafs({}) == 0
    assert count_leafs({"a": 1}) == 1
    assert count_leafs({"a": 1, "b": 2}) == 2
    assert count_leafs({"a": 1, "b": 2, "c": 3}) == 3
    assert count_leafs({"a": 1, "b": {"c": 2}}) == 2
    assert count_leafs({"a": 1, "b": {"c": 2}, "d": 3}) == 3
    assert count_leafs({"a": 1, "b": {"c": 2}, "d": {"e": 3}}) == 3
    assert count_leafs({"a": 1, "b": {"c": 2}, "d": {"e": 3}, "f": 4, "g": {"h": [1, 2, 3, 4]}}) == 8
    assert count_leafs({"a": 1, "b": [1, 2]}) == 3
    assert count_leafs({"a": 1, "b": {"c": 2}, "d": {"e": 3}, "f": 4, "g": {"h": [1, 2, 3, {"a": {"b": 2, "c": 3}}]}}) == 9
    

