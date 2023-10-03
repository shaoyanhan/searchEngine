# BEGIN: abpxx6d04wxr
def calculate(a, b):
    return a + b
# END: abpxx6d04wxr

# BEGIN: abpxx6d04wxr_tests
def test_calculate():
    assert calculate(2, 3) == 5
    assert calculate(0, 0) == 0
    assert calculate(-1, 1) == 0
# END: abpxx6d04wxr_tests