import pytest

from src.ops.functions import signature_args


def test_signature_args():
    def f(x):
        return x + 1

    with pytest.raises(Exception) as e:
        signature_args(f)

    def f(x: int, y):
        return x + y

    with pytest.raises(Exception) as e:
        signature_args(f)

    def f(x: int):
        return x + 1

    assert signature_args(f) == {"x": int}

    def f(x: int, y: int):
        return x + y

    assert signature_args(f) == {"x": int, "y": int}
