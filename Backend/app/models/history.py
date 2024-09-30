from typing import List, Optional

from app.models.action import ActionModel

class HistoryClass:
    def __init__(self, id: str, stack: int, setup: str, hole_cards: List[List[str]], winnings: Optional[List[int]], pot: int, actions: List[ActionModel]):
        self.id = id
        self.stack = stack
        self.setup = setup
        self.hole_cards = hole_cards
        self.winnings = winnings
        self.pot = pot
        self.actions = actions
    
    def to_json(self):
        return {
            'id': self.id,
            'stack': self.stack,
            'setup': self.setup,
            'hole_cards': self.hole_cards,
            'winnings': self.winnings,
            'actions': [{"type": a.type, "amount": a.amount, "card": a.card} for a in self.actions]
        }