from typing import List, Optional
from uuid import UUID
from datetime import datetime
from app.models.action import ActionModel
from app.models.hand import HandModel
from app.repositories.base import BaseRepository

class ActionRepository(BaseRepository):
    def insert_action(self, action: ActionModel) -> UUID:
        query = """
            INSERT INTO action (hand_id, type, player, amount, card)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id, hand_id, player, type, amount, card;
        """
        params = (action.hand_id, action.type, action.player, action.amount, action.card)
        result = self.fetch_one(query, params)
        return ActionModel(id=result[0], hand_id=result[1], player=result[2], type=result[3], amount=result[4], card=result[5], time_stamp=None)

    def fetch_all_actions_for_hand(self, hand_id: UUID) -> List:
        query = """
            SELECT id, hand_id, player, type, amount, card, time_stamp
            FROM action
            WHERE hand_id = %s
            ORDER BY time_stamp ASC;
        """
        params = (hand_id,)
        result = self.fetch_all(query, params)
        return [ActionModel(id=r[0], hand_id=r[1], player=r[2], type=r[3], amount=r[4], card=r[5], time_stamp=None) for r in result]