import pytest


@pytest.fixture(autouse=True)
def preinit():
    """
    Pytest decorator to run preprcessing proceduce before each test case
    ex: init database and cache
    """
