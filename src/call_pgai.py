import json
import os
import requests
from pathlib import Path
from typing import Any
from .voc import *
import pytest

train_generated_new = {}
train_generated_old = {}
header = {'accept': 'application/json', 'Content-Type': 'application/json'}
url_base = "https://steveagi-pgai.hf.space/games/snake/nlp"
url_create = f"{url_base}/c"
url_delete = f"{url_base}/d"


def post_to_pgai_helper(command: str, result: str, desc: str) -> Any:
    myobj = {
        "code": os.getenv("pgai_code"), 
        "command": command,
        "result": result,
        "desc": desc,
    }
    try:
        res = requests.post(url_create, headers=header, json=myobj)
        if res.status_code == 200:
            print(res.text)
            return res.text
        else:
            print(res.text)
            return None
    except Exception as e:
        print(e)
        return None


def post_to_pgai():
    xs = [x for x in train_generated_new.keys() if x not in train_generated_old]
    for x in xs[:]:
        command = x
        result = train_generated_new[x]['result']
        desc = train_generated_new[x]['desc']
        post_to_pgai_helper(command, result, desc)


def read_file(filename: str, dest: dict):
    PATH = Path(__file__).parent

    file_name_new = PATH/filename

    with open(file_name_new, 'r') as f:
        for _, line in enumerate(f):
            if line.strip():
                x = json.loads(line)
                myobj = {
                    x['command']: {
                        "result": x['result'],
                        "desc": x['desc'],
                    }
                }
                dest |= myobj


def delete(command: str):
    myobj = {
        "code": os.getenv("pgai_code"), 
        "command": command,
    }
    try:
        res = requests.post(url_delete, headers=header, json=myobj)
        if res.status_code == 200:
            print(res.text)
            return res.text
        else:
            print(res.text)
            return None
    except Exception as e:
        print(e)
        return None


def test_read_files():
    for filename, dest in [
        ("tmp.jsonl", train_generated_new),
        ("train.jsonl", train_generated_old),
    ]:
        read_file(filename, dest)

@pytest.mark.skip
def test_delete_all():
    for key in train_generated_new:
        if key == "help":
            continue # demostrate 'key already in data'
        delete(key)

def test_call_pgai():
    post_to_pgai()


if __name__ == "__main__":
    test_read_files()
    test_delete_all()
    test_call_pgai()
