# Imports built in math function
import math

# Implements class Card, a data type that holds card objects of type rank and suit
class Card: 
    # Constructs card object with rank and suit
    # Rank holds the face or number value as an Int
    # Suit holds a String of "Diamonds", "Hearts", "Clubs", "Spades"
    def __init__(self, rank, suit): 
        self.rank = rank
        self.suit = suit

    # Takes card object and returns it as a formatted string, else returns a string saying it is an invalid card value
    # Takes Int values between 2 and 14 inclusive
    # 14 represents an Ace in all cases that are not straights where it is beneficial for it to be a value of 1
    # Converts numerical values to card's face names
    def card_to_string(card): 
        if 1 < card.rank <= 14:
            if  card.rank == 14:
                return f"Ace of {card.suit}"
            elif card.rank == 11:
                return f"Jack of {card.suit}"
            elif card.rank == 12:
                return f"Queen of {card.suit}"
            elif card.rank == 13:
                return f"King of {card.suit}"
            else:
                return f"{card.rank} of {card.suit}"
        else:
            return "Invalid Card Value"
    
    # Takes a properly formatted String and returns a card object
    # String must be in the "Ace of Spades" or "4 of Clubs" format
    # Converts face names into numerical values to become ranks
    # Ace is converted to the value of 14, not 1
    def string_to_card(card_str): 
        if "Ace" in card_str:
            return Card(14, card_str[card_str.find("of ") + 3:])
        elif "King" in card_str:
            return Card(13, card_str[card_str.find("of ") + 3:])
        elif "Queen" in card_str:
            return Card(12, card_str[card_str.find("of ") + 3:])
        elif "Jack" in card_str:
            return Card(11, card_str[card_str.find("of ") + 3:])
        else:
             for i in range(2,11):
                if card_str[0] == str(i):
                    return Card(i, card_str[card_str.find("of ") + 3:])

# Implements methods that help with hand identification
class Hand_helper:
    # Takes types "suits" or "ranks" and returns the amount of `target` value that is found in `card_list`
    # card_list must be a list of objects of type card
    # Type is of type string and indicates whether it is suits or ranks
    # Target is the number or suit type that the function must look for multiple amounts of and can be a string or an int
    # find_common always returns an int with how many it found, 0 if it found none, and -1 if the type is not either suits or ranks indicating an invalid call to the function
    @staticmethod
    def find_common(card_list, type, target): 
        count = 0
        if type == "suits":
            for card in card_list:
                if card.suit == target:
                    count = count + 1
        elif type == "ranks":
            for card in card_list:
                if card.rank == target:
                    count = count + 1
        else:
            return -1
        return count
    
    # Returns the first rank in card_list that then increments for `amount` cards, else returns -1
    @staticmethod
    def increments(card_list, amount): 
        # converts cards to int list based on ranks
        # sorts them in least to greatest order
        def sorts(card_list):
            card_num_list = []
            for card in card_list:
                card_num_list.append(card.rank)
            card_num_list.sort()
            return card_num_list
        
        # does the same thing as sorts but replaces the value of 14 for 1 to account for an extra possibility with aces
        def sorts_ace_as_1(card_list):
            card_num_list = []
            for card in card_list:
                card_num_list.append(1 if card.rank == 14 else card.rank)
            card_num_list.sort()
            return card_num_list

        regular = sorts(card_list)
        ace_as_1 = sorts_ace_as_1(card_list)

        # returns the starting number in the list if it increments for `amount` times, an int value, else returns -1
        def count_increments(card_num_list, amount):
            prev_card_num = card_num_list[0]
            count = 1
            for num in card_num_list:
                if count < amount:
                    if num == prev_card_num + 1:
                        count = count + 1
                    elif(num != prev_card_num):
                        count = 1
                prev_card_num = num
            if count >= amount:
                return 1 if card_list[0].rank == 14 else card_num_list[0]
            return -1
        regular_increments = count_increments(regular, amount)
        ace_as_1_increments = count_increments(ace_as_1, amount)

        # Returns the the regular increment value unless the ace as a value of 1 returns a value higher
        # This can only happen when regular increments is -1 from count increments and ace_as_1 increments correctly
        if(regular_increments > ace_as_1_increments):
            return regular_increments
        else:
            return ace_as_1_increments

# Implements methods that identify which type of hand is actively in a list of cards of various lengths
class Hand:
    @staticmethod
    def high_card(card_list): # Returns highest rank in card_list as an integer
        max_card = card_list[0]
        for card in card_list:
            if card.rank >= max_card.rank:
                max_card = card
       
        return max_card.rank

    @staticmethod
    def pair(card_list): # Returns int value of the rank of card that is the highest pair in card_list, else -1
        for i in range(14, 2, -1):
            if Hand_helper.find_common(card_list, "ranks", i) >= 2:
                return i
        return -1

    @staticmethod
    def three_OAK(card_list): # Returns int value of the rank of card that is the highest three of a kind in card_list, else -1
        for i in range(14, 1, -1):
            if Hand_helper.find_common(card_list, "ranks", i) == 3:
                return i
        return -1

    @staticmethod
    def four_OAK(card_list): # Returns int value of the rank of card that is the highest four of a kind in card_list, else -1
        for i in range(14, 1, -1):
            if Hand_helper.find_common(card_list, "ranks", i) == 4:
                return i
        return -1
    
    @staticmethod
    def two_pair(card_list): # Returns int list of the ranks of cards that make up each pair in card_list, else -1
        pair_1 = Hand.pair(card_list)
        next_card_list = []
        if pair_1 > 0:
            for card in card_list:
                if card.rank != pair_1:
                    next_card_list.append(card)
            if Hand.pair(next_card_list) > 0:
                return [pair_1, Hand.pair(next_card_list)]
        return -1

    @staticmethod
    def full_house(card_list): # Returns int list of the ranks of [three of a kind, pair], else -1
        trip = Hand.three_OAK(card_list)
        next_card_list = []
        if trip > 0:
            for card in card_list:
                if card.rank != trip:
                    next_card_list.append(card)
            if Hand.pair(next_card_list) > 0:
                return [trip, Hand.pair(next_card_list)]
        return -1

    @staticmethod
    def straight(card_list): # Returns the highest first rank in card_list that then increments for 5 cards, else returns -1
        return Hand_helper.increments(card_list, 5)

    @staticmethod
    def flush(card_list): # Returns String of the suit that makes the 5 card flush, else -1
        suits_list = ["Diamonds", "Hearts", "Spades", "Clubs"]
        for suit in suits_list:
            if Hand_helper.find_common(card_list, "suits", suit) >= 5:
                return suit
        return -1

    @staticmethod
    def straight_flush(card_list): # Returns list of suit (string) and first rank (int) in card_list that then increments for 5 cards, else returns -1
        if Hand.flush(card_list) != -1 and Hand.straight(card_list) != -1:
            return [Hand.flush(card_list), Hand.straight(card_list)]
        return -1
    
    @staticmethod
    def royal_flush(card_list): # Returns suit if hand is a straight flush that starts incrementing at `10`, else -1
        straight_flush = Hand.straight_flush(card_list)
        if(straight_flush != -1):
            if straight_flush[1] == 10:
                return straight_flush[0]
        return -1

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

def main():
    Test.run_test()
    Poker_game.start_round()
if __name__ == "__main__":
    main()