import os
import uuid
import pytest

from dundie.core import load
from .constants import PEOPLE_FILE


def setup_module():
    """Setup module to ensure the test environment is ready."""
    # This can be used to set up any necessary state before tests run
    print()
    print("First: Setting up the test module.\n")


def teardown_module():
    """Teardown module to clean up after tests."""
    # This can be used to clean up any state after tests run
    print()
    print("Last: Cleaning up the test module.\n")


@pytest.fixture(scope="function", autouse=True)
def create_new_file(tmpdir):
    """Fixture to create a new file for each test."""
    file_ = tmpdir.join("new_file.txt")
    file_.write("this is side effects.")
    yield
    file_.remove(ignore_errors=True)  # Clean up after the test


@pytest.mark.unit
@pytest.mark.high
def test_load(request):
    """Test the load function."""
    # side effect: create the file if it does not exist
    filepath = f"arquivo_indesejado-{uuid.uuid4()}.txt"
    request.addfinalizer(
        lambda: os.unlink(filepath) if os.path.exists(filepath) else "File not found"
    )

    with open(filepath, "w") as file_:
        file_.write("dados uteis somente para teste")

    data = load(PEOPLE_FILE)
    assert len(data) == 2
    assert data[0] == "Jim Halpert, Sales, Salesman, jim@dundlermifflin.com"
