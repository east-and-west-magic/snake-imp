import json
from .voc import *
import pytest


train_generated = {}


def test_increase_death_line():
    global train_generated
    ###########################################
    # increase death line
    ###########################################
    for s in [
        "raise top line",
        "raise top out",
        "raise ceiling",
        "raise death line",
        "raise game over line",
        "lift top line",
        "lift top out",
        "lift ceiling",
        "lift death line",
        "lift game over line",
        "increase top line",
        "increase top out",
        "increase ceiling",
        "increase death line",
        "increase game over line",
    ]:
        xxx = {
            s: {
                "result": [
                    x_increase,
                    x_death_line,
                    {},
                ],
                "desc": [
                    "change death line",
                ],
            },
        }
        train_generated |= xxx


def test_decrease_death_line():
    global train_generated
    ###########################################
    # decrease topline
    ###########################################
    for s in [
        "lower top line",
        "lower top out",
        "lower ceiling",
        "lower death line",
        "lower game over line",
        "decrease top line",
        "decrease top out",
        "decrease ceiling",
        "decrease death line",
        "decrease game over line",
        "reduce top line",
        "reduce top out",
        "reduce ceiling",
        "reduce death line",
        "reduce game over line",
        "drop top line",
        "drop top out",
        "drop ceiling",
        "drop death line",
        "drop game over line",
    ]:
        xxx = {
            s: {
                "result": [
                    x_decrease,
                    x_death_line,
                    {},
                ],
                "desc": [
                    "change death line",
                ],
            },
        }
        train_generated |= xxx


def test_list_props():
    global train_generated
    ###########################################
    # list props
    ###########################################
    for s in [
        "show power ups",
        "show powerups",
        "show buffs",
        "show boosts",
        "show props",
        "list power ups",
        "list powerups",
        "list buffs",
        "list boosts",
        "list props",
        "get power ups",
        "get powerups",
        "get buffs",
        "get boosts",
        "get props",
    ]:
        xxx = {
            s: {
                "result": [
                    x_list,
                    x_prop,
                    {},
                ],
                "desc": [
                    "list powerups",
                ],
            },
        }
        train_generated |= xxx


def test_list_rules():
    global train_generated
    ###########################################
    # list rules
    ###########################################
    for s in [
        "show recipe",
        "show formula",
        "show blueprint",
        "list recipe",
        "list formula",
        "list blueprint",
        "get recipe",
        "get formula",
        "get blueprint",
    ]:
        xxx = {
            s: {
                "result": [
                    x_list,
                    x_rule,
                    {},
                ],
                "desc": [
                    "list rules",
                ],
            },
        }
        train_generated |= xxx


def test_list_modes():
    global train_generated
    ###########################################
    # list modes
    ###########################################
    for s in [
        "show game mode",
        "list game mode",
        "show play mode",
        "list play mode",
        "show game rules",
        "list game rules",
    ]:
        xxx = {
            s: {
                "result": [
                    x_list,
                    x_mode,
                    {},
                ],
                "desc": [
                    "list modes",
                ],
            },
        }
        train_generated |= xxx


def test_reset_game():
    global train_generated
    ###########################################
    # reset game
    ###########################################
    for s in [
        "reset game",
        "start over",
    ]:
        xxx = {
            s: {
                "result": [
                    x_reset,
                    x_game,
                    {},
                ],
                "desc": [
                    "reset game",
                ],
            },
        }
        train_generated |= xxx

def test_list_fruits():
    global train_generated
    ###########################################
    # list fruits
    ###########################################
    for s in [
        'show objects',
        'show items',
        'show elements',
        'show fruits',
        'list objects',
        'list items',
        'list elements',
        'list fruits',
    ]:
        xxx = {
            s: {
                'result': [
                    x_list,
                    x_fruit,
                    {},
                ],
                'desc': [
                    'list fruits',
                ],
            },
        }
        train_generated |= xxx

