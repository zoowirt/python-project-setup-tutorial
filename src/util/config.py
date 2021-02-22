import os

import yaml


class Config:
    def __init__(self, path: str):
        self.path = path

        # reading values from config file
        cfg = self.load_config_file()
        self.value_1 = check(cfg.get('value_1'), str)
        self.value_2 = check(cfg.get('value_2'), list)
        self.value_dict = self.ValueDict(check(cfg.get('value_dict'), dict))

        # reading values from environment
        env = os.environ
        self.string_from_env = check(env.get('STRING_FROM_ENV'), str)

    class ValueDict:
        def __init__(self, value_dict: dict):
            self.value_3 = check(value_dict['value_3'], str)
            self.value_4: int = check(value_dict['value_4'], int)

    def load_config_file(self) -> dict:
        with open(self.path, 'r') as file:
            cfg = yaml.load(file, Loader=yaml.SafeLoader)
        return cfg


def check(x, t):
    if isinstance(x, t):
        return x
    else:
        raise Exception(f'{x} is not of type {t}')
