from .util import dump
from .voc import *
import pytest


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