def test_change_fruit_odds():
    global train_generated
    ###########################################
    # change fruit odds
    ###########################################
    for x_veb, veb in [
        (x_increase, "increase"),
        (x_increase, "boost"),
        (x_increase, "more"),
        (x_decrease, "decrease"),
        (x_decrease, "Reduce"),
        (x_decrease, "less"),
    ]:
        for t in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            for s in [
                f'{veb} the chance of {t}',
                f'{veb} the odds of {t}',
                f'{veb} the probability of {t}',
                f'{veb} odds of object {t}',
                f'{veb} odds of item {t}',
                f'{veb} odds of fruit {t}',
            ]:
                xxx = {
                    s: {
                        'result': [
                            x_veb,
                            x_fruit,
                            x_odd,
                            {x_args: t},
                        ],
                        'desc': [
                            'change fruit odds',
                        ],
                    },
                }
                train_generated |= xxx


def test_change_bomb_odds():
    global train_generated
    ###########################################
    # change bomb odds
    ###########################################
    for x_veb, veb in [
        (x_increase, "increase"),
        (x_increase, "boost"),
        (x_increase, "improve"),
        (x_increase, "enhance"),
        (x_increase, "more"),
        (x_decrease, "decrease"),
        (x_decrease, "Reduce"),
        (x_decrease, "lower"),
        (x_decrease, "cut"),
        (x_decrease, "trim"),
        (x_decrease, "less"),
    ]:
        for s in [
            f'{veb} the chance of bombs',
            f'{veb} the odds of bombs',
            f'{veb} the probability of bombs',
            f'{veb} the possibility of bombs',
        ]:
            xxx = {
                s: {
                    'result': [
                        x_veb,
                        x_bomb,
                        x_odd,
                        {},
                    ],
                    'desc': [
                        'change bomb odds',
                    ]
                },
            }
            train_generated |= xxx


def test_enable_winning_condition():
    global train_generated
    ###########################################
    # disable winning condition
    ###########################################
    for s in [
        "set win condition",
        "win condition on",
        "turn on win condition",
    ]:
        xxx = {
            s: {
                "result": [
                    x_enable,
                    x_winning_condition,
                    {},
                ],
                "desc": [
                    "enable winning condition",
                ],
            },
        }
        train_generated |= xxx


def test_disable_winning_condition():
    global train_generated
    ###########################################
    # disable winning condition
    ###########################################
    for s in [
        "disable win condition",
        "remove win condition",
        "no win condition",
    ]:
        xxx = {
            s: {
                "result": [
                    x_disable,
                    x_winning_condition,
                    {},
                ],
                "desc": [
                    "disable winning condition",
                ],
            },
        }
        train_generated |= xxx


def test_set_winning_condition():
    global train_generated
    ###########################################
    # set winning condition
    ###########################################
    sentences = ["set win condition as scoring certain points"]
    for i in range(10):
        sentences.append(f"set win condition as scoring {i+1} points")

    for s in sentences:
        xxx = {
            s: {
                "result": [
                    x_set,
                    x_winning_condition,
                    {},
                ],
                "desc": [
                    "set winning condition",
                ],
            },
        }
        train_generated |= xxx


def test_object_value():
    global train_generated
    ###########################################
    # set object value
    ###########################################
    for object in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for s in [
            f"make object {object} earn certain points",
            f"object {object} is worth certain points",
        ]:
            xxx = {
                s: {
                    "result": [
                        x_set,
                        x_fruit,
                        x_value,
                        {x_args: object},
                    ],
                    "desc": [
                        "set object value",
                    ],
                },
            }
            train_generated |= xxx


def test_enable_timer():
    global train_generated
    ###########################################
    # enable timer
    ###########################################
    for verb in [
            "set", 
            "make", 
            "create", 
            "add", 
            "enable",
        ]:
        for s in [
            f"{verb} a timer",
            f"{verb} timer",
            f"{verb} time limit",
        ]:
            xxx = {
                s: {
                    "result": [
                        x_enable,
                        x_timer,
                        {},
                    ],
                    "desc": [
                        "enable timer",
                    ],
                },
            }
            train_generated |= xxx


def test_disable_timer_1():
    global train_generated
    ###########################################
    # disable timer
    ###########################################
    for verb in [
            "", 
            "enter", 
            "set", 
            "change to", 
            "switch to", 
            "shift to", 
            "start", 
            "enable",
        ]:
        s = f"{verb} endless mode"
        xxx = {
            s: {
                "result": [
                    x_disable,
                    x_timer,
                    {},
                ],
                "desc": [
                    "disable timer",
                ],
            },
        }
        train_generated |= xxx

