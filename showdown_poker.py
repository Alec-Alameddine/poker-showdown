import distutils.core
from math import floor
from random import shuffle, randint, choice
from enum import Enum
from time import time

DEBUG = False


class Card:
    """A class containing the value and suit for each card"""
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.vname = value_names[value]
        self.sname = suit_names[suit]

    def __str__(self):
        """Pretty-prints each card"""
        return f'{self.sname}{self.vname}{self.sname}'

    def __repr__(self):
        """Represents each card in two characters"""
        if self.value == 0:
            return '__'
        elif 0 < self.value < 10:
            return f'{self.value}{self.suit[0].lower()}'
        elif self.value >= 10:
            return f'{self.vname[0]}{self.suit[0].lower()}'

    def __eq__(self, other_card):
        """Returns True if the value and suit for two cards are equal"""
        if not isinstance(other_card, self.__class__):
            return False

        return self.value == other_card.value and self.suit == other_card.suit

    def __ne__(self,other_card):
        """Returns False if the value and suit for two cards are equal"""
        return not self == other_card

    def __hash__(self):
        """Defines card object hashing for the purpose of comparing equality"""
        return hash((self.value, self.suit))


class Deck:
    """A class containing all of the cards that can be drawn as part of a hand"""
    def __init__(self):
        self.cards = []
        self.create()

    def create(self):
        """Generate all of the cards"""
        for _ in range(decks):
            for val in (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14):
                for suit in ("Hearts", "Spades", "Clubs", "Diamonds"):
                    self.cards.append(Card(val, suit))
        shuffle(self.cards)

    def draw(self, c):
        """Generate a hand of c unique cards"""
        card = 0
        while card < c:
            if self.cards[-1] not in drawcards.values():
                drawcards[card] = self.cards.pop()
                card += 1
            else:
                if len(self.cards) <= 520 and len(drawcards) <= 520:
                    s = set(list(drawcards.values()) + self.cards)
                    if s:
                        for x in self.cards:
                            if x not in drawcards.values():
                                drawcards[card] = x
                                break
                        self.cards.remove(drawcards[card])
                        card += 1
                    else:
                        drawcards[card] = Card(0,0)
                        card += 1
                else:
                    i = randint(0, (len(self.cards) - 1))
                    self.cards[i], self.cards[-1] = self.cards[-1], self.cards[i]

        return drawcards


class BaseStrength(Enum):
    """The minimum strength value for each type of hand"""
    ROYAL_FLUSH = 10000
    STRAIGHT_FLUSH = 9000
    QUADS = 8000
    FULL_HOUSE = 7000
    FLUSH = 6000
    STRAIGHT = 5000
    SET = 4000
    TWO_PAIR = 3000
    PAIR = 2000
    HIGH_CARD = 1000


