import math
import random
from card import Card
from hand import Hand

class Probability:
    @staticmethod
    def generate_deck(excluded_cards, excluded_ranks=None):
        """Generate deck excluding cards and optionally all cards of certain ranks"""
        deck = []
        for suit in ["Diamonds", "Hearts", "Spades", "Clubs"]:
            for rank in range(2, 15):
                if excluded_ranks and rank in excluded_ranks:
                    continue
                card = Card(rank, suit)
                if not any(c.rank == card.rank and c.suit == card.suit for c in excluded_cards):
                    deck.append(card)
        return deck
    
    @staticmethod
    def run_game(card_list, opps):
        if len(card_list) != len({(c.rank, c.suit) for c in card_list}):
            raise ValueError("Duplicate cards in input list")
        # 1. Separate hole cards and known community cards
        hole_cards = card_list[:2]
        known_community = card_list[2:] if len(card_list) > 2 else []
        
        # 2. Generate full deck and remove known cards
        full_deck = Probability.generate_deck([])  # Generate complete deck
        # Remove exact cards that are already known
        remaining_deck = [card for card in full_deck 
                        if not any(card.rank == c.rank and card.suit == c.suit 
                                for c in hole_cards + known_community)]
        random.shuffle(remaining_deck)
        
        # 3. Deal remaining community cards (total = 5)
        full_community = known_community.copy()
        while len(full_community) < 5:
            full_community.append(remaining_deck.pop())
        
        # 4. Now deal opponent cards from remaining deck
        # Need to ensure we have enough cards (2 per opponent)
        if len(remaining_deck) < 2 * opps:
            raise RuntimeError("Not enough cards left for opponents")
        
        opp_hands = []
        for i in range(opps):
            opp_hand = remaining_deck[2*i : 2*i+2]
            opp_hands.append(opp_hand)
        
        # 5. Evaluate all hands
        player_hand = hole_cards + full_community
        player_value = Hand.find_highest(player_hand)
        
        # Compare against each opponent
        player_wins = True
        for opp_hand in opp_hands:
            opp_value = Hand.find_highest(opp_hand + full_community)
            if Hand.compare_hands(player_value, opp_value) >= 0:  # Player doesn't strictly win
                player_wins = False
                break
        
        return player_wins

    @staticmethod
    def monte_carlo(card_list, opps, sim_runs=10000):
        wins = 0
        for i in range(sim_runs):
            if Probability.run_game(card_list, opps):
                wins += 1
            if (i+1) % 1000 == 0:
                print(f"Simulation {i+1}/{sim_runs} - Current win rate: {wins/(i+1):.2%}")
        
        probability = wins / sim_runs
        sd = ((wins * (1 - probability) * (1 - probability)) + ((sim_runs - wins) * probability * probability))/sim_runs
        print(f"\nFinal win probability: {probability:.4f} (based on {sim_runs} simulations)")
        return probability  # IMPORTANT: This line now returns the probability