def test_disable_timer_2():
    global train_generated
    ###########################################
    # disable timer
    ###########################################
    for verb in [
            "remove", 
            "disable", 
            "get rid of", 
            "no", 
            "delete",
        ]:
        for s in [
            f"{verb} timer",
            f"{verb} time limit",
        ]:
            xxx = {
                s: {
                    "result": [
                        x_disable,
                        x_timer,
                        {},
                    ],
                    "desc": [
                        "disable timer",
                    ],
                },
            }
            train_generated |= xxx


def test_set_timer():
    global train_generated
    ###########################################
    # set timer
    ###########################################
    for verb in [
            "set", 
            "change",
        ]:

        counts = []
        for count in range(1, 201):
            counts.append(count)
        for count in range(210, 1001, 10):
            counts.append(count)

        for count in counts:
            s = f"{verb} timer to {count} seconds"
            xxx = {
                s: {
                    "result": [
                        x_set,
                        x_timer,
                        {x_args: count},
                    ],
                    "desc": [
                        "set timer",
                    ],
                },
            }
            train_generated |= xxx


def test_increase_timer_by():
    global train_generated
    ###########################################
    # set timer
    ###########################################
    for verb in [
            "increase",
        ]:
        for count in range(1, 201):
            s = f"{verb} timer by {count} seconds"
            xxx = {
                s: {
                    "result": [
                        x_increase,
                        x_timer,
                        {x_args: count},
                    ],
                    "desc": [
                        "increase timer",
                    ],
                },
            }
            train_generated |= xxx


def test_increase_timer():
    global train_generated
    ###########################################
    # set timer
    ###########################################
    for s in [
            "increase timer",
            "add time to timer",
        ]:
        xxx = {
            s: {
                "result": [
                    x_increase,
                    x_timer,
                    {},
                ],
                "desc": [
                    "increase timer",
                ],
            },
        }
        train_generated |= xxx


def test_change_skin():
    global train_generated
    ###########################################
    # change skin
    ###########################################
    for verb in ["change",
                 "edit",
                 "customize",
                 "replace",
                 "set",]:
        for noun in ["sprites",
                     "skin",
                     "images",
                     "pictures",
                     "art",]:
            s = f"{verb} {noun}"
            xxx = {
                s: {
                    "result": [
                        x_change,
                        x_skin,
                        {},
                    ],
                    "desc": [
                        "change skin",
                    ],
                },
            }
            train_generated |= xxx
            for x_target, target in [
                (x_prop, "power ups"),
                (x_prop, "powerups"),
                (x_prop, "buffs"),
                (x_prop, "boosts"),
                (x_bomb, "bombs"),
                (x_fruit, "fruits"),
                (x_fruit, "items"),
                (x_fruit, "elements"),
                (x_fruit, "objects"),
            ]:
                for s in [
                    f"{verb} {target} {noun}",
                    f"{verb} {noun} of {target}",
                    f"{verb} {noun} for {target}",
                ]:
                    xxx = {
                        s: {
                            "result": [
                                x_change,
                                x_skin,
                                {x_args: x_target},
                            ],
                            "desc": [
                                "change skin",
                            ],
                        },
                    }
                    train_generated |= xxx


def test_change_background_music():
    global train_generated
    ###########################################
    # change background music
    ###########################################
    for verb in [
            "change", 
            "edit", 
            "adjust", 
            "customize", 
            "replace", 
            "set",
        ]:
        for s in [
            f"{verb} background music",
            f"{verb} bgm",
        ]:
            xxx = {
                s: {
                    "result": [
                        x_change,
                        x_background,
                        x_music,
                        {},
                    ],
                    "desc": [
                        "change background music",
                    ],
                },
            }
            train_generated |= xxx


def test_disable_music():
    global train_generated
    ###########################################
    # disable music
    ###########################################
    for verb in ["remove", "disable", "mute", "no", "delete", "shut off", "switch off"]:
        for s in [
            f"{verb} music",
            f"{verb} background music",
            f"{verb} bgm",
        ]:
            xxx = {
                s: {
                    "result": [
                        x_disable,
                        x_music,
                        {},
                    ],
                    "desc": [
                        "disable music",
                    ],
                },
            }
            train_generated |= xxx


