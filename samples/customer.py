from dataclasses import dataclass

from samples.product import Product
from samples.store import Store

__all__ = ['Customer']


@dataclass
class Customer:
    @classmethod
    def purchase(cls, store: Store, product: Product, quantity: int) -> bool:
        if not store.has_enough_inventory(product, quantity):
            return False

        store.remove_inventory(product, quantity)
        return True
