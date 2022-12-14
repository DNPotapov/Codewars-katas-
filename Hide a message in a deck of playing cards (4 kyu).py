"""
Hide a message in a deck of playing cards (4 kyu)
https://www.codewars.com//kata/59b9a92a6236547247000110
"""

from math import factorial as fac
cards = [
    "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "TC", "JC", "QC", "KC",
    "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "TD", "JD", "QD", "KD",
    "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "TH", "JH", "QH", "KH",
    "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "TS", "JS", "QS", "KS"
]
symbols = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols_len = len(symbols)
facs = [1]
for x in range(1, 53, 1):
    facs.append(facs[-1] * x)

class PlayingCards:

    def encode(self, message):
        mess_len = len(message)
        rem = 0
        for i in range(mess_len):
            if message[i] not in symbols: return None
            rem = rem + symbols_len ** (mess_len - i - 1) * symbols.index(message[i])
        if rem >= facs[-1]: return None
        for i in range(1, 53):
            if rem < facs[i]: break
        remaining_cards = cards[53 - i - 1:]
        cards_o = cards[:53 - i - 1]
        for j in range(i - 1, -1, -1):
            idx = rem // facs[j]
            cards_o.append(remaining_cards.pop(idx))
            rem = rem % facs[j]
        return cards_o

    def decode(self, deck):
        if len(deck) != 52: return None
        remaining_cards = cards.copy()
        rem = 0
        for i in range(len(deck)):
            if deck[i] not in remaining_cards: return None
            idx = remaining_cards.index(deck[i])
            rem = rem + facs[51 - i] * idx
            remaining_cards.pop(idx)
        res = []

        if rem == 0 :
            return ''

        while rem > 0:
            res.insert(0, symbols[rem % symbols_len])
            rem = rem // symbols_len

        return ''.join(res)