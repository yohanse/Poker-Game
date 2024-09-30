from typing import List
from app.core.common_game import game
from app.dtos.hand import HandResponse
from app.models.hand import HandModel
from app.repositories.hand import HandRepository
from app.utils.game_utils import GameUtils

class StartService:
    def __init__(self, repository: HandRepository):
        self.repository = repository

    def start_game(self, stack: int) -> HandResponse:
        # Creating the state
        state = game(stack, 6)
        for i in range(12):
            state.deal_hole()

        # Creating the hand model
        hand: HandModel = HandModel(
            id=None,
            stack=stack,
            setup="Dealer: Player 6, Samll Blind: Player 1, Big Blind: Player 2",
            status=state.status,
            hole_cards=GameUtils.convert_hole_card(state.hole_cards),
            pot=state.total_pot_amount,
            winnings=None,
            time_stamp=None
        )

        # Creating in the data base
        hand: HandModel = self.repository.insert_hand(hand)
        
        return HandResponse.from_hand_model(hand).to_json()