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
def test_enemy_speed(train_generated: dict):
    ###########################################
    # enemy speed
    ###########################################
    for num in [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        ]:
        for s in [
            f"set enemy speed to {num}",
            f"set monster speed to {num}",
        ]:
            xxx = {
                s: {
                    "result": [
                        x_enemy_speed,
                        x_set,
                        {x_args: num},
                    ],
                    "desc": [
                        "enemy speed",
                    ],
                },
            }
            train_generated |= xxx


@dump
def test_player_speed(train_generated: dict):
    ###########################################
    # player speed
    ###########################################
    for num in [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    ]:
        for s in [
            f"change player speed to {num}",
        ]:
            xxx = {
                s: {
                    "result": [
                        x_snake_speed,
                        x_set,
                        {x_args: num},
                    ],
                    "desc": [
                        "snake speed",
                    ],
                },
            }
            train_generated |= xxx


@dump
def test_obstacle_speed(train_generated: dict):
    ###########################################
    # obstacle speed
    ###########################################
    for num in [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    ]:
        for s in [
            f"change obstacle speed to {num}",
        ]:
            xxx = {
                s: {
                    "result": [
                        x_obstacle_speed,
                        x_set,
                        {x_args: num},
                    ],
                    "desc": [
                        "obstacle speed",
                    ],
                },
            }
            train_generated |= xxx


@dump
def test_prop_speed(train_generated: dict):
    ###########################################
    # prop speed
    ###########################################
    for num in [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    ]:
        for s in [
            f"change prop speed to {num}",
            f"change weapon speed to {num}",
        ]:
            xxx = {
                s: {
                    "result": [
                        x_prop_speed,
                        x_set,
                        {x_args: num},
                    ],
                    "desc": [
                        "prop speed",
                    ],
                },
            }
            train_generated |= xxx