def test_list_fruit_odds():
    global train_generated
    ###########################################
    # list fruit odds
    ###########################################
    for s in [
        "list the chance of spawning objects",
        "show the chance of objects spawning",
        "show the chance of objects dropping",
        "list the chance of spawning fruit",
        "show the chance of fruit spawning",
        "list fruit odds",
    ]:
        xxx = {
            s: {
                "result": [
                    x_list,
                    x_fruit,
                    x_odd,
                    {},
                ],
                "desc": [
                    "list fruit odds",
                ],
            },
        }
        train_generated |= xxx


def test_drop():
    global train_generated
    ###########################################
    # drop objects
    ###########################################
    for i in range(1, 11):
        for x_target, target in [(x_fruit, "objects"), (x_fruit, "fruits")]:
            for s in [
                f"drop {i} {target} at once",
                f"drop {i} {target} at a time",
                f"drop {i} {target} in one go",
            ]:
                xxx = {
                    s: {
                        "result": [
                            x_drop,
                            x_target,
                            {x_args: i},
                        ],
                        "desc": [
                            "drop objects",
                        ],
                    },
                }
                train_generated |= xxx


def test_reduce_fruit_size():
    global train_generated
    ###########################################
    # reduce fruit size
    ###########################################
    for t in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for percentage in [
            "10%", 
            "20%", 
            "25", 
            "30%", 
            "40%", 
            "50%", 
            "60%", 
            "70%", 
            "75", 
            "80%", 
            "90%",
        ]:
            for s in [
                f"reduce object {t} by {percentage}",
                f"reduce fruit {t} by {percentage}",
            ]:
                xxx = {
                    s: {
                        "result": [
                            x_set,
                            x_fruit,
                            x_size,
                            {x_fruit : t, x_args: round(1 - float(percentage.strip("%")) *0.01, 2)},
                        ],
                        "desc": [
                            "reduce fruit size",
                        ],
                    },
                }
                train_generated |= xxx


def test_increase_fruit_size():
    global train_generated
    ###########################################
    # reduce fruit size
    ###########################################
    for t in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for percentage in [
            "10%", 
            "20%", 
            "25", 
            "30%", 
            "40%", 
            "50%", 
            "60%", 
            "70%", 
            "75", 
            "80%", 
            "90%",
        ]:
            for s in [
                f"increase object {t} by {percentage}",
                f"increase fruit {t} by {percentage}",
            ]:
                xxx = {
                    s: {
                        "result": [
                            x_set,
                            x_fruit,
                            x_size,
                            {x_fruit : t, x_args: round(1  + float(percentage.strip("%")) *0.01, 2)},
                        ],
                        "desc": [
                            "reduce fruit size",
                        ],
                    },
                }
                train_generated |= xxx


def test_set_fruit_odds():
    global train_generated
    ###########################################
    # reduce fruit size
    ###########################################
    for t in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for percentage in [
            "10%", 
            "20%", 
            "25", 
            "30%", 
            "40%", 
            "50%", 
            "60%", 
            "70%", 
            "75", 
            "80%", 
            "90%",
        ]:
            for s in [
                f"set object {t} as {percentage}",
                f"object {t} now has a {percentage} chance of spawning",
            ]:
                xxx = {
                    s: {
                        "result": [
                            x_set,
                            x_fruit,
                            x_odd,
                            {x_fruit : t, x_args: round(float(percentage.strip("%")) *0.01, 2)},
                        ],
                        "desc": [
                            "set fruit odds",
                        ],
                    },
                }
                train_generated |= xxx


def test_help():
    global train_generated
    ###########################################
    # help
    ###########################################
    for s in [
        'help',
        'give me some hints',
        'what commands can I use?',
        'how to get started?',
        'new ideas',
        'how to change the game',
    ]:
        xxx = {
            s: {
                'train': '',
                'result': [
                    x_help,
                    {},
                ],
                'desc': [
                    'help',
                ]
            },
        }
        train_generated |= xxx



