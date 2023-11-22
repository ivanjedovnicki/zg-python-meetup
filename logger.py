import logging


def init_logger():
    logger = logging.getLogger()
    formatter = logging.Formatter(
        fmt='[%(levelname)s %(asctime)s %(threadName)s]: %(message)s'
    )
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    console.setLevel(logging.INFO)
    logger.addHandler(console)
    logger.setLevel(logging.INFO)
