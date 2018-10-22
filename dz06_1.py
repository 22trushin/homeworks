import random as random_number


class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.name = self.rank + self.suit

    def __str__(self):
        rep = self.name
        return rep


class PlayerHand(object):

    def __init__(self):
        self.cards = []
        self.max_cards = 5

    def __getitem__(self, item):
        return self.cards[item]

    def clear(self):
        self.cards = []

    def add(self, card):
        if len(self.cards) <= self.max_cards:
            self.cards.append(card)
        else:
            print('В руке максимальное число карт')


class DeckOfCards(object):
    def __init__(self):
        ranks = ['A', '2', '3', '4', '5', '6', '7',
                 '8', '9', '10', 'J', 'Q', 'K']
        suits = ['C', 'D', 'H', 'S']
        self.deck = [Card(rank=r, suit=s) for s in suits for r in ranks]
        random_number.shuffle(self.deck)

    def razdacha(self, n=5):
        hand = [self.deck[i] for i in range(n)]  # pick cards
        del self.deck[:n]  # remove cards
        return hand


player1_hand = PlayerHand()
player2_hand = PlayerHand()
new_deck = DeckOfCards()
print('Карты в начальной колоде: ', end='')
for item in new_deck.deck:
    print(item, end=' ')
player1_hand.add(new_deck.razdacha())
player2_hand.add(new_deck.razdacha())
print()
print('Карты на руке первого игрока: ', end='')
for obj in player1_hand.cards:
    for item in obj:
        print(item, end=' ')
print()
print('Карты на руке второго игрока: ', end='')
for obj in player2_hand.cards:
    for item in obj:
        print(item, end=' ')
print()
print('Карты в колоде после раздачи: ', end='')
for item in new_deck.deck:
    print(item, end=' ')


