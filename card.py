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
    @staticmethod
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
                if card_str.startswith(str(i)):
                    return Card(i, card_str[card_str.find("of ") + 3:])
        # If we get here, the input was invalid
        raise ValueError(f"Invalid card string: '{card_str}'")

