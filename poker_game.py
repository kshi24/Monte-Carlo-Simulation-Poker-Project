import math
from card import Card
from probability import Probability
from advisor import Advisor

# Implements the prompting for input throughout the game.
class Poker_game:
    @staticmethod
    def get_betting_advice(all_cards, opponents, pot):
        """Run simulation and provide betting advice"""
        probability = Probability.monte_carlo(all_cards, opponents)
        
        if probability > 0.5:
            # We have positive equity, calculate optimal bet
            bet_amount = Advisor.bet(probability, pot, opponents, all_cards)
            if bet_amount > 0:
                print(f"\n✅ ADVICE: Bet/Raise ${bet_amount:.2f}")
                print(f"   (Win probability: {probability:.1%})")
            else:
                print(f"\n⚠️  ADVICE: Check (marginal spot)")
                print(f"   (Win probability: {probability:.1%})")
        else:
            # We don't have the betting lead, calculate max call
            max_call = Advisor.get_max_call(probability, pot)
            print(f"\n📊 ADVICE: Call up to ${max_call:.2f}, otherwise fold")
            print(f"   (Win probability: {probability:.1%})")
        
        # Also provide call/fold advice if facing a bet
        print(f"\nIf facing a bet:")
        example_bet = pot * 0.5  # Example: half pot bet
        if Advisor.should_call(probability, example_bet, pot):
            print(f"   - Call ${example_bet:.2f} ✓ (half-pot sized bet)")
        else:
            print(f"   - Fold to ${example_bet:.2f} ✗ (half-pot sized bet)")
        
        return probability
    
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
            if not(opponents <= 22 and opponents > 0):
                print("That was not a valid input, please answer again.")
                print("")
                opponents = 0

        while(True):
            all_cards = []
            print("\n___________NEW ROUND____________")
            print()
            
            # Initialize pot for this round
            print("What's the current pot size? (antes/blinds)")
            pot = float(input())
            print()
            
            print("Please list cards as \"Ace of Spades\", using capital letters or \"2 of Hearts\" using the number character, separated by the word \"of\"")
            print()
            
            # PRE-FLOP
            print("========== PRE-FLOP ==========")
            print("First hole card?")
            all_cards.append(Card.string_to_card(input()))
            print("Second hole card?")
            all_cards.append(Card.string_to_card(input()))
            
            probability = Poker_game.get_betting_advice(all_cards, opponents, pot)
            
            # Update pot after betting round
            print("\nHow much was added to the pot this round?")
            pot += float(input())
            print()

            # FLOP
            print("========== FLOP ==========")
            print("First community card?")
            all_cards.append(Card.string_to_card(input()))
            print("Second community card?")
            all_cards.append(Card.string_to_card(input()))
            print("Third community card?")
            all_cards.append(Card.string_to_card(input()))
            
            probability = Poker_game.get_betting_advice(all_cards, opponents, pot)
            
            # Update pot after betting round
            print("\nHow much was added to the pot this round?")
            pot += float(input())
            print()
            
            # TURN
            print("========== TURN ==========")
            print("Fourth community card?")
            all_cards.append(Card.string_to_card(input()))
            
            probability = Poker_game.get_betting_advice(all_cards, opponents, pot)
            
            # Update pot after betting round
            print("\nHow much was added to the pot this round?")
            pot += float(input())
            print()
            
            # RIVER
            print("========== RIVER ==========")
            print("Fifth community card?")
            all_cards.append(Card.string_to_card(input()))
            
            probability = Poker_game.get_betting_advice(all_cards, opponents, pot)
            
            print("\n--- End of hand ---")
            print("\nDo you want to play another hand? (yes/no)")
            if input().lower() != 'yes':
                print("Thanks for playing!")
                break