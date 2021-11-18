import pytest

from samples.customer import Customer
from samples.store import Store


@pytest.fixture
def store() -> Store:
    store = Store()
    return store


@pytest.fixture
def customer() -> Customer:
    return Customer()
