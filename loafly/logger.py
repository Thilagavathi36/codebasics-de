
import logging


def get_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filename="loafly.log",
        filemode="a"
    )

    return logging.getLogger("loafly")