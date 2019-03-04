import copy
import distutils.core
from enum import Enum
from time import time
from random import randint,shuffle
from math import floor

#STRAIGHTS AND STRAIGHT FLUSHES BROKEN AT THE MOMENT

#Individual Cards
class Card:
	def __init__ (self,value,suit):
		self.value = value
		self.suit = suit
		self.vname = ''
		self.sname = ''

	def vsname(self,value,suit):
		if self.value == 2:
			self.vname = 'Two'
		elif self.value == 3:
			self.vname = 'Three'
		elif self.value == 4:
			self.vname = 'Four'
		elif self.value == 5:
			self.vname = 'Five'
		elif self.value == 6:
			self.vname = 'Six'
		elif self.value == 7:
			self.vname = 'Seven'
		elif self.value == 8:
			self.vname = 'Eight'
		elif self.value == 9:
			self.vname = 'Nine'
		elif self.value == 10:
			self.vname = 'Ten'
		elif self.value == 11:
			self.vname = 'Jack'
		elif self.value == 12:
			self.vname = 'Queen'
		elif self.value == 13:
			self.vname = 'King'
		elif self.value == 14:
			self.vname = 'Ace'

		if self.suit == "Hearts":
			self.sname = '♥'
		elif self.suit == "Spades":
			self.sname = '♠'
		elif self.suit == "Clubs":
			self.sname = '♣'
		elif self.suit == "Diamonds":
			self.sname = '♦'

	def __str__(self):
		return f'{self.sname}{self.vname}{self.sname}'

#All Decks
class Deck:
	def __init__(self):
		self.cards = []
		self.create()

	def create(self):
		for _ in range(decks):
			for val in (2,3,4,5,6,7,8,9,10,11,12,13,14):
				for suit in ("Hearts", "Spades", "Clubs", "Diamonds"):
					self.cards.append(Card(val,suit))
		shuffle(self.cards)

	def draw(self,x):
		for y in range(x):
			drawcards[y] = self.cards.pop()
			drawcards[y].vsname(drawcards[y].value,drawcards[y].suit)

		return drawcards

class BaseStrength(Enum):
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


#Post-Draw
def adv():
	hss = sorted(h_strength.items(), key=lambda k: k[1], reverse=True)
	print(f'\n\n\nPlayer {hss[0][0]+1} has the strongest hand! [{round(hss[0][1]/10000,6)}]\nPlayer {hss[hnumber-1][0] + 1} has the weakest hand :( [{round(hss[hnumber-1][1]/10000,6)}]') if show_strength else print(f'\n\n\nPlayer {hss[0][0] + 1} has the strongest hand!\nPlayer {hss[hnumber-1][0]+1} has the weakest hand :(')
	if show_strength:

		print('\n\n\n\n\nHand Occurence:\n')
		for x in range(10):
			print(ho_names[x],hand_occurence[x],f'({int(round(100*hand_occurence[x]/len(hss),0))}%)')

		print('\n\n\n\n\nFull Player Ranking:\n')
		for x in range(len(hss)):
			print(f'{x+1}.',f'Player {hss[x][0]+1}',f'[{round(hss[x][1]/10000,6)}]')

		print('\n\n\nExecution Time:', "%ss" % (int(round(time()-start_time,2))))



#Determine Values and Suits in Hand
def determine(hand):
	values = []; suits = []; vset = set()
	for x in range(len(hand)):
		values.append(hand[x].value)
		vset.add(hand[x].value)
		suits.append(hand[x].suit)
	return sorted(values,reverse=True),vset,suits

#Message/Text Functions
def ss():
	if show_strength: print(f'[{round(strength/10000,6)}]')
	else: print()

def hnumber(max,msg):
	while True:
		try:
			hn = int(input(msg))
			if hn <= max and hn>0:
				return hn
			else:
				print(f'Please enter an integer between 1 and {max}.')
		except ValueError:
			print('Please enter a positive integer.')

def decks(msg):
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
	while True:
		try:
			d = int(input(msg))
			if d >= 5:
				return d
			else:
				print('Please enter a positive integer greater than 4.')
		except ValueError:
			print('Please enter a positive integer greater than 4.')

def sstrength(msg):
	while True:
		try:
			ss = distutils.util.strtobool(input(msg))
			if ss == 0 or ss == 1:
				return ss
			else:
				print('Please indicate whether you\'d like to show advanced stats')
		except ValueError:
			print('Please indicate whether you\'d like to show advanced stats')

#Evaluation Functions
def valname(x):
	if x == 2:
		return 'Two'
	elif x == 3:
		return 'Three'
	elif x == 4:
		return 'Four'
	elif x == 5:
		return 'Five'
	elif x == 6:
		return 'Six'
	elif x == 7:
		return 'Seven'
	elif x == 8:
		return 'Eight'
	elif x == 9:
		return 'Nine'
	elif x == 10:
		return 'Ten'
	elif x == 11:
		return 'Jack'
	elif x == 12:
		return 'Queen'
	elif x == 13:
		return 'King'
	elif x == 14:
		return 'Ace'

def hcard(values):
	global strength
	strength = BaseStrength.HIGH_CARD.value + 10*values[0] + values[1] + .1*values[2] + .01*values[3] + .001*values[4]
	return f'High-Card {valname(values[0])}'

