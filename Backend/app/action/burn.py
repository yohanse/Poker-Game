from pokerkit import State

from app.action.action import IAction
from app.dtos.params import Params
from app.models.action import ActionModel
from app.utils.game_utils import GameUtils

class BurnAction(IAction):
    def __init__(self) -> None:
        super().__init__()

    def _do_execute(self, state: State, params: Params) -> ActionModel:
        turn_index = state.turn_index
        state.burn_card()
        return ActionModel(
            id=None,
            hand_id=params.hand_id,
            player=turn_index,
            type="burn",
            card=GameUtils.convert_card_to_string(state.burn_cards[-1]),
            amount=None,
            time_stamp=None
        )
    
    def _is_execute_available(self, state: State, params: Params) -> bool:
        return state.can_burn_card()
    
    def is_execute_available(self, state: State) -> bool:
        return state.can_burn_card()