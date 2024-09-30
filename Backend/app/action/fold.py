from pokerkit import State

from app.action.action import IAction
from app.dtos.params import Params
from app.models.action import ActionModel

class FoldAction(IAction):
    def __init__(self) -> None:
        super().__init__()

    def _do_execute(self, state: State, params: Params) -> ActionModel:
        turn_index = state.turn_index
        state.fold()
        return ActionModel(
            id=None,
            hand_id=params.hand_id,
            player=turn_index,
            type="fold",
            card=None,
            amount=None,
            time_stamp=None
        )
    
    def _is_execute_available(self, state: State, params: Params) -> bool:
        return state.can_fold()
    
    def is_execute_available(self, state: State) -> bool:
        return state.can_fold()