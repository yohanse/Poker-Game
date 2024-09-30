from pokerkit import State

from app.action.action import IAction
from app.dtos.params import Params
from app.models.action import ActionModel

class AllInAction(IAction):
    def __init__(self) -> None:
        super().__init__()

    def _do_execute(self, state: State, params: Params) -> ActionModel:
        turn_index = state.turn_index
        amount = state.get_effective_stack(turn_index)
        state.complete_bet_or_raise_to(amount)

        return ActionModel(
            id=None,
            hand_id=params.hand_id,
            player=turn_index,
            type="allin",
            card=None,
            amount=amount,
            time_stamp=None
        )
    
    def _is_execute_available(self, state: State, params: Params) -> bool:
        turn_index = state.turn_index

        if turn_index == None:
            return False
        
        amount = state.get_effective_stack(turn_index)
        return state.can_complete_bet_or_raise_to(amount)
    
    def is_execute_available(self, state: State) -> bool:
        turn_index = state.turn_index
        status = state.status

        return state.turn_index != None and status and state.get_effective_stack(turn_index) > 0