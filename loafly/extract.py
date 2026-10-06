
import csv
from .config import RAW_ORDERS_FILE


def extract_orders():
    rows = []

    with open(RAW_ORDERS_FILE, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows.append(row)

    return rows