from card import Card
from hand_helper import Hand_helper
from hand import Hand
from probability import Probability
from advisor import Advisor

class Test:
    @staticmethod
    def test(function_result, expected, label):
        print(label)
        print("Expected:", expected)
        print("Result:", function_result)
        print("PASS" if function_result == expected else "FAIL")
        print()

    @staticmethod
    def run_advisor_tests():
        print("\nRunning Advisor Tests...\n")
        
        # Test bet calculation with 2 cards (pre-flop)
        test_cards_1 = [Card(14, "Spades"), Card(14, "Hearts")]  # AA
        prob_1 = 0.85  # High probability
        pot_1 = 100
        opponents_1 = 2
        
        # Expected: edge = 0.85 - (0.15/3) = 0.85 - 0.05 = 0.80
        # kelly_bet = 0.80 * 100 = 80
        # discounted = 80 * (1 - 5/6) = 80 * 1/6 = 13.33
        expected_bet_1 = 13.33
        result_bet_1 = Advisor.bet(prob_1, pot_1, opponents_1, test_cards_1)
        Test.test(
            round(result_bet_1, 2),
            round(expected_bet_1, 2),
            "Bet calculation with 2 cards (pre-flop)"
        )

        # Test bet calculation with 5 cards (flop)
        test_cards_2 = [Card(14, "Spades"), Card(14, "Hearts"), 
                    Card(10, "Diamonds"), Card(10, "Clubs"), Card(9, "Spades")]
        prob_2 = 0.65  # Moderate probability
        pot_2 = 200
        opponents_2 = 1
        
        # Expected: edge = 0.65 - (0.35/2) = 0.65 - 0.175 = 0.475
        # kelly_bet = 0.475 * 200 = 95
        # discounted = 95 * (1 - 2/3) = 95 * 1/3 = 31.67
        expected_bet_2 = 31.67
        result_bet_2 = Advisor.bet(prob_2, pot_2, opponents_2, test_cards_2)
        Test.test(
            round(result_bet_2, 2),
            round(expected_bet_2, 2),
            "Bet calculation with 5 cards (flop)"
        )

        # Test bet calculation with 6 cards (turn)
        test_cards_3 = test_cards_2 + [Card(2, "Hearts")]
        prob_3 = 0.75  # Good probability
        pot_3 = 150
        opponents_3 = 3
        
        # Expected: edge = 0.75 - (0.25/4) = 0.75 - 0.0625 = 0.6875
        # kelly_bet = 0.6875 * 150 = 103.125
        # discounted = 103.125 * (1 - 1/2) = 103.125 * 0.5 = 51.56
        expected_bet_3 = 51.56
        result_bet_3 = Advisor.bet(prob_3, pot_3, opponents_3, test_cards_3)
        Test.test(
            round(result_bet_3, 2),
            round(expected_bet_3, 2),
            "Bet calculation with 6 cards (turn)"
        )
        
        # Test should_call method
        print("\nTesting should_call method...")
        should_call_1 = Advisor.should_call(0.4, 50, 150)  # 50/(150+50) = 0.25 required, we have 0.4
        Test.test(should_call_1, True, "Should call with good pot odds")
        
        should_call_2 = Advisor.should_call(0.2, 100, 150)  # 100/(150+100) = 0.4 required, we have 0.2
        Test.test(should_call_2, False, "Should fold with bad pot odds")
        
        # Test get_max_call method
        print("\nTesting get_max_call method...")
        max_call_1 = Advisor.get_max_call(0.33, 200)  # 0.33*200/(1-0.33) = 66/0.67 = 98.51
        Test.test(round(max_call_1, 2), 98.51, "Max call with 33% equity")
        
        max_call_2 = Advisor.get_max_call(0.5, 100)  # 0.5*100/0.5 = 100
        Test.test(round(max_call_2, 2), 100.00, "Max call with 50% equity")

    @staticmethod
    def run_edge_case_tests():
        print("Running Edge Case Tests...\n")
        
        # Test low straight (Ace-low)
        test_card_1 = Card(14, "Spades")
        test_card_2 = Card(2, "Diamonds")
        test_card_3 = Card(3, "Hearts")
        test_card_4 = Card(4, "Clubs")
        test_card_5 = Card(5, "Spades")
        low_straight = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5]
        result = Hand.straight(low_straight)
        Test.test(result, 5, "Ace-low straight test (should return 5 as high card)")

        # Test royal flush
        test_card_6 = Card(10, "Hearts")
        test_card_7 = Card(11, "Hearts")
        test_card_8 = Card(12, "Hearts")
        test_card_9 = Card(13, "Hearts")
        test_card_10 = Card(14, "Hearts")
        royal_flush = [test_card_6, test_card_7, test_card_8, test_card_9, test_card_10]
        result = Hand.royal_flush(royal_flush)
        Test.test(result, "Hearts", "Royal flush test")

        # Test full house
        test_card_11 = Card(7, "Diamonds")
        test_card_12 = Card(7, "Clubs")
        test_card_13 = Card(7, "Hearts")
        test_card_14 = Card(9, "Spades")
        test_card_15 = Card(9, "Diamonds")
        full_house = [test_card_11, test_card_12, test_card_13, test_card_14, test_card_15]
        result = Hand.full_house(full_house)
        expected = (7, 9)  # trips of 7s, pair of 9s
        Test.test(result, expected, "Full house test")

        # Test four of a kind
        test_card_16 = Card(8, "Spades")
        test_card_17 = Card(8, "Hearts")
        test_card_18 = Card(8, "Diamonds")
        test_card_19 = Card(8, "Clubs")
        test_card_20 = Card(2, "Spades")
        quads = [test_card_16, test_card_17, test_card_18, test_card_19, test_card_20]
        result = Hand.four_OAK(quads)
        expected = (8, 2)  # quad 8s with 2 kicker
        Test.test(result, expected, "Four of a kind test")

        # Test two pair
        test_card_21 = Card(10, "Clubs")
        test_card_22 = Card(10, "Spades")
        test_card_23 = Card(4, "Diamonds")
        test_card_24 = Card(4, "Hearts")
        test_card_25 = Card(3, "Clubs")
        two_pair = [test_card_21, test_card_22, test_card_23, test_card_24, test_card_25]
        result = Hand.two_pair(two_pair)
        expected = (10, 4, 3)  # 10s and 4s with 3 kicker
        Test.test(result, expected, "Two pair test")

        # Test high card
        test_card_26 = Card(14, "Clubs")
        test_card_27 = Card(3, "Diamonds")
        test_card_28 = Card(7, "Hearts")
        test_card_29 = Card(10, "Spades")
        test_card_30 = Card(12, "Clubs")
        high_card = [test_card_26, test_card_27, test_card_28, test_card_29, test_card_30]
        result = Hand.high_card(high_card)
        expected = [14, 12, 10, 7, 3]  # Sorted high to low
        Test.test(result, expected, "High card test")

        # Test pair
        pair_cards = [Card(9, "Hearts"), Card(9, "Clubs"), Card(14, "Spades"), 
                      Card(5, "Diamonds"), Card(2, "Hearts")]
        result = Hand.pair(pair_cards)
        if result:
            pair_rank, kickers = result
            Test.test(pair_rank, 9, "Pair rank test")
            Test.test(kickers[:3], [14, 5, 2], "Pair kickers test")
        
        # Test three of a kind
        trips_cards = [Card(6, "Hearts"), Card(6, "Clubs"), Card(6, "Spades"), 
                       Card(13, "Diamonds"), Card(2, "Hearts")]
        result = Hand.three_OAK(trips_cards)
        if result:
            trip_rank, kickers = result
            Test.test(trip_rank, 6, "Three of a kind rank test")
            Test.test(kickers[:2], [13, 2], "Three of a kind kickers test")

        # Test hand comparison
        print("\nTesting hand comparison...")
        hand1 = (7, (10, 4, 3))  # Two pair: 10s and 4s
        hand2 = (8, (14, 13, 12, 11))  # Pair of Aces
        result = Hand.compare_hands(hand1, hand2)
        Test.test(result, -1, "Two pair beats one pair")
        
        hand3 = (5, (9,))  # Straight to 9
        hand4 = (5, (10,))  # Straight to 10
        result = Hand.compare_hands(hand3, hand4)
        Test.test(result, 1, "Lower straight loses to higher straight")

    @staticmethod
    def run_probability_tests():
        print("\nRunning Probability Tests...\n")
        print("This will run a quick Monte Carlo simulation...")
        print("Testing AA vs 1 opponent (should win ~85% of the time)")
        
        test_hand = [Card(14, "Spades"), Card(14, "Hearts")]
        win_prob = Probability.monte_carlo(test_hand, 1, sim_runs=1000)  # Reduced for speed
        
        Test.test(
            win_prob > 0.75,  # AA should win more than 75% against 1 opponent
            True, 
            f"AA win probability ({win_prob:.1%}) should be >75%"
        )
        
        print("\nTesting 72o vs 3 opponents (should win ~10-15% of the time)")
        weak_hand = [Card(7, "Spades"), Card(2, "Hearts")]
        weak_prob = Probability.monte_carlo(weak_hand, 3, sim_runs=1000)
        
        Test.test(
            weak_prob < 0.25,  # 72o should win less than 25% against 3 opponents
            True,
            f"72o win probability ({weak_prob:.1%}) should be <25%"
        )

    @staticmethod
    def run_all_tests():
        print("=" * 50)
        print("RUNNING ALL TESTS")
        print("=" * 50)
        
        Test.run_edge_case_tests()
        Test.run_advisor_tests()
        Test.run_probability_tests()
        
        print("=" * 50)
        print("ALL TESTS COMPLETE")
        print("=" * 50)

if __name__ == "__main__":
    Test.run_all_tests()