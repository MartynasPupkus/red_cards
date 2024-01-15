import random

class Card:
    def __init__(self, rank, suit, weight):
        self.rank = rank
        self.suit = suit
        self.sign = suit + rank
        self.weight = weight

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['spades ', 'clubs ', 'hearts ', 'diamonds ']
        ranks = [' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', ' T', ' J', ' Q', ' K', ' A']
        weights = {' 2': 2, ' 3': 3, ' 4': 4, ' 5': 5, ' 6': 6, ' 7': 7, ' 8': 8, ' 9': 9, ' T': 10, ' J': 11, ' Q': 12, ' K': 13, ' A': 14}

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit, weights[rank]))

    def shuffle(self):
        random.shuffle(self.cards)

    def take_from_top(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            return None

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_to_hand(self, card):
        self.hand.append(card)

    def play_card(self):
        if len(self.hand) > 0:
            return self.hand.pop(0)
        else:
            return None

    def collect_cards(self, cards):
        self.hand.extend(cards)

class AI(Player):
    def __init__(self):
        super().__init__("AI")

    def play_card(self):
        if len(self.hand) > 0:
            return self.hand.pop(0)
        else:
            return None

def display_cards(player, ai):
    print(f"\n{player.name}'s hand: [{' '.join(card.sign for card in player.hand)}]")
    print(f"{ai.name}'s hand: [{' '.join('X' for _ in ai.hand)}]")

def play_round(player, ai, deck):
    player_card = player.play_card()
    ai_card = ai.play_card()

    if player_card is not None:
        print(f"\n{player.name} plays: {player_card.sign}")
    if ai_card is not None:
        print(f"{ai.name} plays: {ai_card.sign}")

    if player_card is not None and ai_card is not None:
        if player_card.weight > ai_card.weight:
            print(f"{player.name} wins the round!")
            player.collect_cards([player_card, ai_card])
        elif ai_card.weight > player_card.weight:
            print(f"{ai.name} wins the round!")
            ai.collect_cards([player_card, ai_card])
        else:
            print("It's a tie!")

def main():
    deck = Deck()
    deck.shuffle()

    player = Player("Player")
    ai = AI()

    for _ in range(26):
        player.add_to_hand(deck.take_from_top())
        ai.add_to_hand(deck.take_from_top())

    while len(player.hand) > 0 and len(ai.hand) > 0:
        display_cards(player, ai)
        input("\nPress Enter to play a round...")

        play_round(player, ai, deck)

    display_cards(player, ai)

    if len(player.hand) > len(ai.hand):
        print("\nPlayer wins!")
    elif len(ai.hand) > len(player.hand):
        print("\nAI wins!")
    else:
        print("\nIt's a TIE!")

if __name__ == "__main__":
    main()