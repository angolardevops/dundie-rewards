import pytest

from dundie.core import load
from .constants import PEOPLE_FILE


@pytest.mark.unit
@pytest.mark.high
def test_load():
    """Test the load function."""
    # Test loading a file that exists
    data = load(PEOPLE_FILE)
    assert len(data) == 2
    # breakpoint()  # Debugging breakpoint
    assert data[0] == 'Jim Halpert, Sales, Salesman, jim@dundlermifflin.com'
