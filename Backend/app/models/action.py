from dataclasses import dataclass
from uuid import UUID
from typing import Optional
from datetime import datetime  # Fixing DateTime to use the correct type

@dataclass
class ActionModel:
    id: Optional[UUID]
    hand_id: UUID
    player: Optional[int]
    type: str
    amount: Optional[int]
    card: Optional[str]  
    time_stamp: Optional[datetime]        