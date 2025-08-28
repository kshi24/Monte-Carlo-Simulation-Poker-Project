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
        expected_bet_1 = ((0.85 - ((1-0.85)/3))/(1-(5/6))) * 100
        result_bet_1 = Advisor.bet(prob_1, 100, 2, test_cards_1)
        Test.test(
            round(result_bet_1, 2),
            round(expected_bet_1, 2),
            "Bet calculation with 2 cards (pre-flop)"
        )

        # Test bet calculation with 5 cards (flop)
        test_cards_2 = [Card(14, "Spades"), Card(14, "Hearts"), 
                    Card(10, "Diamonds"), Card(10, "Clubs"), Card(9, "Spades")]
        prob_2 = 0.65  # Moderate probability
        expected_bet_2 = ((0.65 - ((1-0.65)/2))/(1-(2/3))) * 200
        result_bet_2 = Advisor.bet(prob_2, 200, 1, test_cards_2)
        Test.test(
            round(result_bet_2, 2),
            round(expected_bet_2, 2),
            "Bet calculation with 5 cards (flop)"
        )

        # Test bet calculation with 6 cards (turn)
        test_cards_3 = test_cards_2 + [Card(2, "Hearts")]
        prob_3 = 0.25  # Low probability
        expected_bet_3 = ((0.25 - ((1-0.25)/4))/(1-(1/2))) * 150
        result_bet_3 = Advisor.bet(prob_3, 150, 3, test_cards_3)
        Test.test(
            round(result_bet_3, 2),
            round(expected_bet_3, 2),
            "Bet calculation with 6 cards (turn)"
        )
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
        Test.test(Hand.straight(low_straight), 1, "Ace-low straight test")

        # Test flush vs straight flush
        test_card_6 = Card(10, "Hearts")
        test_card_7 = Card(11, "Hearts")
        test_card_8 = Card(12, "Hearts")
        test_card_9 = Card(13, "Hearts")
        test_card_10 = Card(14, "Hearts")
        royal_flush = [test_card_6, test_card_7, test_card_8, test_card_9, test_card_10]
        Test.test(Hand.royal_flush(royal_flush), "Hearts", "Royal flush test")

        # Test full house with trips on board
        test_card_11 = Card(7, "Diamonds")
        test_card_12 = Card(7, "Clubs")
        test_card_13 = Card(7, "Hearts")
        test_card_14 = Card(9, "Spades")
        test_card_15 = Card(9, "Diamonds")
        full_house = [test_card_11, test_card_12, test_card_13, test_card_14, test_card_15]
        Test.test(Hand.full_house(full_house), [7, 9], "Full house with trips on board")

        # Test four of a kind with one in hand
        test_card_16 = Card(8, "Spades")
        test_card_17 = Card(8, "Hearts")
        test_card_18 = Card(8, "Diamonds")
        test_card_19 = Card(8, "Clubs")
        test_card_20 = Card(2, "Spades")
        quads = [test_card_16, test_card_17, test_card_18, test_card_19, test_card_20]
        Test.test(Hand.four_OAK(quads), 8, "Four of a kind test")

        # Test two pair with one pair on board
        test_card_21 = Card(10, "Clubs")
        test_card_22 = Card(10, "Spades")
        test_card_23 = Card(4, "Diamonds")
        test_card_24 = Card(4, "Hearts")
        test_card_25 = Card(3, "Clubs")
        two_pair = [test_card_21, test_card_22, test_card_23, test_card_24, test_card_25]
        Test.test(Hand.two_pair(two_pair), [10, 4], "Two pair with one pair on board")

        # Test high card with Ace
        test_card_26 = Card(14, "Clubs")
        test_card_27 = Card(3, "Diamonds")
        test_card_28 = Card(7, "Hearts")
        test_card_29 = Card(10, "Spades")
        test_card_30 = Card(12, "Clubs")
        high_card = [test_card_26, test_card_27, test_card_28, test_card_29, test_card_30]
        Test.test(Hand.high_card(high_card), 14, "High card with Ace")

        # Test Monte Carlo with AA vs 1 opponent
        print("\nRunning Monte Carlo test with AA vs 1 opponent...")
        test_hand = [Card(14, "Spades"), Card(13, "Spades"),Card(12, "Spades"),Card(11, "Spades"),Card(10, "Spades"),]
        win_prob = Probability.monte_carlo(test_hand, 1)
        Test.test(win_prob > 0.67, True, f"AA win probability ({win_prob:.1%}) should be >67%")
        Test.run_advisor_tests()
        
if __name__ == "__main__":
    Test.run_edge_case_tests()