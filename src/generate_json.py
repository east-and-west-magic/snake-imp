from .util import dump
from .voc import *
import pytest


@dump
def test_change_skin(train_generated: dict):
    ###########################################
    # change skin
    ###########################################
    for weapon in [
        "gun", "sword", "club", "bomb",
    ]:
        for s in [
            f"Change image for {weapon}",
            f"change picture for {weapon}",
        ]:
            xxx = {
                s: {
                    "result": [
                        x_change_skin,
                        {x_args: x_weapon},
                    ],
                    "desc": [
                        "change skin",
                    ],
                },
            }
            train_generated |= xxx
