import random

class Card:
    def __init__(self, rank, suit, weight):
        self.rank = rank
        self.suit = suit
        self.sign = suit + rank
        self.weight = weight.calculate_weight

    def calculate_weight(self):
        if self.rank.isdigit():
            return int(self.rank)
        elif self.rank == "A":
            return 14
        else:
            return 13 


class Deck:
    def __init__(self):
        self.cards = []
        suits = ['spades', 'clubs', 'hearts', 'diamonds']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        weight = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

        for suit in suits:
            for rank in ranks:
                for weight in weight:
                    self.cards.append(Card(rank, suit, weight))

    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def take_from_top(self):
        return self.cards.pop() if self.cards else None
    
    def take_from_bottom(self):
        return self.cards.pop(0) if self.cards else None
    
    def take_random(self):
        return random.choice(self.cards) if self.cards else None
    

class Player:
    def __init__(self):
        self.hand = []

    def add_to_hand(self, card):
        self.hand.append(card)

class AI(Player):
    def play_card(self):
        return self.hand.pop(0) if self.hand else None
    
def play_ward_game():
    deck = Deck()
    deck.shuffle()

    player = Player()
    ai = AI()

    for _ in range(26):
        player.add_to_hand(deck.take_from_top())
        ai.add_to_hand(deck.take_from_top())

    while True:
        player_card = player.add_to_hand(deck.take_from_bottom())
        ai_card = ai.add_to_hand(deck.take_from_top())

        if player_card is None or ai_card is None:
            break

        print(f'Cheater: {player_card.sign} vs AI: {ai_card.sign}')

        if player_card.weight > ai_card.weight:
            player.add_to_hand(player_card)
            player_card.add_to_hand(ai_card)
        elif ai_card.weight > player_card.weight:
            ai.add_to_hand(player_card)
            ai.add_to_hand(ai_card)

    if len(player.hand) > len(ai.hand):
        print('Cheater wins!')
    elif len(ai.hand) > len(player.hand):
        print('AI wins!')
    else:
        print('Its a tie')

if __name__ == '__main__':
    play_war_game()
    