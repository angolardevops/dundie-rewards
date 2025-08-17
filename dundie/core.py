"""Core functionality for the Dundie Rewards application."""
from dundie.utils.log import get_logger


log = get_logger(__name__)

def load(filepath):
    """Load data from the specified file.
    load(filepath: str) -> list[str]:

    >>> len(load("assets/people.csv"))
    2
    >>> load("assets/people.csv")[0]
    'Jim Halpert, Sales, Salesman, jim@dundlermifflin.com\\n'
    >>> load("assets/people.csv")[0][0]
    'J'
    """
    try:
        with open(filepath, "r") as file_:
            data = [line.strip() for line in file_.readlines()]
        return data
    except FileNotFoundError as e:
        log.error(f"File {e} not found.")
        raise e
