from typing import List
from app.models.action import ActionModel
from app.models.hand import HandModel
from app.dtos.params import Params
from app.repositories.history import HistoryRepository
from app.utils.game_state import GameState
from app.dtos.action import ActionResponse
from app.action.action import IAction

class HistoryService:
    def __init__(self, respository: HistoryRepository):
        self.repository = respository

    def fetch_all_history(self) -> ActionResponse:
        # Fetch hand from the repository
        unknowns = self.repository.fetch_all_hands()

        return [unknown.to_json() for unknown in unknowns]