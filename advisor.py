class Advisor:
    @staticmethod    
    def bet(probability, pot, opponents, card_list):
        """
        Calculate optimal bet size using Kelly Criterion with street-based discounting
        
        Args:
            probability: Win probability from Monte Carlo simulation (0-1)
            pot: Current pot size
            opponents: Number of opponents
            card_list: List of cards (used to determine street)
        
        Returns:
            Recommended bet size in dollars
        """
        # Determine street based on number of cards
        if len(card_list) == 2:  # Pre-flop (2 hole cards)
            discount = 5/6
        elif len(card_list) == 5:  # Flop (2 hole + 3 community)
            discount = 2/3
        elif len(card_list) == 6:  # Turn (2 hole + 4 community)
            discount = 1/2
        else:  # River (2 hole + 5 community) or other cases
            discount = 0
        
        # Kelly Criterion calculation
        # If we bet X and get called, we win pot + X with probability p
        # We lose X with probability (1-p)
        # Kelly fraction = (p*(pot/X) - (1-p)) / (pot/X)
        # Simplified: bet_size = (p*pot - (1-p)*X) / 1
        # Rearranged: bet_size = p*pot - (1-p)*bet_size
        # Solving: bet_size = p*pot / (2-p)
        
        # But we adjust for multiple opponents potentially calling
        # Edge = probability of winning - probability of losing adjusted for opponents
        edge = probability - (1 - probability) / (opponents + 1)
        
        if edge <= 0:
            return 0  # Negative edge, don't bet
        
        # Calculate Kelly bet
        kelly_bet = edge * pot
        
        # Apply street discount (multiply by discount factor)
        # Earlier streets get smaller bets due to future betting rounds
        discounted_bet = kelly_bet * (1 - discount)
        
        return max(0, discounted_bet)  # Never return negative bet
    
    @staticmethod
    def should_call(probability, bet_to_call, pot):
        """
        Determine if we should call a bet based on pot odds
        
        Args:
            probability: Our win probability from Monte Carlo
            bet_to_call: The amount we need to call
            pot: Current pot size (before we call)
        
        Returns:
            Boolean indicating whether to call
        """
        # Pot odds calculation
        # We need to call bet_to_call to win pot + bet_to_call
        # Required equity = bet_to_call / (pot + bet_to_call)
        required_equity = bet_to_call / (pot + bet_to_call)
        
        # Call if our win probability exceeds required equity
        return probability >= required_equity
    
    @staticmethod
    def get_max_call(probability, pot):
        """
        Calculate maximum amount we should be willing to call
        
        Args:
            probability: Our win probability
            pot: Current pot size
        
        Returns:
            Maximum call amount
        """
        # Based on pot odds: if we call X to win pot+X
        # We need probability >= X/(pot+X)
        # Solving for X: X = probability * pot / (1 - probability)
        
        if probability >= 1:
            return float('inf')  # Would call any amount with 100% equity
        
        if probability <= 0:
            return 0  # Don't call with 0% equity
        
        max_call = (probability * pot) / (1 - probability)
        return max(0, max_call)