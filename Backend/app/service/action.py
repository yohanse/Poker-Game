from typing import List
from app.models.action import ActionModel
from app.models.hand import HandModel
from app.repositories.action import ActionRepository
from app.dtos.params import Params
from app.repositories.hand import HandRepository
from app.utils.game_state import GameState
from app.dtos.action import ActionResponse
from app.action.action import IAction

class ActionService:
    def __init__(self, hand_repository: HandRepository, action_repository: ActionRepository):
        self.hand_repository = hand_repository
        self.action_repository = action_repository

    def process_game(self, params: Params, action: IAction) -> ActionResponse:
        # Fetch hand from the repository
        hand: HandModel = self.hand_repository.fetch_hand(params.hand_id)

        # Fetch all actions for the hand from the repository
        actions: List[ActionModel] = self.action_repository.fetch_all_actions_for_hand(params.hand_id)
        
        # Create the state object
        state: GameState = GameState.from_data(hand, actions)
        
        # Execute the given action on the state
        action: ActionModel = action.execute(state.state, params)
        
        # New action back to the repository
        action: ActionModel = self.action_repository.insert_action(action)

        #Update hand with new action
        hand.pot = max(state.get_pot_amount(), hand.pot)
        hand.winnings = state.get_winnings()
        hand.status = state.get_status()

        hand: HandModel = self.hand_repository.update_hand(hand)

        return ActionResponse.from_action_model(action).to_json()
    
    def is_process_game_available(self, hand_id: str, action: IAction) -> bool:
        # Fetch hand from the repository
        hand: HandModel = self.hand_repository.fetch_hand(hand_id)

        # Fetch all actions for the hand from the repository
        actions: List[ActionModel] = self.action_repository.fetch_all_actions_for_hand(hand_id)
        
        # Create the state object
        state: GameState = GameState.from_data(hand, actions)

        return action.is_execute_available(state.state)