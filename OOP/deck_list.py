import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    item = 0

    def __init__(self):
        self._card = (Card(rank, suit) for suit in self.suits for rank in self.ranks)

    #def __len__(self):
    #    return len(self._card)

    #def __getitem__(self, position):
    #    return self._card[position]

    def __iter__(self):
        return self

    def __next__(self):
        self.item += 1
        return self._card


deck = FrenchDeck()
iter_deck = iter(deck)

def func():
    for value in deck.__dict__.values():
        for item in value:
            yield item


if __name__ == '__main__':

    for i in iter_deck:
        print(i)


