from samples.ch02.customer import Customer
from samples.ch02.product import Product
from samples.ch02.store import Store


class TestCustomer:
    def test_purchase_succeeds_when_enough_inventory(self) -> None:
        # Arrange
        store = Store()
        store.add_inventory(Product.Shampoo, 10)
        customer = Customer()

        # Act
        success = customer.purchase(store, Product.Shampoo, 5)

        # Assert
        assert success is True
        assert store.get_inventory(Product.Shampoo) == 5

    def test_purchase_fails_when_not_enough_inventory(self) -> None:
        # Arrange
        store = Store()
        store.add_inventory(Product.Shampoo, 10)
        customer = Customer()

        # Act
        success = customer.purchase(store, Product.Shampoo, 15)

        # Assert
        assert success is False
        assert store.get_inventory(Product.Shampoo) == 10
