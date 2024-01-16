import random
# funkcija sukurti kortu kalade
def create_deck():
    # values 2-10 ir + bartukas, karaliene, karalius, tuzas 
    # dar dabar antras variantas, kad susirasome visas kortas kiek ju yra ir kokios jos 
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck
    values = list(range(2,11)) + [10, 10, 10, 11]
    deck = values * 4 
    random.shuffle(deck)
    return deck

# funkcija isdalinti kortas kad jos butu tarp 5 ir 20
def starting_hand(deck):
    while True:
        hand = random.sample(deck, 3)
        total = sum(hand)
        if 5 <= total <=20:
            return hand
        
    
# sukurti kalade
deck = create_deck()

# isdalinti kortas zaidejui ir AI
player_hand = starting_hand(deck)
dealer_hand = starting_hand(deck)

player_hand, dealer_hand

def hit(deck, hand):
    # skaicius nauju kortu kurias prideti: tarp 2 ir 10
    number_of_new_cards = random.randint(2, 10)
    new_cards = random.sample(deck, number_of_new_cards)

    hand.extend(new_cards)
    for card in new_cards:
        dec.remove(card)

    return hand