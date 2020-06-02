#checks the add service is working correctly
import pytest

from model.value_object import Valueobj

@pytest.fixture(scope='module')
def new_valueobj():
    vo = Valueobj(1, 2, 4)
    return vo


