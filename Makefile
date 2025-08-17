.PHONE: install virtualenv ipython clean

install:
	@echo "Installing  for dev environment"
	@.venv/bin/python -m  pip install -e '.[dev]'

virtualenv:
	@echo "Creating virtual environment"
	@.venv/bin/python -m  pip -m venv .venv
	@echo "Virtual environment created at .venv"

ipython:
	@echo "Installing IPython in virtual environment"
	@.venv/bin/ipython

test:
	@echo "Running tests"
	@.venv/bin/pytest -s

testci:
	@echo "Running tests"
	@.venv/bin/pytest -v --junitxml=test-unit.xml
watch:
	@echo "Watching for changes and running tests"
# 	@.venv/bin/ptw -- -vv -s tests/
	@ls **/*.py | entr pytest

clean:
	@echo "Cleaning up virtual environment"
	@find ./ -name "*.pyc" -exec rm -f {} \;
	@find ./ -name "__pycache__" -exec rm -rf {} \;
	@find ./ -name "Thumbs.db" -exec rm -f {} \;
	@find ./ -name ".DS_Store" -exec rm -f {} \;
	@find ./ -name "*~" -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox
	@rm -rf .coverage
	@rm -rf docs/_build
