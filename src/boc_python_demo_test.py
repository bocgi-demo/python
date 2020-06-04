from boc_python_demo import my_sum


def test_my_sum():
    assert my_sum(1) == 1
    assert my_sum(2) == 2
    assert my_sum(3) == 3
    assert my_sum(4) == 5
    assert my_sum(5) == 8
    assert my_sum(6) == 13

