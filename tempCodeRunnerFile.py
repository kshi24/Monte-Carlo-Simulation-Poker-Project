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