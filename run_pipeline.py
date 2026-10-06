# run_pipeline.py
# run_pipeline.py

from dotenv import load_dotenv

load_dotenv()

from loafly.extract import extract_orders
from loafly.transform import transform_orders
from loafly.load import load_orders


def main():
    rows = extract_orders()
    orders = transform_orders(rows)
    load_orders(orders)


if __name__ == "__main__":
    main()
from loafly.extract import extract_orders
from loafly.transform import transform_orders
from loafly.load import load_orders
from loafly.logger import get_logger

logger = get_logger()


def main():

    logger.info("Pipeline started")

    try:
        rows = extract_orders()
        logger.info("Extract completed")

        orders = transform_orders(rows)
        logger.info("Transform completed")

        load_orders(orders)
        logger.info("Load completed")

    except Exception as e:
        logger.error("Pipeline failed: %s", e)

    finally:
        logger.info("Pipeline finished")


if __name__ == "__main__":
    main()