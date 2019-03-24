# Stud Showdown

This command-line python program generates (5-52 card) poker hands and compares their strengths using Texas Hold'Em hand ranking rules. The user can specify how many cards are in each hand, as well as how many decks should be generated and hands drawn. The program mimics an N-card Stud game, where N is the number of cards per hand.

## User Input
There are four options that the user can specify. He can choose, in order of input, how many decks to generate, how many cards will be in each hand, how many players there are (equivalent to amount of hands that will be drawn) and whether or not to show advanced stats. In order to input a value, the user must enter it into the prompt and then hit enter or return.

### Number of decks
The first prompt asks how many decks the user wants to generate:
```
How many decks are there? 
```
Any positive integer is valid input, but very large numbers may be too taxing for some machines. An input of 1 generates a one standard 52-card, Two to Ace deck without any Jokers or wild cards.

### Cards per Hand
The second prompt asks the user how many cards he wants to include in each hand:
```
How many cards per hand?
```
Any integer between 5 and 52 (inclusive) is valid input. Since Texas Hold'Em evaluation rules consider the user's best possible five-card combination (this is explained in more depth in the Hand Evaluation Rules section) in order to rank his hand, a hand must contain at least 5 cards. Because each card in a hand must be unique, there can only be 52 cards in each hand, due to the fact that there are only 52 unique cards.

### Number of Players
The third prompt asks the user how many players he wants to generate hands for:
```
How many players are there (max __)?
```

The maximum input is dependent on the amount of cards per hand and also the amount of decks generated. The minimum input is 1. Any integer between 1 and the maximum value (inclusive), which will be displayed in the prompt, is valid. 

### Advanced Stats
The final prompt asks the user if he'd like to see advanced stats:
 ```
 Would you like to see advanced stats?
 ```
Any of these inputs is an indication that the user would like to see advanced stats: y, yes, t, true, on, 1. 

Any of these inputs is an indication that the user would not like to see advanced stats: n, no, f, false, off, 0.

If advanced stats are off, only the players with the best and worst hands are shown.

If advanced stats are on, three pieces of information are displayed following the first and last place player:


1. Hand occurence of the ten types of hands
2. The full player ranking
3. Execution time, including total execution time, deck build time, and hand build time.

Additionally, hand strength, as determined by the program's hand-ranking algorithm, is displayed next to every hand and player ranking. A hand strength of 1 represents the best possible hand, a Royal Flush.

## Hand Evaluation
xxx

### Hold'Em Hand Evaluation Rules
xxx (best 5)

### Holdem Hand Ranking
xxx (1. rf --> 10 hc, kickers)

### Examples
xxx

### More Resources

* [PokerStars](https://www.pokerstarsschool.com/article/Poker-Hand-Rankings) - Hand rankings
* [Pokerlistings](https://www.pokerlistings.com/strategy/beginner/how-to-determine-the-winning-hand) - How to determine the best hand
* [Cardplayer](https://www.cardplayer.com/poker-tools/odds-calculator/seven-card-stud) - Seven-Card Stud Calculator
