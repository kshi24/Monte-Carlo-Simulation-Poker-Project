
import math
from hand import Hand
from itertools import combinations

# Implements probability calculations that are useful information to someone who is playing poker.
class Probability:
    @staticmethod
    def new_card(card_list):
       new_card = None
       # While card_list does not contain new_card
       while True:
            new_rank = math.randInt(1,15)
            suits_list = ["Diamonds", "Hearts", "Spades", "Clubs"]
            new_suit = suits_list[math.randInt(0,4)]

            new_card = Card(new_rank, new_suit)

    def monte_carlo(card_list, opp_num):
       def cardGetter(card_list, opp_num):
           new_card_list = card_list
           return new_card_list.add(Probability.new_card(card_list))
           
    # create list of seperate card hands 
    
    
    
    
    #determines which hand is the winner 
def determine_winner(hands):
    best_hand_rank = -1
    winner_index = 0
  
    # iterate over each player's 7-card hand    
    for i, hand in enumerate(hands): 
        best_rank = -1
        
        # Generate all 5-card hands
        for five_card_hand in combinations(hand, 5):  
            hand_rank = evaluate_hand(five_card_hand)
            best_rank = max(best_rank, hand_rank)
            
        # Update best rank and index in from hands list 
        # if this player had the better hand
        if best_rank > best_hand_rank:  
            best_hand_rank = best_rank
            winner_index = i  
    return winner_index

def evaluate_hand(five_card_hand):
    best_rank = 1 # Default value
    
    # return the best hand, no need to check others
    if Hand.royal_flush(five_card_hand) != -1:
        return 10  
    if Hand.straight_flush(five_card_hand) != -1:
        return 9
    if Hand.four_OAK(five_card_hand) != -1:
        return 8
    if Hand.full_house(five_card_hand) != -1:
        return 7
    if Hand.flush(five_card_hand) != -1:
        return 6
    if Hand.straight(five_card_hand) != -1:
        return 5
    if Hand.three_OAK(five_card_hand) != -1:
        return 4
    if Hand.two_pair(five_card_hand) != -1:
        return 3
    if Hand.pair(five_card_hand) != -1:
        return 2
        
    return best_rank
    