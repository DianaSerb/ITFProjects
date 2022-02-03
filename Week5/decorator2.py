from Week5.utils import my_unit_test


@my_unit_test
def test1(a):
    assert sum([1, 12], a) == 15


test1(2)

my_unit_test(test1)(2)
