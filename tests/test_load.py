import pytest

from dundie.core import load
from .constants import PEOPLE_FILE


@pytest.mark.unit
@pytest.mark.high
def test_load_positive_has_2_people():
    """Test the load function."""
    # side effect: create the file if it does not exist

    data = load(PEOPLE_FILE)
    assert len(data) == 2


@pytest.mark.unit
@pytest.mark.high
def test_load_positive_first_name_starts_with_j():
    """Test the load function."""
    # side effect: create the file if it does not exist

    data = load(PEOPLE_FILE)
    assert data[0][0] == "J"
