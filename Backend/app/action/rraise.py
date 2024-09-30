from pokerkit import State

from app.action.action import IAction
from app.dtos.params import Params
from app.models.action import ActionModel

class RaiseAction(IAction):
    def __init__(self) -> None:
        super().__init__()

    def _do_execute(self, state: State, params: Params) -> ActionModel:
        turn_index = state.turn_index
        amount = params.amount + max(state.bets)
        state.complete_bet_or_raise_to(amount)

        return ActionModel(
            id=None,
            hand_id=params.hand_id,
            player=turn_index,
            type="raise",
            card=None,
            amount=amount,
            time_stamp=None
        )
    
    def _is_execute_available(self, state: State, params: Params) -> bool:
        if self.is_execute_available(state) == False or params.amount == None  or params.amount % 40 != 0:
            return False
        
        amount = params.amount + max(state.bets)
        return state.can_complete_bet_or_raise_to(amount)
    
    def is_execute_available(self, state: State) -> bool:
        # Does the game end?
        if state.status == False:
            return False
        
        # Do we have current player?
        turn_index = state.turn_index
        if turn_index == None:
            return False
        
        amount = state.get_effective_stack(turn_index) - 40
        bets = max(state.bets)
        return amount > 0 and bets != 0 and state.can_complete_bet_or_raise_to()