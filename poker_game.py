
# Implements the prompting for input throughout the game.
class Poker_game:
    # runs each round
    def start_round():
        print("Welcome to the poker computer program. The functionality of this project is providing probabilities that can help decision making while playing a game of poker.")
        print()
        print("Please list cards as \"Ace of Spades\", using capital letters or \"2 of Hearts\" using the number character, separated by the word \"of\"")
        while(True):
            all_cards = []
            print("___________NEW ROUND____________")
            print()
            print("First hole card?")
            all_cards = [Card.string_to_card(input())]
            print("Second hole card?")
            all_cards.append(Card.string_to_card(input()))
            print()
            print("First community card?")
            all_cards = [Card.string_to_card(input())]
            print()
            print("Second community card?")
            all_cards.append(Card.string_to_card(input()))
            print()
            print("Third community card?")
            all_cards.append(Card.string_to_card(input()))
            print()
            print("Fourth community card?")
            all_cards.append(Card.string_to_card(input()))
            print()
            print("Fifth community card?")
            all_cards.append(Card.string_to_card(input()))
