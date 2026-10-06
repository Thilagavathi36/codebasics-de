# loafly/models.py

from .config import DISCOUNT_PERCENT
from .logger import get_logger

logger = get_logger()


def clean_price(price):
    """Clean a price string and return a float."""

    if not price or not price.strip():
        raise ValueError("Price is missing")

    return float(price.replace(",", "").strip())


def apply_discount(total, discount_percent):
    """Apply a discount to the total."""

    return total - total * discount_percent / 100


class Order:

    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.items = []

    def add_item(self, name, price):
        self.items.append((name, price))

    def total(self):
        total = 0

        for name, price in self.items:

            try:
                cleaned_price = clean_price(price)
                total += cleaned_price

            except (ValueError, TypeError) as e:
                logger.warning(
                    "Skipping item '%s' in order %s: %s",
                    name,
                    self.order_id,
                    e
                )

            finally:
                logger.info(
                    "Finished processing price for item '%s' in order %s",
                    name,
                    self.order_id
                )

        return apply_discount(total, DISCOUNT_PERCENT)