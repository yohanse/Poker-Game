from typing import Any, Optional, Dict

class Params:
    def __init__(self, action_string: str, hand_id: Optional[str] = None, amount: Optional[int] = None, stack: Optional[int] = None) -> None:
        self.hand_id: Optional[str] = hand_id
        self.amount: Optional[int] = amount
        self.stack: Optional[int] = stack
        self.action_string: str = action_string

    @classmethod
    def from_json(cls, json: Dict[str, Any]) -> "Params":
        return cls(
            action_string=json.get("action_string", ""),
            hand_id=json.get("handID"),
            amount=json.get("amount"),
            stack=json.get("stack")
        )
