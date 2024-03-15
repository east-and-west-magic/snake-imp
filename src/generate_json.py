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
def test_prop_patrol(train_generated: dict):
    ###########################################
    # prop patrol
    ###########################################
    for s in [
        "prop do not move",
        "prop stationary",
    ]:
        xxx = {
            s: {
                "result": [
                    x_disable,
                    x_patrol,
                    {x_args: x_prop}
                ],
                "desc": [
                    "disable patrol",
                ],
            },
        }
        train_generated |= xxx
