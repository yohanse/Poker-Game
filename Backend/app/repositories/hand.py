import json
from typing import List, Optional
from uuid import UUID

from app.repositories.base import BaseRepository
from app.models.hand import HandModel

class HandRepository(BaseRepository):
    def __init__(self, conn):
        super().__init__(conn)
        
    def fetch_all_hands(self) -> List:
        query = """
            SELECT id, stack, setup, status, hole_cards, winnings, pot
            FROM hand
            WHERE status = FALSE
            ORDER BY time_stamp ASC;
        """
        result = self.fetch_all(query)
        return [HandModel(id=r[0], stack=r[1], setup=r[2], status=r[3], hole_cards=r[4], winnings=r[5], pot=r[6], time_stamp=None) for r in result]

    def insert_hand(self, hand: HandModel) -> HandModel:
        query = """
            INSERT INTO hand (stack, setup, status, hole_cards, pot)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id, stack, setup, status, hole_cards, pot, winnings;
        """
        params = (hand.stack, hand.setup, hand.status, json.dumps(hand.hole_cards), hand.pot)
        result = self.fetch_one(query, params)
        
        return HandModel(id=result[0], stack=result[1], setup=result[2], status=result[3], hole_cards=result[4], pot=result[5], winnings=result[6], time_stamp=None)
    
    def fetch_hand(self, hand_id: UUID) -> HandModel:
        query = """
            SELECT id, stack, setup, status, hole_cards, winnings, pot
            FROM hand
            WHERE id = %s
            ORDER BY time_stamp ASC;
        """

        params = (hand_id,)
        result = self.fetch_one(query, params)
        return HandModel(id=result[0], stack=result[1], setup=result[2], status=result[3], hole_cards=result[4], winnings=result[5], pot=result[6], time_stamp=None)

    def update_hand(self, hand:HandModel) -> HandModel:
        query = """
            UPDATE hand
            SET 
                pot = %s,
                winnings = %s,
                status = %s
            WHERE id = %s
            RETURNING id, stack, setup, status, hole_cards, winnings, pot;
        """

        params = (hand.pot, json.dumps(hand.winnings), hand.status, hand.id)
        result = self.fetch_one(query, params)
        
        return HandModel(id=result[0], stack=result[1], setup=result[2], status=result[3], hole_cards=result[4], winnings=result[5], pot=result[6], time_stamp=None)