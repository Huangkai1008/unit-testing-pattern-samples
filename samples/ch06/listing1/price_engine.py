from samples.ch06.listing1.product import Product


def calculate_discount(*products: Product) -> float:
    discount: float = len(products) * 0.01
    return min(discount, 0.2)