def test_add_object_1():
    global train_generated
    ###########################################
    # add object
    ###########################################

    for t in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for x_target, target in [
            (x_fruit, "fruit"),
            (x_fruit, "object"),
            (x_fruit, "item"),
            (x_fruit, "element"),
            (x_fruit, ""),
        ]:
            for dest in [
                "generation", 
                "spawn", 
                "drop", 
                "regenerating pool",
            ]:
                s = f"add {target} {t} into {dest}"
                xxx = {
                    s: {
                        "result": [
                            x_add,
                            x_target,
                            {x_args: t},
                        ],
                        "desc": [
                            "add objects",
                        ],
                    },
                }
                train_generated |= xxx


def test_add_object_2():
    global train_generated
    ###########################################
    # add object
    ###########################################

    for t in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for x_target, target in [
            (x_fruit, "fruit"),
            (x_fruit, "object"),
            (x_fruit, "item"),
            (x_fruit, "element"),
            (x_fruit, ""),
        ]:
            for verb in [
                "generate", 
                "spawn", 
                "drop", 
                "regenerate", 
                "add", 
                "increase",
            ]:
                s = f"{verb} {target} {t}"
                xxx = {
                    s: {
                        "result": [
                            x_add,
                            x_target,
                            {x_args: t},
                        ],
                        "desc": [
                            "add objects",
                        ],
                    },
                }
                train_generated |= xxx


def test_add_object_3():
    global train_generated
    ###########################################
    # add object
    ###########################################

    for t in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for x_target, target in [
            (x_fruit, "fruit"),
            (x_fruit, "object"),
            (x_fruit, "item"),
            (x_fruit, "element"),
            (x_fruit, ""),
        ]:
            for verb in [
                "generated", 
                "added", 
            ]:
                s = f"{target} {t} can be {verb}"
                xxx = {
                    s: {
                        "result": [
                            x_add,
                            x_target,
                            {x_args: t},
                        ],
                        "desc": [
                            "add objects",
                        ],
                    },
                }
                train_generated |= xxx


def test_add_object_4():
    global train_generated
    ###########################################
    # add object
    ###########################################

    for verb in [
        "add", 
        "increase", 
    ]:
        for x_target, target in [
            (x_fruit, "fruits"),
            (x_fruit, "objects"),
            (x_fruit, "items"),
            (x_fruit, "elements"),
        ]:
            s = f"{verb} {target}"
            xxx = {
                s: {
                    "result": [
                        x_add,
                        x_target,
                        {},
                    ],
                    "desc": [
                        "add objects",
                    ],
                },
            }
            train_generated |= xxx


def test_delete_object():
    global train_generated
    ###########################################
    # delete object
    ###########################################

    for verb in [
        "remove", 
        # "cancel", 
        # "disable", 
        # "get rid of", 
        "delete", 
        # "decrease",
    ]:
        for x_target, target in [
            (x_fruit, "fruit"),
            (x_fruit, "object"),
            (x_fruit, "item"),
            (x_fruit, "element"),
            (x_fruit, ""),
        ]:
            for t in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                for dest in [
                    # " from generation", 
                    " from spawn", 
                    " from drop", 
                    # " from regenerating pool", 
                    "",
            ]:
                    s = f"{verb}{target} {t}{dest}"
                    xxx = {
                        s: {
                            "result": [
                                x_delete,
                                x_target,
                                {x_args: t},
                            ],
                            "desc": [
                                "delete objects",
                            ],
                        },
                    }
                    train_generated |= xxx


def test_change_freeze_power():
    global train_generated
    ###########################################
    # change freeze power
    ###########################################
    for x_veb, veb in [
        (x_increase, "increase"),
        (x_increase, "expand"),
        (x_increase, "widen"),
        (x_decrease, "decrease"),
        (x_decrease, "Reduce"),
        (x_decrease, "shorten"),
    ]:
        for s in [
            f"{veb} freeze area",
            f"{veb} freeze range",
            f"{veb} freeze radius",
            f"{veb} freeze spread",
            f"{veb} freeze power",
            f"{veb} freeze strength",
        ]:
            xxx = {
                s: {
                    "result": [
                        x_veb,
                        x_freeze,
                        x_power,
                        {},
                    ],
                    "desc": [
                        "change freeze power",
                    ],
                },
            }
            train_generated |= xxx


