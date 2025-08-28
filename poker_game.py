import math
from card import Card
from probability import Probability
# Implements the prompting for input throughout the game.
class Poker_game:
    # runs each round
    @staticmethod
    def start_round():
        print("Welcome to the poker computer program. The functionality of this project is providing probabilities that can help decision making while playing a game of poker.")
        print("How much money did you bring to the table?")
        money = float(input())
        print("")
        opponents = 0
        while opponents == 0:
            print("How many opponents do you have")
            opponents = int(input())
            if not(opponents <= 22 and opponents > 1):
                print("That was not a valid input, please answer again.")
                print("")
                opponents = 0

        while(True):
            all_cards = []
            print("___________NEW ROUND____________")
            print()
            print("Please list cards as \"Ace of Spades\", using capital letters or \"2 of Hearts\" using the number character, separated by the word \"of\"")
            print()
            print("First hole card?")
            all_cards.append(Card.string_to_card(input()))

            print("Second hole card?")
            all_cards.append(Card.string_to_card(input()))
            Probability.monte_carlo(all_cards, opponents)
            print()
            # spits out probability and advised betting based on kellys criterion
            print()

            print("First community card?")
            all_cards.append(Card.string_to_card(input()))
            print()
            print("Second community card?")
            all_cards.append(Card.string_to_card(input()))
            print()
            print("Third community card?")
            all_cards.append(Card.string_to_card(input()))
            Probability.monte_carlo(all_cards, opponents)
            # spits out probability and advised betting based on kellys criterion
            print()
            print("Fourth community card?")
            all_cards.append(Card.string_to_card(input()))
            Probability.monte_carlo(all_cards, opponents)
            # spits out probability and advised betting based on kellys criterion
            print()
            print("Fifth community card?")
            all_cards.append(Card.string_to_card(input()))
            Probability.monte_carlo(all_cards, opponents)
            # spits out probability and advised betting based on kellys criterion
