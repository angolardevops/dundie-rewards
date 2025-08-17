MARKER = """\
unit: Mark unit tests
integration: Mark integration tests
high: High Priority
medium: Medium Priority
low: Low Priority
"""

def pytest_configure(config):
    """Configure pytest to recognize custom markers."""
    map(lambda line: config.addinivalue_line('markers', line), MARKER.splitlines())
