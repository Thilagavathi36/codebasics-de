# loafly/transform.py

from .models import Order


def transform_orders(rows):
    orders = {}

    for row in rows:
        oid = row["order_id"]

        if oid not in orders:
            orders[oid] = Order(oid, row["customer"])

        orders[oid].add_item(
            row["item_name"],
            row["item_price"]
        )

    return orders