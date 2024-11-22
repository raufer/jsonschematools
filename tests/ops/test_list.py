from src.ops.lists import chunked, non_duplicate_indices, repeated_elements
from src.ops.lists import dedup


def test_chunked():
    xs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(chunked(xs, 3)) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert list(chunked([], 2)) == []


def test_dedup():
    assert dedup([]) == []
    assert dedup([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert dedup(["208", "210", "217", "217"]) == ["208", "210", "217"]
    
def test_non_duplicate_indices():
    assert non_duplicate_indices([]) == []
    assert non_duplicate_indices([1, 2, 3]) == [0, 1, 2]
    assert non_duplicate_indices(["208", "210", "217", "217"]) == [0, 1, 2]


def test_repeated_elements():
    assert repeated_elements([]) == []
    assert repeated_elements([(1, 1), (2, 2)]) == []
    assert repeated_elements([(1, 1), (2, 2), (3, 2)]) == [(2, 2), (3, 2)]
    assert repeated_elements([(1, 1, 1), (2, 2, 2), (3, 3, 2), (3, 2, 3)]) == [(3, 3, 2), (3, 2, 3), (2, 2, 2)]
    assert repeated_elements([(1,1), (2,2), (2, 10), (3, 3), (4, 10), (5, 9), (6, 10)]) == [(2, 2), (2, 10), (4, 10), (6, 10)]
