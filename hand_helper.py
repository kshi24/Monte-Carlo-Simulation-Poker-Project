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
        if not card_list or amount < 1 or amount > len(card_list):
            return -1

        def get_sorted_ranks(ace_low=False):
            ranks = []
            for card in card_list:
                rank = card.rank
                if ace_low and rank == 14:  # Treat Ace as 1 if ace_low
                    rank = 1
                ranks.append(rank)
            return sorted(list(set(ranks)))  # Remove duplicates and sort

        def find_longest_sequence(ranks):
            if not ranks:
                return -1
            
            max_start = -1
            current_start = ranks[0]
            current_length = 1
            
            for i in range(1, len(ranks)):
                if ranks[i] == ranks[i-1] + 1:
                    current_length += 1
                else:
                    if current_length >= amount:
                        return current_start
                    current_start = ranks[i]
                    current_length = 1
            
            if current_length >= amount:
                return current_start
            return -1

        # Check regular ranks (Ace high)
        regular_ranks = get_sorted_ranks(ace_low=False)
        regular_result = find_longest_sequence(regular_ranks)

        # Check with Ace as low (value 1)
        ace_low_ranks = get_sorted_ranks(ace_low=True)
        ace_low_result = find_longest_sequence(ace_low_ranks)

        # Return the best result (prioritize regular ranks if both have sequences)
        if regular_result != -1:
            return regular_result
        return ace_low_result