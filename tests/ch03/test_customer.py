from samples.customer import Customer
from samples.product import Product
from samples.store import Store


class TestCustomer:
    def test_purchase_succeeds_when_enough_inventory(
        self, store: Store, customer: Customer
    ) -> None:
        store.add_inventory(Product.Shampoo, 10)

        success = customer.purchase(store, Product.Shampoo, 5)

        assert success is True
        assert store.get_inventory(Product.Shampoo) == 5

    def test_purchase_fails_when_not_enough_inventory(
        self, store: Store, customer: Customer
    ) -> None:
        store.add_inventory(Product.Shampoo, 10)

        success = customer.purchase(store, Product.Shampoo, 15)

        assert success is False
        assert store.get_inventory(Product.Shampoo) == 10
