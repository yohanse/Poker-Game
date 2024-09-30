import json
from typing import List, Optional
from uuid import UUID

from app.models.action import ActionModel
from app.models.history import HistoryClass
from app.repositories.base import BaseRepository
from app.models.hand import HandModel

class HistoryRepository(BaseRepository):
    def __init__(self, conn):
        super().__init__(conn)
        
    def fetch_all_hands(self) -> List:
        query = """
            SELECT 
            h.id AS hand_id,
            h.stack,
            h.setup,
            h.hole_cards,
            h.pot,
            h.winnings,
            json_agg(
                json_build_object(
                    'id', a.id,
                    'player', a.player,
                    'type', a.type,
                    'amount', a.amount,
                    'card', a.card
                )
                ORDER BY a.time_stamp  -- Sort actions by time_stamp
            ) AS actions
            FROM 
            hand h
            LEFT JOIN 
            action a 
            ON 
            h.id = a.hand_id
            WHERE 
            h.status = false
            GROUP BY 
            h.id
            ORDER BY 
            h.time_stamp DESC;  -- Sort hands by time_stamp
        """
        result = self.fetch_all(query)
        
        return [HistoryClass(id=r[0], stack=r[1], setup=r[2], hole_cards=r[3], pot=r[4], winnings=r[5], actions=[ActionModel(id=a['id'], player=a['player'], type=a['type'], amount=a['amount'], card=a['card'], hand_id=r[0], time_stamp=None) for a in r[6]]) for r in result]