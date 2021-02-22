import logging

logger = logging.getLogger(__name__)


def add_numbers(x: float, y: float) -> float:
    logger.info('Start adding numbers')

    result = x + y

    logger.info('Finished adding numbers')
    return result
