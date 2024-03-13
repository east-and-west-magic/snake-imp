import os
import json
from glob import glob


DIR_NAME = 'gen_data'


def write_json(data: dict, filename: str):
    for val in data.values():
        if "result" not in val:
            assert False
        if "desc" not in val:
            assert False
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def dump(f):
    train_generated = {}
    def wrapper():
        f(train_generated)
        func_name = os.environ.get('PYTEST_CURRENT_TEST') \
            .split(':')[-1].split(' ')[0]
        # print(func_name)
        filename = f"./{DIR_NAME}/{func_name}.json"
        write_json(train_generated, filename)
    return wrapper

