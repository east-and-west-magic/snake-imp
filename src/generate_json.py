from .util import dump
from .voc import *
import pytest


@pytest.mark.skip
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


@pytest.mark.skip
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
