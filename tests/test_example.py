from orbit.example import add_one


def test_add_positive():
    assert add_one(1) == 2


def test_add_negative():
    assert add_one(-2) == -1


def test_add_float():
    assert add_one(1.5) == 2.5


def test_fail():
    assert add_one(1) == 1
