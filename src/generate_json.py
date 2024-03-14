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
def test_enemy_destroyable(train_generated: dict):
    ###########################################
    # enemy destroyable
    ###########################################
    for s in [
        "make enemy indestructible",
        "make enemy unbreakable",
    ]:
        xxx = {
            s: {
                "result": [
                    x_disable,
                    x_enemy,
                    {x_args: "destroyable"}
                ],
                "desc": [
                    "enable/disable obstacles/enemies destroyable",
                ],
            },
        }
        train_generated |= xxx
