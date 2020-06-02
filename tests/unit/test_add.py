import pytest

from app.value_object import Valueobj

# checks the add service is working correctly

@pytest.fixture
def new_valueobj():
    vo = Valueobj(1, 2, 4)
    return vo
