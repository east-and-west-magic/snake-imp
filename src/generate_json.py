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
                    x_set,
                    x_weapon,
                    x_speed,
                    {x_args: 0},
                ],
                "desc": [
                    "make weapons stationary",
                ],
            },
        }
        train_generated |= xxx
