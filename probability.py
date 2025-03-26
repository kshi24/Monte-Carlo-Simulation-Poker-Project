
import math
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
           