from app.dtos.hand import HandResponse
from app.models.hand import HandModel
from app.repositories.action import ActionRepository
from app.dtos.params import Params
from app.repositories.hand import HandRepository
from app.dtos.action import ActionResponse

class OverService:
    def __init__(self, hand_repository: HandRepository):
        self.hand_repository = hand_repository

    def over(self, hand_id: str) -> ActionResponse:
        # Fetch hand from the repository
        hand: HandModel = self.hand_repository.fetch_hand(hand_id)

        if hand.status:
            raise Exception("Hand isn't over")

        return HandResponse.from_hand_model(hand).to_json()

    def is_over(self, hand_id: str) -> ActionResponse:
        # Fetch hand from the repository
        hand: HandModel = self.hand_repository.fetch_hand(hand_id)

        return not hand.status