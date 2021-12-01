from samples.ch06.listing2.product import Product
from samples.ch06.listing2.order import Order


class TestOrder:
    # State-based testing
    def test_adding_a_product_to_an_order(self) -> None:
        product: Product = Product('Hand wash')
        order: Order = Order()

        order.add_product(product)

        assert len(order.products) == 1
        assert order.products[0] == product
