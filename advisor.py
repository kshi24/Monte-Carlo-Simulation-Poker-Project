class Advisor:
    @staticmethod    
    def bet(probability, pot, opponents, card_list):
        if len(card_list) == 2:  # Pre-flop (2 hole cards)
            discount = 5/6
        elif len(card_list) == 5:  # Flop (2 hole + 3 community)
            discount = 2/3
        elif len(card_list) == 6:  # Turn (2 hole + 4 community)
            discount = 1/2
        else:  # River (2 hole + 5 community) or other cases
            discount = 0
        # Kelly's criterion assuming that only 1 person calls your bet
        # Also restricts pot sizing based on the street due to 
        return (2 * probability - ((1 - probability) / (opponents + 1))) * pot / (1 - discount)
   
    @staticmethod
    def decision(probability, bet, pot, opponents, card_list):
        if probability > 0.50:
            bet_amount = bet(probability, pot, opponents, card_list)
            print(f"Raise bet to: ${bet_amount:.2f}")
        else: 
            max_call = (pot * probability)
            print(f"Call until ${max_call:.2f}, otherwise fold")