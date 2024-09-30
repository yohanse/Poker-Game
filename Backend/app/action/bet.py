from pokerkit import State

from app.action.action import IAction
from app.dtos.params import Params
from app.models.action import ActionModel

class BetAction(IAction):
    def __init__(self) -> None:
        super().__init__()

    def _do_execute(self, state: State, params: Params) -> ActionModel:
        turn_index = state.turn_index
        state.complete_bet_or_raise_to(params.amount)

        return ActionModel(
            id=None,
            hand_id=params.hand_id,
            player=turn_index,
            type="bet",
            card=None,
            amount=params.amount,
            time_stamp=None
        )
    
    def _is_execute_available(self, state: State, params: Params) -> bool:
        if self.is_execute_available(state) == False or params.amount == None or params.amount % 40 != 0:
            return False
        
        amount = params.amount
        return state.can_complete_bet_or_raise_to(amount)
    
    def is_execute_available(self, state: State) -> bool:
        # Does the game end?
        if state.status == False:
            return False
        
        # Do we have current player?
        turn_index = state.turn_index
        if turn_index == None:
            return False
        
        amount = state.get_effective_stack(turn_index)
        bets = max(state.bets)
        
        return amount > 0 and bets == 0 and state.can_complete_bet_or_raise_to()