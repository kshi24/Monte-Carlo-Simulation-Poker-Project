import math
from hand_helper import Hand_helper

# Implements methods that identify which type of hand is actively in a list of cards of various lengths
class Hand:
    @staticmethod
    def high_card(card_list): 
        # Returns sorted list of ranks in descending order for tie-breaking
        ranks = sorted([card.rank for card in card_list], reverse=True)
        return ranks

    @staticmethod
    def pair(card_list): 
        # Returns tuple of (pair_rank, [kickers]) or None
        pairs = []
        kickers = []
        ranks = [card.rank for card in card_list]
        
        for rank in set(ranks):
            if ranks.count(rank) == 2:
                pairs.append(rank)
            else:
                kickers.append(rank)
                
        if not pairs:
            return None
            
        pairs = sorted(pairs, reverse=True)
        kickers = sorted(kickers, reverse=True)
        return (max(pairs), kickers)

    @staticmethod
    def three_OAK(card_list): 
        # Returns tuple of (trip_rank, [kickers]) or None
        ranks = [card.rank for card in card_list]
        for rank in set(ranks):
            if ranks.count(rank) == 3:
                kickers = sorted([r for r in ranks if r != rank], reverse=True)
                return (rank, kickers)
        return None

    @staticmethod
    def four_OAK(card_list): 
        # Returns tuple of (quad_rank, kicker) or None
        ranks = [card.rank for card in card_list]
        for rank in set(ranks):
            if ranks.count(rank) == 4:
                kicker = max([r for r in ranks if r != rank])
                return (rank, kicker)
        return None
    
    @staticmethod
    def two_pair(card_list):
        ranks = [card.rank for card in card_list]
        rank_counts = {}
        for rank in ranks:
            rank_counts[rank] = rank_counts.get(rank, 0) + 1
        
        pairs = [rank for rank, count in rank_counts.items() if count >= 2]
        pairs = sorted(pairs, reverse=True)[:2]  # Take top two highest pairs
        
        if len(pairs) < 2:
            return None
        
        # Get kicker (highest non-pair card)
        kickers = [rank for rank in ranks if rank not in pairs]
        kicker = max(kickers) if kickers else 0
        
        return (pairs[0], pairs[1], kicker)
    
    @staticmethod
    def full_house(card_list):
        ranks = [card.rank for card in card_list]
        rank_counts = {}
        for rank in ranks:
            rank_counts[rank] = rank_counts.get(rank, 0) + 1
        
        # Get all possible trips and pairs
        trips = [rank for rank, count in rank_counts.items() if count >= 3]
        pairs = [rank for rank, count in rank_counts.items() if count >= 2]
        
        if not trips:
            return None
        
        # Sort descending
        trips = sorted(trips, reverse=True)
        pairs = sorted(pairs, reverse=True)
        
        # Find best trip
        best_trip = trips[0]
        
        # Find best pair that's not part of the best trip
        best_pair = None
        for pair in pairs:
            if pair != best_trip:
                best_pair = pair
                break
        
        # If no separate pair, check if we have another trip to use as pair
        if best_pair is None and len(trips) >= 2:
            best_pair = trips[1]
        
        return (best_trip, best_pair) if best_pair is not None else None
    @staticmethod
    def straight(card_list):
        ranks = [card.rank for card in card_list]
        unique_ranks = sorted(list(set(ranks)))  # Remove duplicates
        
        # Check for Ace-low straight
        if 14 in unique_ranks:
            ranks_with_ace_low = [1 if r == 14 else r for r in ranks]
            unique_ace_low = sorted(list(set(ranks_with_ace_low)))
            if set([1,2,3,4,5]).issubset(set(unique_ace_low)):
                return 5  # Return 5 as high card for Ace-low straight
        
        # Check normal straights
        for i in range(len(unique_ranks) - 4):
            if unique_ranks[i+4] - unique_ranks[i] == 4:
                return unique_ranks[i+4]
                
        return None
    @staticmethod
    def flush(card_list): 
        # Returns tuple of (suit, [ranks]) or None
        suits = [card.suit for card in card_list]
        for suit in set(suits):
            if suits.count(suit) >= 5:
                flush_ranks = sorted([card.rank for card in card_list if card.suit == suit], reverse=True)
                return (suit, flush_ranks[:5])  # Return top 5 cards
        return None

    @staticmethod
    def straight_flush(card_list): 
        # Returns highest straight flush rank or None
        flush = Hand.flush(card_list)
        if not flush:
            return None
            
        suit, _ = flush
        flush_cards = [card for card in card_list if card.suit == suit]
        
        return Hand.straight(flush_cards)
    
    @staticmethod
    def royal_flush(card_list): 
        # Returns suit if royal flush exists
        straight_flush = Hand.straight_flush(card_list)
        if straight_flush == 14:  # Ace-high straight flush
            flush_suit = Hand.flush(card_list)[0]
            return flush_suit
        return None
    
    @staticmethod
    def find_highest(card_list):
        
        if len(card_list) < 5:
            high_cards = sorted([card.rank for card in card_list], reverse=True)
            return (9, tuple(high_cards))

        # Check hands in descending order of strength
        straight_flush = Hand.straight_flush(card_list)
        if straight_flush:
            # Royal flush is just a straight flush with high card Ace (14)
            if straight_flush == 14:
                return (0, (14,))  # Royal flush
            else:
                return (1, (straight_flush,))  # Straight flush (high card)

        quads = Hand.four_OAK(card_list)
        if quads:
            quad_rank, kicker = quads
            return (2, (quad_rank, kicker))

        full_house = Hand.full_house(card_list)
        if full_house:
            trips_rank, pair_rank = full_house
            return (3, (trips_rank, pair_rank))

        flush = Hand.flush(card_list)
        if flush:
            suit, flush_ranks = flush
            return (4, tuple(flush_ranks))  # Top 5 flush cards

        straight = Hand.straight(card_list)
        if straight:
            return (5, (straight,))  # High card of straight

        trips = Hand.three_OAK(card_list)
        if trips:
            trip_rank, kickers = trips
            return (6, (trip_rank, *kickers[:2]))  # Trip + top 2 kickers

        two_pair = Hand.two_pair(card_list)
        if two_pair:
            high_pair, low_pair, kicker = two_pair
            return (7, (high_pair, low_pair, kicker))

        pair = Hand.pair(card_list)
        if pair:
            pair_rank, kickers = pair
            return (8, (pair_rank, *kickers[:3]))  # Pair + top 3 kickers

        # High card: return top 5 cards
        high_cards = sorted([card.rank for card in card_list], reverse=True)[:5]
        return (9, tuple(high_cards))
    
    @staticmethod
    def compare_hands(hand_value1, hand_value2):
        rank1, values1 = hand_value1
        rank2, values2 = hand_value2

        if rank1 < rank2:
            return -1
        elif rank1 > rank2:
            return 1
        
        # Special handling for high-card scenarios
        if rank1 == 9:  # High card case
            for i in range(min(len(values1), len(values2))):
                if values1[i] > values2[i]:
                    return -1
                elif values1[i] < values2[i]:
                    return 1
            return 0
        
        # Standard comparison for other hand types
        for v1, v2 in zip(values1, values2):
            if v1 > v2:
                return -1
            elif v1 < v2:
                return 1
        return 0