def test_change_lightning_power():
    global train_generated
    ###########################################
    # change lightning power
    ###########################################
    for x_veb, veb in [
        (x_increase, "increase"),
        (x_increase, "expand"),
        (x_increase, "boost"),
        (x_decrease, "decrease"),
        (x_decrease, "Reduce"),
        (x_decrease, "weaken"),
    ]:
        for s in [
            f"{veb} lightning range",
            f"{veb} lightning power",
            f"{veb} lightning effect",
            f"{veb} lightning strength",
            f"{veb} lightning intensity",
        ]:
            xxx = {
                s: {
                    "result": [
                        x_veb,
                        x_lightning,
                        x_power,
                        {},
                    ],
                    "desc": [
                        "change lightning power",
                    ],
                },
            }
            train_generated |= xxx



def test_custmize_rules():
    global train_generated
    ###########################################
    # combine fruits
    ###########################################
    for obj in [
        "object",
        "item",
        "fruit",
    ]:
        for s in [
            f"{obj} can be combined with {obj} to create {obj}",
        ]:
            xxx = {
                s: {
                    "result": [
                        x_custmize,
                        x_rule,
                        {},
                    ],
                    "desc": [
                        "custmize rules",
                    ],
                },
            }
            train_generated |= xxx


def test_decrease_props1():
    global train_generated
    ###########################################
    # decrease props
    ###########################################
    for verb in [
        "reduce",
        "decrease",
        "cut down",
        "lower",
    ]:
        for x_target, target in [
            (x_prop, "power ups"),
            (x_lightning, "lightning"),
            (x_bomb, "bombs"),
            (x_swap_card, "swap card"),
            (x_freeze, "freeze"),
        ]:
            for s in [
                f"{verb} {target}",
                f"{verb} {target} number",
                f"{verb} number of {target}"
                f"{verb} the number of {target}"
            ]:
                xxx = {
                    s: {
                        "result": [
                            x_decrease,
                            x_target,
                            {},
                        ],
                        "desc": [
                            "decrease power ups",
                        ],
                    },
                }
                train_generated |= xxx


def test_decrease_props2():
    global train_generated
    ###########################################
    # decrease props
    ###########################################
    for verb in [
        "reduce",
        "decrease",
        "cut down",
        "lower",
    ]:
        for x_target, target in [
            (x_prop, "power ups"),
            (x_lightning, "lightning"),
            (x_bomb, "bombs"),
            (x_swap_card, "swap card"),
            (x_freeze, "freeze"),
        ]:
            for number in range(1, 6):
                s = f"{verb} {number} {target}"
                xxx = {
                    s: {
                        "result": [
                            x_decrease,
                            x_target,
                            {x_args: number},
                        ],
                        "desc": [
                            "decrease power ups",
                        ],
                    },
                }
                train_generated |= xxx


def test_decrease_props3():
    global train_generated
    ###########################################
    # decrease props
    ###########################################
    for x_target, target in [
        (x_prop, "power ups"),
        (x_lightning, "lightning"),
        (x_bomb, "bombs"),
        (x_swap_card, "swap card"),
        (x_freeze, "freeze"),
    ]:
        s = f"less {target}"
        xxx = {
            s: {
                "result": [
                    x_decrease,
                    x_target,
                    {},
                ],
                "desc": [
                    "decrease power ups",
                ],
            },
        }
        train_generated |= xxx


def test_delete_props1():
    global train_generated
    ###########################################
    # delete props
    ###########################################
    for x_target, target in [
        (x_prop, "power ups"),
        (x_lightning, "lightning"),
        (x_bomb, "bombs"),
        (x_swap_card, "swap card"),
        (x_freeze, "freeze"),
    ]:
        for s in [
            f"no {target}",
            f"without {target}",
        ]:
            xxx = {
                s: {
                    "result": [
                        x_delete,
                        x_target,
                        {x_args:"all"},
                    ],
                    "desc": [
                        "delete power ups",
                    ],
                },
            }
            train_generated |= xxx


