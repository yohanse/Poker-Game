from pokerkit import State

from app.action.action import IAction
from app.dtos.params import Params
from app.models.action import ActionModel
from app.utils.game_utils import GameUtils

class DealAction(IAction):
    def __init__(self) -> None:
        super().__init__()

    def _do_execute(self, state: State, params: Params) -> ActionModel:
        turn_index = state.turn_index
        state.deal_board()
        action_type, card = GameUtils.convert_board_card(state.board_cards)
        return ActionModel(
            id=None,
            hand_id=params.hand_id,
            player=turn_index,
            type=action_type,
            card=card,
            amount=None,
            time_stamp=None
        )
    
    def _is_execute_available(self, state: State, params: Params) -> bool:
        return state.can_deal_board()
    
    def is_execute_available(self, state: State) -> bool:
        return state.can_deal_board()