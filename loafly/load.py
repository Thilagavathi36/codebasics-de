
import time

from . import gateway
from .config import RETRY_COUNT
from .logger import get_logger

logger = get_logger()


def load_orders(orders):

    for oid, order in orders.items():

        total = order.total()

        for attempt in range(1, RETRY_COUNT + 1):

            try:
                result = gateway.save_to_orders_api(oid, total)

                logger.info(
                    "Order %s saved successfully for %s. Total: %.2f",
                    oid,
                    order.customer,
                    total
                )

                break

            except ConnectionError as e:

                if attempt < RETRY_COUNT:
                    logger.warning(
                        "Attempt %s/%s failed for order %s: %s. Retrying...",
                        attempt,
                        RETRY_COUNT,
                        oid,
                        e
                    )

                    time.sleep(1)

                else:
                   
                  logger.error(
                        "Order %s could not be saved after %s attempts: %s",
                        oid,
                        RETRY_COUNT,
                        e
                    )