def test_delete_props2():
    global train_generated
    ###########################################
    # delete props
    ###########################################
    for x_target, target in [
        (x_prop, "power ups"),
        (x_lightning, "lightning"),
        (x_bomb, "bombs"),
        (x_swap_card, "swap card"),
        (x_freeze, "freeze"),
    ]:
        for verb in [
            "delete",
            "remove",
        ]:
            for s in [
                f"{verb} {target}",
                f"{verb} all {target}",
                f"{verb} all of {target} ",
            ]:
                xxx = {
                    s: {
                        "result": [
                            x_delete,
                            x_target,
                            {x_args:"all"},
                        ],
                        "desc": [
                            "delete all power ups",
                        ],
                    },
                }
                train_generated |= xxx


def test_delete_props3():
    global train_generated
    ###########################################
    # delete props
    ###########################################
    for x_target, target in [
        (x_prop, "power ups"),
        (x_lightning, "lightning"),
        (x_bomb, "bombs"),
        (x_swap_card, "swap card"),
        (x_freeze, "freeze"),
    ]:
        for verb in [
            "delete",
            "remove",
        ]:
            for number in range(1, 6):
                s = f"{verb} {number} {target}"
                xxx = {
                    s: {
                        "result": [
                            x_delete,
                            x_target,
                            {x_args: number},
                        ],
                        "desc": [
                            "delete some power ups",
                        ],
                    },
                }
                train_generated |= xxx


def test_add_props1():
    global train_generated
    ###########################################
    # add props
    ###########################################
    for x_target, target in [
        (x_prop, "power ups"),
        (x_lightning, "lightning"),
        (x_bomb, "bombs"),
        (x_swap_card, "swap card"),
        (x_freeze, "freeze"),
    ]:
        for verb in [
            "add",
            "increase",
        ]:
            for s in [
                f"{verb} {target}",
                f"{verb} {target} number",
                f"{verb} number of {target}",
            ]:
                xxx = {
                    s: {
                        "result": [
                            x_add,
                            x_target,
                            {},
                        ],
                        "desc": [
                            "add power ups",
                        ],
                    },
                }
                train_generated |= xxx


def test_add_props2():
    global train_generated
    ###########################################
    # add props
    ###########################################
    for x_target, target in [
        (x_prop, "power ups"),
        (x_lightning, "lightning"),
        (x_bomb, "bombs"),
        (x_swap_card, "swap card"),
        (x_freeze, "freeze"),
    ]:
        for verb in [
            "add",
            "increase",
            "produce",
            "generate",
        ]:
            for number in range(1, 6):
                s = f"{verb} {number} {target}"
                xxx = {
                    s: {
                        "result": [
                            x_add,
                            x_target,
                            {x_args: number},
                        ],
                        "desc": [
                            "increase power ups",
                        ],
                    },
                }
                train_generated |= xxx


def test_add_props3():
    global train_generated
    ###########################################
    # add props
    ###########################################
    for x_target, target in [
        (x_prop, "power ups"),
        (x_lightning, "lightning"),
        (x_bomb, "bombs"),
        (x_swap_card, "swap card"),
        (x_freeze, "freeze"),
    ]:
        s = f"more {target}"
        xxx = {
            s: {
                "result": [
                    x_add,
                    x_target,
                    {},
                ],
                "desc": [
                    "increase power ups",
                ],
            },
        }
        train_generated |= xxx


def test_set_props_number():
    global train_generated
    ###########################################
    # set props number
    ###########################################
    for x_target, target in [
        (x_prop, "power ups"),
        (x_lightning, "lightning"),
        (x_bomb, "bombs"),
        (x_swap_card, "swap card"),
        (x_freeze, "freeze"),
    ]:
        for verb in [
            "set",
            "change",
        ]:
            for number in range(1, 6):
                for s in [
                    # f"{verb} {target} as {number}",
                    f"{verb} {target} to {number}",
                    f"{verb} the number of {target} to {number}",
                    # f"{verb} the number of {target} as {number}",
                    f"{verb} {target} number to {number}",
                    # f"{verb} {target} number as {number}",
                ]:
                    xxx = {
                        s: {
                            "result": [
                                x_set,
                                x_target,
                                {x_args: number},
                            ],
                            "desc": [
                                "set props number",
                            ],
                        },
                    }
                    train_generated |= xxx


def test_list_mode():
    global train_generated
    ###########################################
    # list mode
    ###########################################
    for s in [
        "mode list",
        "list modes",
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
