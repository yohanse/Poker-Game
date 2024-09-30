from dataclasses import dataclass
from uuid import UUID
from typing import List, Optional
from datetime import datetime  # Fixing DateTime to use the correct type

@dataclass
class HandModel:
    id: Optional[UUID]
    stack: int
    setup: str
    status: bool
    hole_cards: List[List[str]]
    winnings: Optional[List[int]]
    pot: int
    time_stamp: Optional[datetime]