class HandTypeEvaluation:
    """Contains functions that determine the name of and assign strength values to each hand."""

    def __init__(self):
        HandTypeEvaluation.strength = 0

    @classmethod
    def h_card(cls, values):
        """Returns the name of a high-card hand (string) given a list of the hand's card values.
        Also changes hand strength accordingly."""
        cls.strength = BaseStrength.HIGH_CARD.value + 60*values[0] + 6*values[1] + .6*values[2] + .06*values[3] + .006*values[4]
        return f'High-Card {value_names[values[0]]}'

    @classmethod
    def num_pair(cls, values):
        """Returns the name of a one-pair or two-pair hand (string) given a list of the hand's card values.
        Returns False if one-pair or two-pair is not present within the hand. Also changes hand strength accordingly."""
        pairs = list(dict.fromkeys([val for val in values if values.count(val) == 2]))

        if not pairs:
            return False

        if len(pairs) == 1:
            vp = values.copy()
            for _ in range(2):
                vp.remove(pairs[0])
            cls.strength = BaseStrength.PAIR.value + 60*pairs[0] + 6*vp[0] + .6*vp[1] + .06*vp[2]

            return f'Pair of {value_names_plural[pairs[0]]}s'

        if len(pairs) >= 2:
            vps = values.copy()
            pairs = sorted(pairs, reverse=True)
            for _ in range(2):
                vps.remove(pairs[0]); vps.remove(pairs[1])
            cls.strength = BaseStrength.TWO_PAIR.value + 60*pairs[0] + 6*pairs[1] + .6*vps[0]

            return f'{value_names_plural[pairs[0]]}s and {value_names_plural[pairs[1]]}s'

    @classmethod
    def trip(cls, values):
        """Returns the name of a three-of-a-kind hand (string) given a list of the hand's card values.
        Returns False if a set is not present within the hand. Also changes hand strength accordingly."""
        trips = [val for val in values if values.count(val) == 3]
        if not trips:
            return False
        else:
            trips = max(trips)
            vs = values.copy()
            for _ in range(3):
                vs.remove(trips)
            cls.strength = BaseStrength.SET.value + 60*trips + 6*vs[0] + .6*vs[1]

            return f'Set of {value_names_plural[trips]}s'

    @classmethod
    def straight(cls, vset, get_vals=False):
        """Returns the name of a straight hand (string) given a set of the hand's card values.
        Returns False if a straight is not present within the hand. Also changes hand strength accordingly.
        If get_vals is true, straight() does not change strength and returns the values present in a straight."""
        count = 0

        if not get_vals:
            straight = False
            for rank in reversed([14, *range(2, 15)]):
                if rank in vset:
                    count += 1
                    min_c = rank
                    if count == 5:
                        if min_c != 14:
                            max_c = min_c + 4
                        else:
                            min_c, max_c = 1, 5
                        cls.strength = BaseStrength.STRAIGHT.value + 70*max_c
                        straight = f'Straight from {value_names[min_c]} to {value_names[max_c]}'
                        break
                else: count = 0
            return straight

        if get_vals:
            sset = set()
            for rank in reversed([14, *range(2, 15)]):
                if rank in vset:
                    count += 1
                    sset.add(rank)
                    if count == 5:
                        return sset
                else:
                    count = 0
                    sset = set()
            raise Exception('No SSET')

    @classmethod
    def flush(cls, suits, all_cards):
        """Returns the name of a flush hand (string) given a list of the hand's card suits and a list of all the cards
        in the hand. Returns False if a flush is not present within the hand. Also changes hand strength accordingly."""
        flushes = [suit for suit in suits if suits.count(suit) >= 5]
        if flushes: flushes_vals = sorted([card.value for card in all_cards if card.suit == flushes[0]], reverse=True)
        if not flushes:
            return False
        else:
            cls.strength = BaseStrength.FLUSH.value + 60*flushes_vals[0] + 6*flushes_vals[1] + .6*flushes_vals[2] + \
                       .06*flushes_vals[3] + .006*flushes_vals[4]
            flush = f'{value_names[max(flushes_vals)]}-High flush of {flushes[0]}'

        return flush

    @classmethod
    def full_house(cls, values):
        """Returns the name of a filled up (string) hand given a list of the hand's card values.
        Returns False if a full house is not present within the hand. Also changes hand strength accordingly."""
        trips = list(dict.fromkeys(sorted([val for val in values if values.count(val) == 3], reverse=True)))
        pairs = sorted([val for val in values if values.count(val) == 2], reverse=True)

        if not trips or (len(trips) == 1 and not pairs):
            return False

        if pairs:
            cls.strength = BaseStrength.FULL_HOUSE.value + 60*trips[0] + 6*pairs[0]
            fh = f'{value_names_plural[trips[0]]}s full of {value_names_plural[pairs[0]]}s'

        if len(trips) > 1:
            if pairs:
                if trips[1] > pairs[0]:
                    cls.strength = BaseStrength.FULL_HOUSE.value + 60*trips[0] + 6*trips[1]
                    fh = f'{value_names_plural[trips[0]]}s full of {value_names_plural[trips[1]]}s'
            else:
                cls.strength = BaseStrength.FULL_HOUSE.value + 60*trips[0] + 6*trips[1]
                fh = f'{value_names_plural[trips[0]]}s full of {value_names_plural[trips[1]]}s'

        return fh

    @classmethod
    def quads(cls, values):
        """Returns the name of a four-of-a-kind hand (string) given a list of the hand's card values.
        Returns False if quads are not present within the hand. Also changes hand strength accordingly."""
        quads = [val for val in values if values.count(val) >= 4]
        if not quads:
            return False
        else:
            quads = max(quads)
            vq = values.copy()
            for _ in range(4): vq.remove(quads)
            cls.strength = BaseStrength.QUADS.value + 60*quads + 6*vq[0]

            return f'Quad {value_names_plural[quads]}s'

    @classmethod
    def straight_flush(cls, suits, all_cards):
        """Returns the name of a straight or royal flush hand (string) given a list of the hand's card suits,
        a set of the hand's card values, and a list of all the cards in the hand. Returns False if a straight or royal
        flush is not present within the hand. Also changes hand strength accordingly."""
        straight_: str = None

        flushes = [suit for suit in suits if suits.count(suit) >= 5]
        if flushes:
            flushes_vals = sorted([card.value for card in all_cards if card.suit == flushes[0]], reverse=True)

            if HandTypeEvaluation.straight(flushes_vals):
                straight_vals = HandTypeEvaluation.straight(flushes_vals, True)
                if {14, 10, 11, 12, 13} <= straight_vals: straight_ = "Royal"
                elif {14, 2, 3, 4, 5} <= straight_vals: straight_ = "Wheel"
                else: straight_ = "Normal"

        if straight_ == "Normal":
            cls.strength = BaseStrength.STRAIGHT_FLUSH.value + 70*max(flushes_vals)
            sf = f'{value_names[max(straight_vals)]}-High Straight Flush of {flushes[0]}'
        elif straight_ == "Wheel":
            cls.strength = BaseStrength.STRAIGHT_FLUSH.value
            sf = f'Five-High Straight Flush of {flushes[0]}'
        elif straight_ == "Royal":
            cls.strength = BaseStrength.ROYAL_FLUSH.value
            sf = f'Royal Flush of {flushes[0]}'
        else:
            return False

        return sf

    @staticmethod
    def evalhand(values, suits, vset, all_cards):
        """Returns the exact type of hand (string) that is present given a list of values and suits within the hand,
        a set of values within the hand, and a list of all the cards in the hand"""
        x = HandTypeEvaluation.straight_flush(suits, all_cards)
        if not x: x = HandTypeEvaluation.quads(values)
        if not x: x = HandTypeEvaluation.full_house(values)
        if not x: x = HandTypeEvaluation.flush(suits, all_cards)
        if not x: x = HandTypeEvaluation.straight(vset)
        if not x: x = HandTypeEvaluation.trip(values)
        if not x: x = HandTypeEvaluation.num_pair(values)
        if not x: x = HandTypeEvaluation.h_card(values)

        return x


