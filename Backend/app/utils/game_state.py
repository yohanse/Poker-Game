from typing import List
from pokerkit import State

from app.models.action import ActionModel
from app.models.hand import HandModel
from app.core.common_game import game
from app.utils.action_type import ActionType



from typing import List


class GameState:
    def __init__(self, state: State) -> None:
        self.state = state

    def get_winnings(self) -> List[int]:
        return self.state.payoffs
    
    def get_pot_amount(self) -> int:
        return self.state.total_pot_amount

    def get_status(self) -> str:
        return self.state.status

    @classmethod
    def from_data(cls, hand: HandModel, actions: List[ActionModel]) -> "GameState":
        # Initialize the state from the hand setup
        state: State = game(hand.stack, 6)
       
        # Deal the hole cards
        cls._deal_hole_cards(state, hand.hole_cards)

        # Process each action in the list
        for action in actions:
            cls._process_action(state, action)

        return cls(state)
    
    @staticmethod
    def _initialize_state(hand: HandModel) -> State:
        return game(hand.stack, 6)
    
    @staticmethod
    def _deal_hole_cards(state: State, hole_cards: List[List[str]]) -> None:
        for i in range(2):
            for j in range(6):
                state.deal_hole(hole_cards[j][i])

    @staticmethod
    def _process_action(state: State, action: ActionModel) -> None:
        if action.type in {ActionType.BET.value, ActionType.RAISE.value, ActionType.ALLIN.value}:
            state.complete_bet_or_raise_to(action.amount)

        elif action.type in {ActionType.CALL.value, ActionType.CHECK.value}:
            state.check_or_call()

        elif action.type == ActionType.FOLD.value:
            state.fold()

        elif action.type == ActionType.BURN.value:
            state.burn_card(action.card)
        
        elif action.type in {ActionType.FLOP.value, ActionType.TURN.value, ActionType.RIVER.value}:
            state.deal_board(action.card)
        
        elif action.type == {ActionType.BET.value, ActionType.RAISE.value, ActionType.ALLIN.value}: 
            state.complete_bet_or_raise_to(action.amount)

        else:
            raise ValueError(f"Unknown action type: {action.type}")