def numpair(values):
	global strength
	pairs = list(dict.fromkeys([val for val in values if values.count(val) == 2]))
	if len(pairs) < 1:
		return False
	if len(pairs) == 1:
		vp = values.copy()
		for _ in range(2):
			vp.remove(pairs[0])
		strength = BaseStrength.PAIR.value + 10*pairs[0] + vp[0] + .1*vp[1] + .01*vp[2];
		return f'Pair of {valname(pairs[0])}s'
	if len(pairs) >= 2:
		vps = values.copy()
		pairs = sorted(pairs,reverse=True)
		for _ in range(2):
			vps.remove(pairs[0]); vps.remove(pairs[1])
		strength = (BaseStrength.TWO_PAIR.value + 10*int(pairs[0]) + int(pairs[1])) + .1*vps[0]
		return f'{valname(pairs[0])}s and {valname(pairs[1])}s'


def detset(values):
	global strength
	detsets = [val for val in values if values.count(val) == 3]
	if len(detsets) < 1:
		return False
	else:
		vs = values.copy()
		for _ in range(3):
			vs.remove(detsets[0])
		strength = BaseStrength.SET.value + 10*detsets[0] + vs[0] + .1*vs[1]
		return f'Set of {valname(detsets[0])}s'

def straight(vset):
	global strength
	straight = False
	count = 0
	for rank in range(2, 15):
		if rank in vset:
			count += 1
			if count == 5:
				strength = BaseStrength.STRAIGHT.value + 10*min(vset)
				straight = f'Straight'
				#from {valname(min(vset))} to {valname(max(vset))}'
				break
		else: count = 0
	if {14,2,3,4,5} < vset:
		strength = BaseStrength.STRAIGHT.value
		straight = 'Straight from Ace to Five'
	return straight

def flush(values,suits):
	global strength
	flushes = [suit for suit in suits if suits.count(suit) >= 5]
	flushes_vals = sorted([value for value in values if len(flushes) >= 5],reverse=True)
	if len(flushes) < 5:
		flush = False
	else:
		strength = BaseStrength.FLUSH.value + 10*flushes_vals[0] + flushes_vals[1] + .1*flushes_vals[2] + .01*flushes_vals[3] + .001*flushes_vals[4]
		flush = f'{valname(max(values))}-High flush of {flushes[0]}'
	return flush

def fullhouse(values):
	global strength
	pairs = [val for val in values if values.count(val) == 2]
	detsets = [val for val in values if values.count(val) == 3]
	if detset(values) != False and numpair(values) != False:
		strength = BaseStrength.FULL_HOUSE.value + 10*detsets[0] + pairs[0]
		fh = f'{valname(detsets[0])}s full of {valname(pairs[0])}s'
	else:
		fh = False
	return fh

def quads(values):
	global strength
	quads = [val for val in values if values.count(val) == 4]
	if len(quads) < 1:
		return False
	else:
		vq = values.copy()
		for _ in range(4):
			vq.remove(quads[0])
		strength = BaseStrength.QUADS.value + 10*quads[0] + vq[0]
		return f'Quad {valname(quads[0])}s'

def straightflush(values,suit,vset):
	global strength
	straight_ = False
	if straight(vset) != False:
		straight_ = "True"
	if {14,10,11,12,13} < vset:
		straight_ = "Royal"

	flushes = [suit for suit in suits if suits.count(suit) >= 5]
	if len(flushes) < 1:
		flush = False
	else:
		flush = True

	if straight_ == "True" and flush == True:
		strength = BaseStrength.STRAIGHT_FLUSH.value + 10*min(vset)
		sf = f'Straight Flush of {flushes[0]}'
	elif straight_ == "Royal" and flush == True:
		strength = BaseStrength.ROYAL_FLUSH.value
		sf = f'Royal Flush of {flushes[0]}'
	else:
		sf = False
	return sf


#Count Hand Occurence
hand_occurence = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
ho_names = ['High Card: ','Pair: ','Two-Pair: ','Three of a Kind: ','Straight: ','Flush: ','Full House: ','Four of a Kind: ','Straight Flush: ','Royal Flush: ']

drawcards = {}

decks = decks('How many decks are there? ')
x = cph('How many cards per hand? ')
hnumber = hnumber(floor((decks*52)/x), f'How many players are there (max {floor((decks*52)/x)})? ')
show_strength = sstrength("Would you like to show advanced stats? ")

h_strength = {}; start_time = time()
deck = Deck()

for h_inc in range(hnumber):
	print(f"\nPlayer {h_inc + 1}'s hand:")
	user_hand = deck.draw(x)
	values,vset,suits = determine(user_hand)
	print("| ",end="")
	for c_x in user_hand:
		print(user_hand[c_x],end=" | ")

	hcard(values); numpair(values); detset(values); straight(vset); flush(values,suits); fullhouse(values); quads(values); straightflush(values,suits,vset)
	if strength < 2000:
		print('\n'+hcard(values),end=" "); ss()
		hand_occurence[0]+=1
	elif strength < 3000:
		print('\n'+numpair(values),end=" "); ss()
		hand_occurence[1]+=1
	elif strength < 4000:
		print('\n'+numpair(values),end=" "); ss()
		hand_occurence[2]+=1
	elif strength < 5000:
		print('\n'+detset(values),end=" "); ss()
		hand_occurence[3]+=1
	elif strength < 6000:
		print('\n'+straight(vset),end=" "); ss()
		hand_occurence[4]+=1
	elif strength < 7000:
		print('\n'+flush(values,suits),end=" "); ss()
		hand_occurence[5]+=1
	elif strength < 8000:
		print('\n'+fullhouse(values),end=" "); ss()
		hand_occurence[6]+=1
	elif strength < 9000:
		print('\n'+quads(values),end=" "); ss()
		hand_occurence[7]+=1
	elif strength < 10000:
		print('\n'+straightflush(values,suits,vset),end=" "); ss()
		hand_occurence[8]+=1
	elif strength == 10000:
		print('\n'+straightflush(values,suits,vset),end=" "); ss()
		hand_occurence[9]+=1

	h_strength[h_inc] = strength

adv()
