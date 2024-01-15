import random

def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

# Function to deal initial cards ensuring total is between 5 and 20
def starting_hand(deck):
    while True:
        hand = random.sample(deck, 3)
        total = sum(hand)
        if 5 <= total <= 20:
            return hand

# Create the deck        
deck = create_deck()

# Deal cards to player and dealer/AI
player_hand = starting_hand(deck)
dealer_hand = starting_hand(deck)

player_hand, dealer_hand

def hit(deck, hand):
    # Number of new cards to add: Between 2 and 10
    num_of_new_cards = random.randint(2, 10)
    new_cards = random.sample(deck, num_of_new_cards)

    hand.extend(new_cards)
    for card in new_cards:
         deck.remove(card)

    return hand