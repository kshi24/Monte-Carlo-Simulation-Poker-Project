
import math
# Implements methods that identify which type of hand is actively in a list of cards of various lengths
class Hand:
    @staticmethod
    def high_card(card_list): # Returns highest rank in card_list as an integer
        max_card = card_list[0]
        for card in card_list:
            if card.rank >= max_card.rank:
                max_card = card
       
        return max_card.rank

    @staticmethod
    def pair(card_list): # Returns int value of the rank of card that is the highest pair in card_list, else -1
        for i in range(14, 2, -1):
            if Hand_helper.find_common(card_list, "ranks", i) >= 2:
                return i
        return -1

    @staticmethod
    def three_OAK(card_list): # Returns int value of the rank of card that is the highest three of a kind in card_list, else -1
        for i in range(14, 1, -1):
            if Hand_helper.find_common(card_list, "ranks", i) == 3:
                return i
        return -1

    @staticmethod
    def four_OAK(card_list): # Returns int value of the rank of card that is the highest four of a kind in card_list, else -1
        for i in range(14, 1, -1):
            if Hand_helper.find_common(card_list, "ranks", i) == 4:
                return i
        return -1
    
    @staticmethod
    def two_pair(card_list): # Returns int list of the ranks of cards that make up each pair in card_list, else -1
        pair_1 = Hand.pair(card_list)
        next_card_list = []
        if pair_1 > 0:
            for card in card_list:
                if card.rank != pair_1:
                    next_card_list.append(card)
            if Hand.pair(next_card_list) > 0:
                return [pair_1, Hand.pair(next_card_list)]
        return -1

    @staticmethod
    def full_house(card_list): # Returns int list of the ranks of [three of a kind, pair], else -1
        trip = Hand.three_OAK(card_list)
        next_card_list = []
        if trip > 0:
            for card in card_list:
                if card.rank != trip:
                    next_card_list.append(card)
            if Hand.pair(next_card_list) > 0:
                return [trip, Hand.pair(next_card_list)]
        return -1

    @staticmethod
    def straight(card_list): # Returns the highest first rank in card_list that then increments for 5 cards, else returns -1
        return Hand_helper.increments(card_list, 5)

    @staticmethod
    def flush(card_list): # Returns String of the suit that makes the 5 card flush, else -1
        suits_list = ["Diamonds", "Hearts", "Spades", "Clubs"]
        for suit in suits_list:
            if Hand_helper.find_common(card_list, "suits", suit) >= 5:
                return suit
        return -1

    @staticmethod
    def straight_flush(card_list): # Returns list of suit (string) and first rank (int) in card_list that then increments for 5 cards, else returns -1
        if Hand.flush(card_list) != -1 and Hand.straight(card_list) != -1:
            return [Hand.flush(card_list), Hand.straight(card_list)]
        return -1
    
    @staticmethod
    def royal_flush(card_list): # Returns suit if hand is a straight flush that starts incrementing at `10`, else -1
        straight_flush = Hand.straight_flush(card_list)
        if(straight_flush != -1):
            if straight_flush[1] == 10:
                return straight_flush[0]
        return -1

    