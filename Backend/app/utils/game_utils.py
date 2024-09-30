from typing import List
from pokerkit import Card


class GameUtils:
    @staticmethod
    def convert_card_to_string(card: Card) -> str:
        return f"{card.rank}{card.suit}"
    
    @staticmethod
    def convert_hole_card(cards: List[List[Card]]) -> List[str]:
        converted_hole_cards = [["" for i in range(2)] for j in range(len(cards))]
        for i in range(len(cards)):
            for j in range(2):
                converted_hole_cards[i][j] = GameUtils.convert_card_to_string(cards[i][j])
        return converted_hole_cards
    
    @staticmethod
    def convert_board_card(board_cards: List[List[Card]]) -> str:
        if len(board_cards) == 3:
            first_card = GameUtils.convert_card_to_string(board_cards[0][0])
            second_card = GameUtils.convert_card_to_string(board_cards[1][0])
            third_card = GameUtils.convert_card_to_string(board_cards[2][0])
            return "flop", f"{first_card}{second_card}{third_card}"
        
        if len(board_cards) == 4:
            fourth_card = GameUtils.convert_card_to_string(board_cards[3][0])
            return "turn", f"{fourth_card}"
        
        if len(board_cards) == 5:
            fivth_card = GameUtils.convert_card_to_string(board_cards[4][0])
            return "river", f"{fivth_card}"