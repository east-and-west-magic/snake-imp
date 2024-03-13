import json
import os
from glob import glob
from .util import DIR_NAME

def pytest_sessionstart(session):
    print()
    print("[PGSoft] Starting... ", end="")
    pass
    print("Ready.")
    
    
def pytest_sessionfinish(session, exitstatus):
    print()
    print()
    print("[PGSoft] Gathering... ", end="")
    gather()
    print("Done.")


def gather():
    train_generated = {}
    files = glob("*.json", root_dir=DIR_NAME)
    for file in files:
        try:
            with open(os.sep.join([DIR_NAME, file]), "r") as f:
                tmp = json.load(f)
            for key in tmp:
                # assert key not in train_generated                
                if key in train_generated:
                    raise Exception(
                        f"The key '{key}' is already in the dataset"
                    )
                train_generated[key] = tmp[key]
        except json.JSONDecodeError:
            pass
    with open("tmp.jsonl", "w") as f:
        for key in train_generated:
            myobj = {
                "command": key,
                "result": train_generated[key]["result"],
                "desc": train_generated[key]["desc"],
            }
            json.dump(myobj, f, indent=None)
            f.write("\n")
