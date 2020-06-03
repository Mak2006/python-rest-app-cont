# As per assumptions our service must be able to handle incorrect inputs
# So we construct unit test specifically to test sum()

from mathapp.service import sum

def test_sum():
    nulldata1 = [None, None]
    strdata2 = ["a", "b", "c"]
    nulllist = []

    result = str(sum(nulldata1))
    assert "Cannot add null data" == result

    result = str(sum(strdata2))
    assert "Cannot add str data" == result

    result = str(sum(nulllist))
    assert "Cannot add empty list" == result