def determine(hand):
    """Returns a list of values, a set of values, a list of suits, and a list of cards within a hand."""
    values, vset, suits, all_cards = [], set(), [], []
    for x in range(len(hand)):
        values.append(hand[x].value)
        vset.add(hand[x].value)
        suits.append(hand[x].suit)
        all_cards.append(hand[x])
    return sorted(values, reverse=True), vset, suits, all_cards


# Message/Text Functions

def ss():
    """Prints hand strength if advanced stats are on"""
    if show_strength_: print(f'[{round(HandTypeEvaluation.strength / 10000, 6)}]')
    else: print()


def hnumber(max_v, msg):
    """Returns the number of hands (int) to be generated given the maximum hands that can be generated"""
    while True:
        try:
            hn = input(msg)
            if hn.lower() == 'm' or hn.lower() == 'max':
                return max_v
            elif 0 < int(hn) <= max_v:
                return int(hn)
            else:
                print(f'Please enter an integer between 1 and {max_v}.')
        except ValueError:
            print('Please enter a positive integer.')


def decks(msg):
    """Returns the number of decks (int) to be generated"""
    while True:
        try:
            d = int(input(msg))
            if d > 0:
                return d
            else:
                print('Please enter a positive integer.')
        except ValueError:
            print('Please enter a positive integer.')


def cph(msg):
    """Returns the number of cards (int) to be included in each hand"""
    while True:
        try:
            d = int(input(msg))
            if 5 <= d <= 52:
                return d
            else:
                print('Please enter a positive integer between 5 and 52.')
        except ValueError:
            print('Please enter a positive integer between 5 and 52.')


def show_strength(msg):
    """Returns a boolean indicating whether advanced stats are shown"""
    while True:
        try:
            ss = distutils.util.strtobool(input(msg))
            if ss == 0 or ss == 1:
                return ss
            else:
                print('Please indicate whether you\'d like to see advanced stats')
        except ValueError:
            print('Please indicate whether you\'d like to see advanced stats')


