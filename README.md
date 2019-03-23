# Showdown Poker

This command-line python program generates (5-52 card) poker hands and compares their strengths. The user can specify how many cards are in each hand, as well as how many decks should be generated and hands drawn.

## User Input
There are four options that the user can specify. He can choose, in order of input, how many decks to generate, how many cards will be in each hand, how many players there are (equivalent to amount of hands drawn) and whether or not to show advanced stats.

### Number of decks
The first prompt the user will see is this:
```
How many decks are there? 
```
Any positive integer is valid input, but very large numbers may be too taxing for some machines. An input of 1 generates a standard 52-card, Two to Ace deck without any Jokers or wild cards.
