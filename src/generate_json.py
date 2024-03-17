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


@dump
def test_disable_enemy_attack_around(train_generated: dict):
    ###########################################
    # disable enemy attack around
    ###########################################
    for s in [
        "stop the enemies from following the player",
        "stop enemy from following player",
        "disable enemy following player",
        "enemy stop following player",
    ]:
        xxx = {
            s: {
                "result": [
                    x_enemy_attack_around,
                    x_delete,
                    {},
                ],
                "desc": [
                    "enemies/obstacles attack snake/player",
                ],
            },
        }
        train_generated |= xxx