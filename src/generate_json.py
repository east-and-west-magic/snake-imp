from .util import dump
from .voc import *
import pytest

@dump
def test_make_weapon_stationary(train_generated: dict):
    ###########################################
    # make weapon stationary
    ###########################################
    for s in [
        "make weapons stationary",
        "make the weapons stationary",
        "stop weapons from moving",
        "let weapons stand still",
    ]:
        xxx = {
            s: {
                "result": [
                    x_disable,
                    x_patrol,
                    {x_args: x_weapon},
                ],
                "desc": [
                    "disable weapons patrol",
                ],
            },
        }
        train_generated |= xxx
