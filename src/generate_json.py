from .util import dump
from .voc import *


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


@dump
def test_list_mode2(train_generated: dict):
    ###########################################
    # list mode
    ###########################################
    for s in [
        "mode list",
        "list modes",
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