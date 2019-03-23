# Hold'Em Showdown Poker

This command-line python program generates (5-52 card) poker hands and compares their strengths using Texas Hold'Em hand ranking rules. The user can specify how many cards are in each hand, as well as how many decks should be generated and hands drawn.

## User Input
There are four options that the user can specify. He can choose, in order of input, how many decks to generate, how many cards will be in each hand, how many players there are (equivalent to amount of hands that will be drawn) and whether or not to show advanced stats. In order to input a value, the user must enter it into the prompt and then hit enter or return.

### Number of decks
The first prompt the user will see asks how many decks the user wants to generate:
```
How many decks are there? 
```
Any positive integer is valid input, but very large numbers may be too taxing for some machines. An input of 1 generates a one standard 52-card, Two to Ace deck without any Jokers or wild cards.

### Cards per Hand
The second prompt the user will see asks how many cards the user wants to include in each hand:
```
How many cards per hand?
```
Any integer between 5 and 52 (inclusive) is valid input. Since Texas Hold'Em evaluation rules consider the user's best possible five-card combination (this is explained in more depth in the Hand Evaluation Rules section) in order to rank his hand, a hand must contain at least 5 cards. Because each card in a hand must be unique, there can only be 52 cards in each hand, due to the fact that there are only 52 unique cards.

### Number of Players
xxx

### Advanced Stats
xxx (if off just w/l shown, if on ___ shown)

## Hand Evaluation
xxx

### Hold'Em Hand Evaluation Rules
xxx (best 5)

### Holdem Hand Ranking
xxx (1. rf --> 10 hc, kickers)

### Examples
xxx
