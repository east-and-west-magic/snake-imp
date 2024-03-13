import json
from .voc import *
import pytest


train_generated = {}


def test_final():
    file_name = "tmp.jsonl"
    with open(file_name, "w") as f:
        for key in train_generated:
            myobj = {
                "command": key,
                "result": train_generated[key]["result"],
                "desc": train_generated[key]["desc"],
            }
            json.dump(myobj, f, indent=None)
            f.write("\n")


if __name__ == "__main__":
    test_final()
