# from main import present_value
from main import add


def test_add():
    assert add(2, 2) == 4
    assert add(1, 2) == 3
    assert add(1, 1) == 2


# def test_present_value():
#     "Testing Out a fucntion"
#     assert present_value({2024: 10000}, 0.00) == 10000
#     assert present_value({}, 0.00) == "Current data structure has has no Cash Flow Info"


if __name__ == "__main__":
    test_add()
