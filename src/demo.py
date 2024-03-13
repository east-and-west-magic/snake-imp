import requests
import os
import json
from .voc import *


base_url = "https://steveagi-pgai.hf.space/games/snake/nlp"
header = {'accept': 'application/json', 'Content-Type': 'application/json'}


def read():
    url = f"{base_url}/r"
    myobj = {
        "code": os.getenv("pgai_code"), 
        "command": "help",
    }
    try:
        res = requests.post(url, headers=header, json=myobj)
        if res.status_code == 200:
            print(res.text)
            return res.text
        else:
            print(res.text)
            return None
    except Exception as e:
        print(e)
        return None


def delete():
    url = f"{base_url}/d"
    myobj = {
        "code": os.getenv("pgai_code"), 
        "command": "help",
    }
    try:
        res = requests.post(url, headers=header, json=myobj)
        if res.status_code == 200:
            print(res.text)
            return res.text
        else:
            print(res.text)
            return None
    except Exception as e:
        print(e)
        return None


def create():
    url = f"{base_url}/c"
    myobj = {
        "code": os.getenv("pgai_code"), 
        "command": "help",
        "result": ["x_help", {}],
        "desc": ["help"],
    }
    try:
        res = requests.post(url, headers=header, json=myobj)
        if res.status_code == 200:
            print(res.text)
            return res.text
        else:
            print(res.text)
            return None
    except Exception as e:
        print(e)
        return None


if __name__ == "__main__":
    if read() is None:
        print("[read] error")
        print()
    else:
        print("[read] OK")
        print()

    if delete() is None:
        print("[delete] error")
        print()
    else:
        print("[delete] OK")
        print()
        # create and re-create
        for _ in range(3):
            if create() is None:
                print("[create] error")
                print()
            else:
                print ("[create] OK")
                print()
