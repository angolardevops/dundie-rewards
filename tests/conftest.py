import pytest

MARKER = """\
unit: Mark unit tests
integration: Mark integration tests
high: High Priority
medium: Medium Priority
low: Low Priority
"""

def pytest_configure(config):
    """Configure pytest to recognize custom markers."""
    for marker in MARKER.splitlines():
        if marker.strip():
            config.addinivalue_line("markers", marker.strip())

# disable side effects in tests: automatically change to a temporary directory
@pytest.fixture(autouse=True)
def go_to_tmpdir(request): # injection dependencies
    """Change to a temporary directory for each test."""
    tmpdir = request.getfixturevalue("tmpdir")
    with  tmpdir.as_cwd():
        yield # protocol generators, allows to run the test in the tmpdir
