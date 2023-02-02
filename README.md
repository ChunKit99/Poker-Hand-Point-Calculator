
# Poker Hand Point Calculator

The Poker Hand Point Calculation system is a program that calculates the point of a given hand of 5 poker cards. The input hand should be a list of integers where the cards J, Q, K are represented as 10 and A as 1. The input also acceptable character "J", "Q", "K", "A", but other character is not acceptable. The program considers two special rules for the calculation of the point. Firstly, the card value of 3 can be converted to 6 and vice versa. Secondly, if the sum of the 3 selected cards is divisible by 10, then the point is the sum of the remaining 2 cards.

The program also includes a function to convert the J, Q, K, and A card values to 10 and 1 respectively.

Here's an example input and expected result of the program:

```
Input: [4, 7, 10, 6, 2]
Output: ([10, 6, 4], [7, 2])

```

In this example, the three selected cards with the sum divisible by 10 are 10, 6, and 4. The remaining two cards are 7 and 2. Thus, the calculated point is 9 (sum of 7 and 2).

Additionally, the selected cards with the sum divisible by 10 could also be 7, 6, and 10, with the remaining two cards being 4 and 2. But, as this system aims to obtain the highest point, the previous output is the final output.
## Usage/Examples

To use the program, follow these steps:

1. Clone or download the repository.
2. Import the get_max_point functions from the poker.py file.
3. Call the convert_to_point function on your hand of cards, with the hand as a list of strings.

```
from poker import get_max_point

hand = ['4', '7', '10', 'J', '2']
point, selected, remaining = get_max_point(hand)
print("Point:", point)
print("Selected 3 cards:", selected)
print("Remaining 2 cards:", remaining)

```


## Environment Variables

The program is written in **Python 3.7** and uses the **itertools** library.


## Limitation

- Only calculates the point of 5 cards hand.
- Point calculation based on given rules.
- Input hand must be a list of integers, J, Q, K represented as 10 and A as 1.
- No error checking on input hand.
- Output may not be maximized, as the card values of 3 and 6 can be converted to each other.