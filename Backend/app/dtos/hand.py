from typing import List, Any, Dict, Optional
from uuid import UUID

from app.models.action import ActionModel
from app.models.hand import HandModel

class HandResponse:
    def __init__(self, id: UUID, stack: int, setup: str, status: bool, hole_cards: List[List[str]], pot: int, winnings: Optional[List[int]]) -> None:
        self.id: UUID = id
        self.stack: int= stack
        self.setup: str = setup
        self.status: bool = status
        self.hole_cards: List[List[str]] = hole_cards
        self.pot: int = pot
        self.winnings: Optional[List[int]] = winnings
    
    def to_json(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "stack": self.stack,
            "setup": self.setup,
            "status": self.status,
            "pot": self.pot,
            "hole_cards": self.hole_cards
        }
    
    @classmethod
    def from_hand_model(cls, hand: HandModel) -> "HandResponse":
        return cls(
            id=hand.id,
            stack=hand.stack,
            setup=hand.setup,
            status=hand.status,
            hole_cards=hand.hole_cards,
            pot=hand.pot,
            winnings=hand.winnings
        )