def get_inputs():
    """Returns the integer outputs of decks(), cph(), hnumber() and the boolean output of show_strength()"""
    decks_ = decks('How many decks are there? ')
    cph_ = cph('How many cards per hand? ')
    max_v = floor((decks_*52)/cph_)
    hnumber_ = hnumber(max_v, f'How many players are there (max {floor((decks_*52)/cph_)})? ')
    sstrength_ = show_strength("Would you like to see advanced stats? ")

    return decks_, cph_, hnumber_, sstrength_


def print_hand(user_hand, h_inc):
    """Pretty-prints a single hand"""
    print(f"\nPlayer {h_inc + 1}'s hand:")
    print("| ", end="")
    if DEBUG:
        for c_x in user_hand: print(repr(user_hand[c_x]), end=" | ")
        if sorted(list(set(user_hand))) != sorted(user_hand):
            print("DUPLICATE", end="")
    else:
        for c_x in user_hand: print(user_hand[c_x], end=" | ")


def post_draw():
    """Displays various stats if advanced stats are on
    and displays the strongest and weakest hand if advanced stats are off"""
    hss = sorted(h_strength.items(), key=lambda k: k[1], reverse=True)

    if not show_strength_:
        print(f'\n\n\nPlayer {hss[0][0] + 1} has the strongest hand!')
        print(f'Player {hss[hnumber-1][0]+1} has the weakest hand :(')

    if show_strength_:

        print(f'\n\n\nPlayer {hss[0][0] + 1} has the strongest hand! [{round(hss[0][1]/10000, 6)}]')
        print(f'Player {hss[hnumber-1][0]+1} has the weakest hand :( [{round(hss[hnumber-1][1]/10000, 6)}]')

        print('\n\n\n\n\nHand Occurrence:\n')
        for x in range(10): print(ho_names[x], hand_occurrence[x], f'({round(100*hand_occurrence[x]/len(hss), 2)}%)')

        print('\n\n\n\n\nFull Player Ranking:\n')
        for x in range(len(hss)): print(f'{x+1}.', f'Player {hss[x][0]+1}', f'[{round(hss[x][1]/10000, 6)}]')

        print('\n\n\nComplete Execution Time:', "~%ss" % (round(time()-deck_start_time, 2)))
        print('Deck Build Time:', '~%ss' % (round(deck_end_time-deck_start_time, 2)),
              f'({int(round(100*(deck_end_time-deck_start_time)/(time()-deck_start_time), 0))}%)')
        print('Hand Build Time:', '~%ss' % (round(time()-deck_end_time, 2)),
              f'({int(round(100*(time()-deck_end_time)/(time()-deck_start_time), 0))}%)')


def showdown_poker():  # Main Function
    for h_inc in range(hnumber):
        user_hand = deck.draw(cards_per_hand)
        print_hand(user_hand, h_inc)

        values, vset, suits, all_cards = determine(user_hand)
        exact_hand = HandTypeEvaluation.evalhand(values, suits, vset, all_cards)
        print('\n'+exact_hand, end=" "); ss()

        hand_occurrence[floor(HandTypeEvaluation.strength/1000-1)] += 1
        h_strength[h_inc] = HandTypeEvaluation.strength

    post_draw()


ho_names = ('High Card: ', 'Pair: ', 'Two-Pair: ', 'Three of a Kind: ', 'Straight: ', 'Flush: ', 'Full House: ',
            'Four of a Kind: ', 'Straight Flush: ', 'Royal Flush: ')
hand_occurrence = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

value_names = {1: 'Ace', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
               10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace', 0: 'EMPTY'}
value_names_plural = {1: 'Ace', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Sixe', 7: 'Seven', 8: 'Eight',
                      9: 'Nine', 10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}
suit_names = {"Hearts": '♥', "Spades": '♠', "Clubs": '♣', "Diamonds": '♦', 0: ''}

drawcards, h_strength = {}, {}

decks, cards_per_hand, hnumber, show_strength_ = get_inputs()
deck_start_time = time()

deck = Deck()
deck_end_time = time()


if __name__ == '__main__':
    showdown_poker()
