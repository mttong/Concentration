class Card:

    SUITS = ["♣", "♦", "♥", "♠"]
    RANK = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} \n {self.suit}'

    def __eq__(self, other):
        return self.rank == other.rank and self.same_color(other)

    def same_color(self, other):
        if self.suit == "♦" or self.suit == "♥":
            return other.suit == "♦" or other.suit == "♥"
        elif self.suit == "♣" or self.suit == "♠":
            return other.suit == "♣" or other.suit == "♠"
        else:
            return False
