class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cards = [Card(value, suit) for suit in suits for value in values]
        print(self.cards)

    def __repr__(self):
        return f"deck of {self.count()} values"

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        actual = min([count, num])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def deal_card(self):
        return self.deal(1)[0]

    def deal_hand(self,hand_size):
        return self._deal(hand_size)

d = Deck()
print(d._deal(52))
print(d.count())
print(d._deal(3))