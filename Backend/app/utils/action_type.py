from enum import Enum

class ActionType(Enum):
    BET = "bet"
    RAISE = "raise"
    ALLIN = "allin"
    CALL = "call"
    CHECK = "check"
    FOLD = "fold"
    BURN = "burn"
    FLOP = "flop"
    TURN = "turn"
    RIVER = "river"