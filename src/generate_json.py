from .util import dump
from .voc import *


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