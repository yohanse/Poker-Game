from typing import List
from app.dtos.hand import HandResponse
from app.models.action import ActionModel
from app.models.hand import HandModel
from app.repositories.action import ActionRepository
from app.dtos.params import Params
from app.repositories.hand import HandRepository
from app.utils.game_state import GameState
from app.dtos.action import ActionResponse
from app.action.action import IAction

class HandService:
    def __init__(self, repository: HandRepository):
        self.repository = repository

    def fetch_all(self) -> List[HandResponse]:
        # Fetch hand from the repository
        hands: HandModel = self.repository.fetch_all_hands()

        return [HandResponse.from_hand_model(hand).to_json() for hand in hands]