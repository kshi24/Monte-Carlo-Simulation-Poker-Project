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
