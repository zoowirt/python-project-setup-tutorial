import logging
import os
from pathlib import Path

from arithmetics.adding_numbers import add_numbers
from util.custom_json_formatter import CustomJsonFormatter
from util.config import Config

logger = logging.getLogger(__name__)


def main():
    _initialize_logging(log_level='INFO')

    logger.info('Starting job')

    path_to_root_directory = Path(__file__).parent.parent
    config = Config(path=os.path.join(path_to_root_directory, 'config.yaml'))
    print(config.value_2)

    result = add_numbers(3, 4)
    print('The result is ', result)

    logger.info('Finished job')


def _initialize_logging(log_level: str) -> None:
    log_handler = logging.StreamHandler()
    formatter = CustomJsonFormatter('%(timestamp)s %(level)s %(name)s %(message)s')
    log_handler.setFormatter(formatter)
    logging.basicConfig(level=log_level, handlers=[log_handler])


if __name__ == "__main__":
    main()
