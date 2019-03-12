def assert_func(x, y):
    assert x < y


def pointless_func(x, y):
    assert_func(x * 20, y - 3)


pointless_func(1, 2)
