from .util import dump
from .voc import *
import pytest

@dump
def test_list_mode(train_generated: dict):
    ###########################################
    # list mode
    ###########################################
    for s in [
        "show mode list",
        "what modes do you support?",
    ]:
        xxx = {
            s: {
                "result": [
                    x_list,
                    x_mode,
                    {},
                ],
                "desc": [
                    "list mode",
                ],
            },
        }
        train_generated |= xxx
