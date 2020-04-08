import pytest
def sum(a,b):
    return a+b

@pytest.mark.parametrize("input1, input2, output", [
    (2,3,5),
    (4,4,8),
    (5,7,11)
])

def test_calc_sum(input1,input2, output):
    result = sum(input1,input2)
    assert result == output

# def test_calc_sum_1():
#     result = sum(2,3)
#     assert result == 5
#
# def test_calc_sum_2():
#     result = sum(4,3)
#     assert result == 7
#
# def test_calc_sum_3():
#     result = sum(6,4)
#     assert result == 10

