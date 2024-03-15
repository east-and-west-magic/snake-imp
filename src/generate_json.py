from .util import dump
from .voc import *


@dump
def test_decrease_enemy_number(train_generated: dict):
    ###########################################
    # decrease number of enemy
    ###########################################
    for verb in [
        "reduce",
        "decrease",
    ]:
        for noun in [
            "enemy",
            "monster",
        ]:
            for s in [
                f"{verb} number of {noun}",
                f"{verb} quantity of {noun}",
                f"{verb} {noun}'s number",
                f"{verb} {noun}'s quantity",
            ]:
                xxx = {
                    s: {
                        "result": [
                            x_decrease,
                            x_quantity,
                            {x_args: x_enemy},
                        ],
                        "desc": [
                            "decrease number of enemy",
                        ],
                    },
                }
                train_generated |= xxx


@dump
def test_increase_enemy_number(train_generated: dict):
    ###########################################
    # increase number of enemy
    ###########################################
    for verb in [
        "increase",
        "add",
    ]:
        for noun in [
            "enemy",
            "monster",
        ]:
            for s in [
                f"{verb} number of {noun}",
                f"{verb} quantity of {noun}",
                f"{verb} {noun}'s number",
                f"{verb} {noun}'s quantity",
            ]:
                xxx = {
                    s: {
                        "result": [
                            x_increase,
                            x_quantity,
                            {x_args: x_enemy},
                        ],
                        "desc": [
                            "increase number of enemy",
                        ],
                    },
                }
                train_generated |= xxx

                
@dump
def test_play_game(train_generated: dict):
    ###########################################
    # play game
    ###########################################
    for s in [
        "start",
        "play",
        "run",
        "start game",
        "play game",
        "run game"
    ]:
        xxx = {
            s: {
                "result": [
                    x_start,
                    {},
                ],
                "desc": [
                    "play game",
                ],
            },
        }
        train_generated |= xxx

