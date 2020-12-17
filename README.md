# Hand Showdown

This command-line python program generates (5-52 card) poker hands and compares their strengths using Texas Hold'Em hand ranking rules. The user can specify how many cards are in each hand, as well as how many decks should be generated and how many hands to draw.

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

An input of 'm', 'mx', 'max' or 'maximum' will generate hands for the maximum amount of players possible.

### Advanced Stats
The final prompt asks the user if he'd like to see advanced stats:
 ```
 Would you like to see advanced stats?
 ```
Any of these inputs is an indication that the user would like to see advanced stats: y, yes, t, true, on, 1. 

Any of these inputs is an indication that the user would not like to see advanced stats: n, no, f, false, off, 0.

If advanced stats are off, only the players with the best and worst hands are shown.

If advanced stats are on, four pieces of information are displayed following the first and last place player:

1. The hand type corresponding to the average hand strength
2. Hand occurence of the ten types of hands
3. The full player ranking
4. Execution time, including total execution time, deck build time, hand build time, and stats calculation time.

Additionally, hand strength, as determined by the program's hand-ranking algorithm, is displayed next to every hand and player ranking. A hand strength of 1 represents the best possible hand, a Royal Flush.

## Hand Evaluation
This section will discuss how hands are ranked. The suits that comprise any specific hand (including flushes and straight flushes, which require five or more cards of the same suit) do not matter, so ties can be present even when using a single deck. In the event of a tie, one hand will be randomly chosen to be the better than the other(s).

### Holdem Hand Ranking from Strongest to Weakest
**1. Royal Flush:**

The strongest straight flush. A-K-Q-J-T all of the same suit constitutes the only royal flush.

**2. Straight Flush:**

Five consecutive cards that are also all of the same suit. Ace can act as the low card to constitute a A-2-3-4-5 straight flush.

**3. Four of a Kind:**

Four cards of the same value.

**4. Full House:**

Three cards of the same value present in conjunction with another two of a different value.

**5. Flush:**

Five cards of the same suit.


**6. Straight:**

Five consecutive cards. Ace can act as the low card to constitute a A-2-3-4-5 straight.

**7. Three of a Kind:**

Three cards of the same value.

**8. Two-Pair:**

Two cards of one value, coupled with another two cards of another value.

**9. Pair:**

Two cards of the same value.

**10. High Card:**

If no other hand is present, the hand containing the highest card(s) wins.


### Hold'Em Hand Evaluation Rules
Hands are evaluated by determining the best 5-card combination that can be made. No combination except for the best one matters when evaluating a hand. If two hands both fall under one hand ranking subset (listed above), the cards' ranks are used to determine the best hand, where 2 is the weakest card and Ace is the strongest. The strongest card that determines the hand ranking subset matters above all others, and if the strongest card is tied the next strongest one is used. If every card that determines a hand ranking subset is of equal rank, the strongest card that does not determine a hand ranking subset is used. If a winner still cannot be determined, the next strongest card will be considered until the weakest card. Only if every value in the best five-card hand from two seperate hands is equal will a tie be present. In the case of an A-5 straight or straight flush (coined 'wheel' and 'steel wheel' respectively), the Ace is considered to be a 1 and the A-5 straight or straight flush loses to all other straights or straight flushes.

### More Resources

* [PokerStars](https://www.pokerstarsschool.com/article/Poker-Hand-Rankings) - Hand Rankings
* [Pokerlistings](https://www.pokerlistings.com/strategy/beginner/how-to-determine-the-winning-hand) - How To Determine the Best Hand
* [Cardplayer](https://www.cardplayer.com/poker-tools/odds-calculator/seven-card-stud) - Seven-Card Stud Calculator
