from card import Card

class Test:
    def test(function_result, expected, label):
        print(label)
        print("Expected:", expected)
        print("Result:", function_result)
        print()

    def run_test():
        print("_____________________Tests:__________________________\n")
        
        # Test.card_to_string_tests()
        # Test.string_to_card_tests()

        # Test.find_common_tests()
        # Test.increments_tests()

        # Test.high_card_tests()
        # Test.pair_tests()
        # Test.three_OAK_tests()
        # Test.four_OAK_tests()
        # Test.two_pair_tests()
        # Test.full_house_tests()
        # Test.straight_tests()
        # Test.flush_tests()
        # Test.straight_flush_tests()
        # Test.royal_flush_tests()

        # Test.choose_tests()
        # Test.find_highest_tests()
        # Test.sum_higher_categories_tests()

        # Test.hands_higher_straight_flush_tests()
        # Test.hands_higher_four_OAK_tests()
        # Test.hands_higher_full_house_tests()
        # Test.hands_higher_flush_tests()
        # Test.hands_higher_straight_tests()
        # Test.hands_higher_three_OAK_tests()
        # Test.hands_higher_two_pair_tests()
        # Test.hands_higher_pair_tests()
        # Test.hands_higher_high_card_tests()




    def card_to_string_tests(): # All tests passed
        test_card_1 = Card(14, "Spades")
        Test.test(Card.card_to_string(test_card_1), "Ace of Spades", "card_to_string Tester:")
        test_card_2 = Card(1, "Spades")
        Test.test(Card.card_to_string(test_card_2), "Invalid Card Value", "card_to_string Tester:")
        test_card_3 = Card(15, "Spades")
        Test.test(Card.card_to_string(test_card_3), "Invalid Card Value", "card_to_string Tester:")
        test_card_4 = Card(12, "Spades")
        Test.test(Card.card_to_string(test_card_4), "Queen of Spades", "card_to_string Tester:")
        test_card_5 = Card(4, "Spades")
        Test.test(Card.card_to_string(test_card_5), "4 of Spades", "card_to_string Tester:")

    def string_to_card_tests(): # All tests passed
        Test.test(Card.card_to_string(Card.string_to_card("Ace of Spades")), "Ace of Spades", "string_to_card Tester:")
        Test.test(Card.card_to_string(Card.string_to_card("Queen of Diamonds")), "Queen of Diamonds", "string_to_card Tester:")
        Test.test(Card.card_to_string(Card.string_to_card("4 of Clubs")), "4 of Clubs", "string_to_card Tester:")

    def find_common_tests(): # All tests passed
        test_card_1 = Card(2, "Spades")
        test_card_2 = Card(2, "Diamonds")
        test_card_3 = Card(2, "Spades")
        test_card_4 = Card(14, "Clubs")
        test_card_5 = Card(14, "Spades")
        test_card_6 = Card(3, "Hearts")
        test_card_7 = Card(3, "Spades")

        test_list_1 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5]
        test_list_2 = [test_card_1, test_card_2, test_card_3]
        test_list_3 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5, test_card_6, test_card_7]

        Test.test(Hand_helper.find_common(test_list_1, "ranks", 2), "3", "find common tester: ")
        Test.test(Hand_helper.find_common(test_list_2, "ranks", 2), "3", "find common tester: ")
        Test.test(Hand_helper.find_common(test_list_3, "ranks", 2), "3", "find common tester: ")
        Test.test(Hand_helper.find_common(test_list_1, "suits", "Spades"), "3", "find common tester: ")
        Test.test(Hand_helper.find_common(test_list_1, "suits", "Hearts"), "0", "find common tester: ")
        Test.test(Hand_helper.find_common(test_list_1, "abc", "dcf"), "-1", "find common tester: ")

    def increments_tests(): # All tests passed
        test_card_1 = Card(4, "Spades")
        test_card_2 = Card(3, "Diamonds")
        test_card_3 = Card(2, "Spades")
        test_card_4 = Card(5, "Clubs")
        test_card_5 = Card(6, "Spades")
        test_card_6 = Card(7, "Hearts")
        test_card_7 = Card(14, "Spades")

        test_card_8 = Card(5, "Spades")
        test_card_9 = Card(8, "Diamonds")
        test_card_10 = Card(10, "Spades")
        test_card_11 = Card(12, "Clubs")
        test_card_12 = Card(14, "Spades")

        test_card_13 = Card(14, "Spades")
        test_card_14 = Card(2, "Diamonds")
        test_card_15 = Card(3, "Spades")
        test_card_16 = Card(4, "Clubs")

        test_card_17 = Card(11, "Spades")
        test_card_18 = Card(12, "Diamonds")
        test_card_19 = Card(13, "Spades")
        test_card_20 = Card(14, "Clubs")


        test_list_1 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5]
        test_list_2 = [test_card_1, test_card_2, test_card_3]
        test_list_3 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5, test_card_6, test_card_7]

        test_list_4 = [test_card_8, test_card_9, test_card_10, test_card_11, test_card_12]
        test_list_5 = [test_card_13, test_card_14, test_card_15, test_card_16]
        test_list_6 = [test_card_17, test_card_18, test_card_19, test_card_20]

        Test.test(Hand_helper.increments(test_list_1, 5), "2", "increments tester: ")
        Test.test(Hand_helper.increments(test_list_2, 2), "2", "increments tester: ")
        Test.test(Hand_helper.increments(test_list_3, 6), "2", "increments tester: ")
        Test.test(Hand_helper.increments(test_list_4, 2), "-1", "increments tester: ")
        Test.test(Hand_helper.increments(test_list_5, 4), "1", "increments tester: ")
        Test.test(Hand_helper.increments(test_list_6, 4), "11", "increments tester: ")

    def high_card_tests(): # All tests passed
        test_card_1 = Card(4, "Spades")
        test_card_2 = Card(3, "Diamonds")
        test_card_3 = Card(2, "Spades")
        test_card_4 = Card(5, "Clubs")
        test_card_5 = Card(6, "Spades")
        test_card_6 = Card(7, "Hearts")
        test_card_7 = Card(14, "Spades")

        test_card_8 = Card(5, "Spades")
        test_card_9 = Card(5, "Diamonds")
        test_card_10 = Card(5, "Spades")
        test_card_11 = Card(2, "Clubs")
        test_card_12 = Card(3, "Spades")

        test_list_1 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5]
        test_list_2 = [test_card_1, test_card_2, test_card_3]
        test_list_3 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5, test_card_6, test_card_7]
        test_list_4 = [test_card_8, test_card_9, test_card_10, test_card_11, test_card_12]

        Test.test(Hand.high_card(test_list_1), "6", "high card tester: ")
        Test.test(Hand.high_card(test_list_3), "14", "high card tester: ")
        Test.test(Hand.high_card(test_list_2), "4", "high card tester: ")
        Test.test(Hand.high_card(test_list_4), "5", "high card tester: ")

    def pair_tests(): # All tests passed
        test_card_1 = Card(4, "Spades")
        test_card_2 = Card(3, "Diamonds")
        test_card_3 = Card(2, "Spades")
        test_card_4 = Card(5, "Clubs")
        test_card_5 = Card(6, "Spades")
        test_card_6 = Card(7, "Hearts")
        test_card_7 = Card(14, "Spades")

        test_card_8 = Card(5, "Spades")
        test_card_9 = Card(5, "Diamonds")
        test_card_10 = Card(5, "Spades")
        test_card_11 = Card(2, "Clubs")
        test_card_12 = Card(3, "Spades")
        test_card_13 = Card(14, "Hearts")
        test_card_14 = Card(14, "Diamonds")
        test_card_15 = Card(14, "Clubs")

        test_list_1 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5]
        test_list_2 = [test_card_1, test_card_2, test_card_3]
        test_list_3 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5, test_card_6, test_card_7]

        test_list_4 = [test_card_8, test_card_9, test_card_10, test_card_11, test_card_12]
        test_list_5 = [test_card_8, test_card_9, test_card_10]
        test_list_6 = [test_card_8, test_card_9, test_card_10, test_card_11, test_card_12, test_card_13, test_card_14, test_card_15]


        Test.test(Hand.pair(test_list_1), "-1", "pair tester: ")
        Test.test(Hand.pair(test_list_2), "-1", "pair tester: ")
        Test.test(Hand.pair(test_list_3), "-1", "pair tester: ")
        Test.test(Hand.pair(test_list_4), "5", "pair tester: ")
        Test.test(Hand.pair(test_list_5), "5", "pair tester: ")
        Test.test(Hand.pair(test_list_6), "14", "pair tester: ")
        
    def three_OAK_tests(): # All tests passed
        test_card_1 = Card(4, "Spades")
        test_card_2 = Card(3, "Diamonds")
        test_card_3 = Card(2, "Spades")
        test_card_4 = Card(5, "Clubs")
        test_card_5 = Card(6, "Spades")
        test_card_6 = Card(7, "Hearts")
        test_card_7 = Card(14, "Spades")

        test_card_8 = Card(5, "Spades")
        test_card_9 = Card(5, "Diamonds")
        test_card_10 = Card(5, "Spades")
        test_card_11 = Card(2, "Clubs")
        test_card_12 = Card(3, "Spades")
        test_card_13 = Card(14, "Hearts")
        test_card_14 = Card(14, "Diamonds")
        test_card_15 = Card(14, "Clubs")

        test_list_1 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5]
        test_list_2 = [test_card_1, test_card_2, test_card_3]
        test_list_3 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5, test_card_6, test_card_7]

        test_list_4 = [test_card_8, test_card_9, test_card_10, test_card_11, test_card_12]
        test_list_5 = [test_card_8, test_card_9, test_card_10]
        test_list_6 = [test_card_8, test_card_9, test_card_10, test_card_11, test_card_12, test_card_13, test_card_14, test_card_15]


        Test.test(Hand.three_OAK(test_list_1), "-1", "three of a kind tester: ")
        Test.test(Hand.three_OAK(test_list_2), "-1", "three of a kind tester: ")
        Test.test(Hand.three_OAK(test_list_3), "-1", "three of a kind tester: ")
        Test.test(Hand.three_OAK(test_list_4), "5", "three of a kind tester: ")
        Test.test(Hand.three_OAK(test_list_5), "5", "three of a kind tester: ")
        Test.test(Hand.three_OAK(test_list_6), "14", "three of a kind tester: ")

    def four_OAK_tests(): # All tests passed
        test_card_1 = Card(4, "Spades")
        test_card_2 = Card(4, "Diamonds")
        test_card_3 = Card(4, "Spades")
        test_card_4 = Card(4, "Clubs")
        test_card_5 = Card(6, "Spades")

        test_card_8 = Card(5, "Spades")
        test_card_9 = Card(5, "Diamonds")
        test_card_10 = Card(5, "Spades")

        test_list_1 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5]
        test_list_2 = [test_card_8, test_card_9, test_card_10]
        
        Test.test(Hand.four_OAK(test_list_1), "4", "four of a kind tester: ")
        Test.test(Hand.four_OAK(test_list_2), "-1", "four of a kind tester: ")

    def two_pair_tests(): # All tests passed
        test_card_1 = Card(4, "Spades")
        test_card_2 = Card(4, "Diamonds")
        test_card_3 = Card(4, "Spades")
        test_card_4 = Card(4, "Clubs")
        test_card_5 = Card(6, "Spades")

        test_card_8 = Card(5, "Spades")
        test_card_9 = Card(5, "Diamonds")
        test_card_10 = Card(5, "Spades")

        test_list_1 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5]
        test_list_2 = [test_card_8, test_card_9, test_card_10]
        test_list_3 = [test_card_1, test_card_2,test_card_8, test_card_9]
        
        Test.test(Hand.two_pair(test_list_1), "-1", "two pair tester: ")
        Test.test(Hand.two_pair(test_list_2), "-1", "two pair tester: ")
        Test.test(Hand.two_pair(test_list_3), "[5, 4]", "two pair tester: ")

    def full_house_tests(): # All tests passed
        test_card_1 = Card(4, "Spades")
        test_card_2 = Card(4, "Diamonds")
        test_card_3 = Card(4, "Spades")
        test_card_4 = Card(4, "Clubs")
        test_card_5 = Card(6, "Spades")

        test_card_8 = Card(5, "Spades")
        test_card_9 = Card(5, "Diamonds")
        test_card_10 = Card(5, "Spades")

        test_list_1 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5]
        test_list_2 = [test_card_8, test_card_9, test_card_10]
        test_list_3 = [test_card_1, test_card_2, test_card_3, test_card_8, test_card_9]
        
        Test.test(Hand.full_house(test_list_1), "-1", "full house tester: ")
        Test.test(Hand.full_house(test_list_2), "-1", "full house tester: ")
        Test.test(Hand.full_house(test_list_3), "[4, 5]", "full house tester: ")

    def straight_tests(): # All tests passed
        test_card_1 = Card(4, "Spades")
        test_card_2 = Card(3, "Diamonds")
        test_card_3 = Card(2, "Spades")
        test_card_4 = Card(5, "Clubs")
        test_card_5 = Card(6, "Spades")
        test_card_6 = Card(7, "Hearts")
        test_card_7 = Card(14, "Spades")

        test_card_8 = Card(5, "Spades")
        test_card_9 = Card(8, "Diamonds")
        test_card_10 = Card(10, "Spades")
        test_card_11 = Card(12, "Clubs")
        test_card_12 = Card(14, "Spades")

        test_card_13 = Card(14, "Spades")
        test_card_14 = Card(2, "Diamonds")
        test_card_15 = Card(3, "Spades")
        test_card_16 = Card(4, "Clubs")

        test_card_17 = Card(11, "Spades")
        test_card_18 = Card(12, "Diamonds")
        test_card_19 = Card(13, "Spades")
        test_card_20 = Card(14, "Clubs")


        test_list_1 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5]
        test_list_2 = [test_card_1, test_card_2, test_card_3]
        test_list_3 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5, test_card_6, test_card_7]

        test_list_4 = [test_card_8, test_card_9, test_card_10, test_card_11, test_card_12]
        test_list_5 = [test_card_13, test_card_14, test_card_15, test_card_16]
        test_list_6 = [test_card_17, test_card_18, test_card_19, test_card_20]

        Test.test(Hand.straight(test_list_1), "2", "straight tester: ")
        Test.test(Hand.straight(test_list_2), "-1", "straight tester: ")
        Test.test(Hand.straight(test_list_3), "2", "straight tester: ")
        Test.test(Hand.straight(test_list_4), "-1", "straight tester: ")
        Test.test(Hand.straight(test_list_5), "-1", "straight tester: ")
        Test.test(Hand.straight(test_list_6), "-1", "straight tester: ")

    def flush_tests(): # All tests passed
        test_card_1 = Card(2, "Spades")
        test_card_2 = Card(2, "Diamonds")
        test_card_3 = Card(2, "Spades")
        test_card_4 = Card(14, "Clubs")
        test_card_5 = Card(14, "Spades")
        test_card_6 = Card(3, "Hearts")
        test_card_7 = Card(3, "Spades")
        test_card_8 = Card(8, "Spades")

        test_list_1 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5, test_card_7, test_card_8]
        test_list_2 = [test_card_1, test_card_2, test_card_3]
        test_list_3 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5, test_card_6, test_card_7]


        Test.test(Hand.flush(test_list_1), "Spades", "flush tester: ")
        Test.test(Hand.flush(test_list_2), "-1", "flush tester: ")
        Test.test(Hand.flush(test_list_3), "-1", "flush tester: ")

    def straight_flush_tests(): # All tests passed
        test_card_1 = Card(4, "Spades")
        test_card_2 = Card(3, "Spades")
        test_card_3 = Card(2, "Spades")
        test_card_4 = Card(5, "Spades")
        test_card_5 = Card(6, "Spades")
        test_card_6 = Card(7, "Hearts")
        test_card_7 = Card(14, "Spades")

        test_card_8 = Card(5, "Diamons")
        test_card_9 = Card(8, "Diamonds")
        test_card_10 = Card(10, "Diamonds")
        test_card_11 = Card(12, "Diamonds")
        test_card_12 = Card(14, "Diamonds")

        test_card_13 = Card(14, "Spades")
        test_card_14 = Card(2, "Diamonds")
        test_card_15 = Card(3, "Spades")
        test_card_16 = Card(4, "Clubs")

        test_card_17 = Card(9, "Clubs")
        test_card_18 = Card(10, "Hearts")
        test_card_19 = Card(11, "Clubs")
        test_card_20 = Card(12, "Clubs")
        test_card_21 = Card(13, "Clubs")


        test_list_1 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5]
        test_list_2 = [test_card_1, test_card_2, test_card_3]
        test_list_3 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5, test_card_6, test_card_7]

        test_list_4 = [test_card_8, test_card_9, test_card_10, test_card_11, test_card_12]
        test_list_5 = [test_card_13, test_card_14, test_card_15, test_card_16]
        test_list_6 = [test_card_17, test_card_18, test_card_19, test_card_20, test_card_21]

        Test.test(Hand.straight_flush(test_list_1), "['Spades', 2]", "straight flush tester: ")
        Test.test(Hand.straight_flush(test_list_2), "-1", "straight flush tester: ")
        Test.test(Hand.straight_flush(test_list_3), "['Spades', 2]", "straight flush tester: ")
        Test.test(Hand.straight_flush(test_list_4), "-1", "straight flush tester: ")
        Test.test(Hand.straight_flush(test_list_5), "-1", "straight flush tester: ")
        Test.test(Hand.straight_flush(test_list_6), "-1", "straight flush tester: ")

    def royal_flush_tests(): # All tests passed
        test_card_1 = Card(4, "Spades")
        test_card_2 = Card(3, "Spades")
        test_card_3 = Card(2, "Spades")
        test_card_4 = Card(5, "Spades")
        test_card_5 = Card(6, "Spades")
        test_card_6 = Card(7, "Hearts")
        test_card_7 = Card(14, "Spades")

        test_card_8 = Card(5, "Diamons")
        test_card_9 = Card(8, "Diamonds")
        test_card_10 = Card(10, "Diamonds")
        test_card_11 = Card(12, "Diamonds")
        test_card_12 = Card(14, "Diamonds")

        test_card_13 = Card(14, "Spades")
        test_card_14 = Card(2, "Diamonds")
        test_card_15 = Card(3, "Spades")
        test_card_16 = Card(4, "Clubs")

        test_card_17 = Card(10, "Clubs")
        test_card_18 = Card(11, "Clubs")
        test_card_19 = Card(12, "Clubs")
        test_card_20 = Card(13, "Clubs")
        test_card_21 = Card(14, "Clubs")


        test_list_1 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5]
        test_list_2 = [test_card_1, test_card_2, test_card_3]
        test_list_3 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5, test_card_6, test_card_7]

        test_list_4 = [test_card_8, test_card_9, test_card_10, test_card_11, test_card_12]
        test_list_5 = [test_card_13, test_card_14, test_card_15, test_card_16]
        test_list_6 = [test_card_17, test_card_18, test_card_19, test_card_20, test_card_21]

        Test.test(Hand.royal_flush(test_list_1), "-1", "royal flush tester: ")
        Test.test(Hand.royal_flush(test_list_2), "-1", "royal flush tester: ")
        Test.test(Hand.royal_flush(test_list_3), "-1", "royal flush tester: ")
        Test.test(Hand.royal_flush(test_list_4), "-1", "royal flush tester: ")
        Test.test(Hand.royal_flush(test_list_5), "-1", "royal flush tester: ")
        Test.test(Hand.royal_flush(test_list_6), "Clubs", "royal flush tester: ")

    def choose_tests(): # All tests passed
        Test.test(Probability.choose(52, 5), "2598960.0", "choose tester: ")

    def find_highest_tests(): # All tests passed
        test_card_1 = Card(4, "Spades")
        test_card_2 = Card(3, "Diamonds")
        test_card_3 = Card(2, "Spades")
        test_card_4 = Card(5, "Clubs")
        test_card_5 = Card(6, "Spades")
        test_card_6 = Card(7, "Hearts")
        test_card_7 = Card(14, "Spades")

        test_card_8 = Card(5, "Spades")
        test_card_9 = Card(8, "Diamonds")
        test_card_10 = Card(10, "Spades")
        test_card_11 = Card(12, "Clubs")
        test_card_12 = Card(14, "Spades")

        test_card_13 = Card(14, "Spades")
        test_card_14 = Card(2, "Diamonds")
        test_card_15 = Card(3, "Spades")
        test_card_16 = Card(4, "Clubs")

        test_card_17 = Card(10, "Clubs")
        test_card_18 = Card(11, "Clubs")
        test_card_19 = Card(12, "Clubs")
        test_card_20 = Card(13, "Clubs")
        test_card_21 = Card(14, "Clubs")

        test_card_22 = Card(10, "Clubs")
        test_card_23 = Card(10, "Diamonds")
        test_card_24 = Card(10, "Spades")
        test_card_25 = Card(13, "Clubs")
        test_card_26 = Card(14, "Diamonds")

        test_card_27 = Card(3, "Clubs")
        test_card_28 = Card(3, "Diamonds")
        test_card_29 = Card(3, "Hearts")
        test_card_30 = Card(8, "Diamonds")
        test_card_31 = Card(8, "Clubs")


        test_list_1 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5]
        test_list_2 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5, test_card_6, test_card_7]

        test_list_3 = [test_card_8, test_card_9, test_card_10, test_card_11, test_card_12]
        test_list_4 = [test_card_13, test_card_14, test_card_15, test_card_16]
        test_list_5 = [test_card_17, test_card_18, test_card_19, test_card_20, test_card_21]
        test_list_6 = [test_card_22, test_card_23, test_card_24, test_card_25, test_card_26]
        test_list_7 = [test_card_27, test_card_28, test_card_29, test_card_30, test_card_31]

        Test.test(Probability.find_highest(test_list_1), "5 (straight)", "find highest tester: ")
        Test.test(Probability.find_highest(test_list_2), "5 (straight)", "find highest tester: ")
        Test.test(Probability.find_highest(test_list_3), "9 (high card)", "find highest tester: ")
        Test.test(Probability.find_highest(test_list_4), "9 (high card)", "find highest tester: ")
        Test.test(Probability.find_highest(test_list_5), "0 (royal flush)", "find highest tester: ")
        Test.test(Probability.find_highest(test_list_6), "6 (three of a kind)", "find highest tester: ")
        Test.test(Probability.find_highest(test_list_7), "3 (full house)", "find highest tester: ")
        
    def sum_higher_categories_tests():
        test_card_1 = Card(4, "Spades")
        test_card_2 = Card(3, "Spades")
        test_card_3 = Card(2, "Spades")
        test_card_4 = Card(5, "Spades")
        test_card_5 = Card(6, "Spades")
        test_card_6 = Card(7, "Hearts")
        test_card_7 = Card(14, "Spades")

        test_card_8 = Card(5, "Diamonds")
        test_card_9 = Card(8, "Diamonds")
        test_card_10 = Card(10, "Diamonds")
        test_card_11 = Card(12, "Diamonds")
        test_card_12 = Card(14, "Diamonds")

        test_card_13 = Card(14, "Spades")
        test_card_14 = Card(2, "Diamonds")
        test_card_15 = Card(3, "Spades")
        test_card_16 = Card(4, "Clubs")

        test_card_17 = Card(10, "Clubs")
        test_card_18 = Card(11, "Clubs")
        test_card_19 = Card(12, "Clubs")
        test_card_20 = Card(13, "Clubs")
        test_card_21 = Card(14, "Clubs")


        test_list_1 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5]
        test_list_2 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5, test_card_6, test_card_7]

        test_list_3 = [test_card_8, test_card_9, test_card_10, test_card_11, test_card_12]
        test_list_4 = [test_card_13, test_card_14, test_card_15, test_card_16]
        test_list_5 = [test_card_17, test_card_18, test_card_19, test_card_20, test_card_21]

        Test.test(Probability.sum_higher_categories(test_list_1), "4.0", "sum higher categories tester: ")
        Test.test(Probability.sum_higher_categories(test_list_2), "4.0", "sum higher categories tester: ")
        Test.test(Probability.sum_higher_categories(test_list_3), "4408.0", "sum higher categories tester: ")
        Test.test(Probability.sum_higher_categories(test_list_4), "1296420.0", "sum higher categories tester: ")
        Test.test(Probability.sum_higher_categories(test_list_5), "0", "sum higher categories tester: ")

    def hands_higher_straight_flush_tests():
        test_card_1 = Card(4, "Spades")
        test_card_2 = Card(3, "Spades")
        test_card_3 = Card(2, "Spades")
        test_card_4 = Card(5, "Spades")
        test_card_5 = Card(6, "Spades")

        test_list_1 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5]

        Test.test(Probability.hands_higher_straight_flush(test_list_1), "28", "hands higher straight flush tester: ")

    def hands_higher_four_OAK_tests():
        test_card_1 = Card(4, "Spades")
        test_card_2 = Card(4, "Clubs")
        test_card_3 = Card(4, "Hearts")
        test_card_4 = Card(4, "Diamonds")
        test_card_5 = Card(6, "Spades")

        test_list_1 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5]

        Test.test(Probability.hands_higher_four_OAK(test_list_1), "432", "hands higher four of a kind tester: ")

    def hands_higher_full_house_tests():
        test_card_1 = Card(4, "Spades")
        test_card_2 = Card(4, "Clubs")
        test_card_3 = Card(4, "Hearts")
        test_card_4 = Card(6, "Diamonds")
        test_card_5 = Card(6, "Spades")

        test_list_1 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5]

        Test.test(Probability.hands_higher_full_house(test_list_1), "115", "hands higher full house tester: ")

    def hands_higher_flush_tests():
        test_card_1 = Card(4, "Spades")
        test_card_2 = Card(5, "Spades")
        test_card_3 = Card(10, "Spades")
        test_card_4 = Card(9, "Spades")
        test_card_5 = Card(6, "Spades")

        test_list_1 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5]

        Test.test(Probability.hands_higher_flush(test_list_1), "8", "hands higher flush tester: ")

    def hands_higher_straight_tests():
        test_card_1 = Card(4, "Spades")
        test_card_2 = Card(3, "Clubs")
        test_card_3 = Card(2, "Spades")
        test_card_4 = Card(5, "Diamonds")
        test_card_5 = Card(6, "Spades")

        test_list_1 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5]

        Test.test(Probability.hands_higher_straight(test_list_1), "2048", "hands higher straight tester: ")

    def hands_higher_three_OAK_tests():
        test_card_1 = Card(4, "Spades")
        test_card_2 = Card(4, "Clubs")
        test_card_3 = Card(4, "Hearts")
        test_card_4 = Card(9, "Diamonds")
        test_card_5 = Card(6, "Spades")

        test_list_1 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5]

        Test.test(Probability.hands_higher_three_OAK(test_list_1), "76032", "hands higher three of a kind tester: ")

    def hands_higher_two_pair_tests():
        test_card_1 = Card(8, "Spades")
        test_card_2 = Card(8, "Clubs")
        test_card_3 = Card(3, "Hearts")
        test_card_4 = Card(11, "Diamonds")
        test_card_5 = Card(11, "Spades")

        test_list_1 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5]

        Test.test(Probability.hands_higher_two_pair(test_list_1), "26136", "hands higher two pair tester: ")

    def hands_higher_pair_tests():
        test_card_1 = Card(4, "Spades")
        test_card_2 = Card(4, "Clubs")
        test_card_3 = Card(10, "Hearts")
        test_card_4 = Card(9, "Diamonds")
        test_card_5 = Card(6, "Spades")

        test_list_1 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5]

        Test.test(Probability.hands_higher_pair(test_list_1), "41472", "hands higher pair tester: ")

    def hands_higher_high_card_tests():
        test_card_1 = Card(10, "Spades")
        test_card_2 = Card(4, "Clubs")
        test_card_3 = Card(3, "Hearts")
        test_card_4 = Card(13, "Diamonds")
        test_card_5 = Card(6, "Spades")

        test_list_1 = [test_card_1, test_card_2, test_card_3, test_card_4, test_card_5]

        Test.test(Probability.hands_higher_high_card(test_list_1), "194580.0", "hands higher high card tester: ")