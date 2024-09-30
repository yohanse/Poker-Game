from typing import List, Any, Dict, Optional
from uuid import UUID

from app.models.action import ActionModel

class ActionResponse:
    def __init__(self, id: UUID, player: Optional[int], type: str, card: str, amount: int) -> None:
        self.id: UUID = id
        self.type : str = type
        self.card: str = card
        self.amount: int = amount
        self.player: Optional[int] = player
    
    def to_json(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "player": self.player,
            "type": self.type,
            "card": self.card,
            "amount": self.amount,
        }
    
    @classmethod
    def from_action_model(cls, action: ActionModel) -> "ActionResponse":
        return cls(
            id=action.id,
            player=action.player,
            type=action.type,
            card=action.card,
            amount=action.amount,
        )