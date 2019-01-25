"""
In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest
value wins; for example, a pair of eights beats a pair of fives (see example 1
below). But if two ranks tie, for example, both players have a pair of queens,
then highest cards in each hand are compared (see example 4 below); if the
 highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You can
assume that all hands are valid (no invalid characters or repeated cards), each
player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""

# Create individual function to check for the presence of an outcome
def royal_flush(player_1, player_2):
    """
    function that checkks if either player has a royal flush. Return 1 if player
    1 has one, -1 if player 2 wins. 0 if neither or bot players have it.
    """
    result = 0
    player_1_values = []
    player_1_suits = []
    for card in player_1:
        player_1_values.append(card[0])
        player_1_suits.append(card[1])

    player_2_values = []
    player_2_suits = []
    for card in player_2:
        player_2_values.append(card[0])
        player_2_suits.append(card[1])

    if "A" and "K" and "Q" and "J" and "T" in player_1_values:
        if player_1_suits[0] == player_1_suits[1] == player_1_suits[2] == player_1_suits [3] == player_1_suits[4]:
            result += 1
    if "A" and "K" and "Q" and "J" and "T" in player_2_values:
        if player_2_suits[0] == player_2_suits[1] == player_2_suits[2] == player_2_suits [3] == player_2_suits[4]:
            result += -1
    return result

def straight_flush(player_1, player_2):
    """
    function that determines if either player has a straight flush. Return 1
    if player 1 has it, returns -1 if player 2 has it. Returns 0 if both
    or neither players have it. If both players have it, there will be a
    function call to check the high card.

    """

def flush(player_1, player_2):
    """
    function that determines if either player has a flush. Returns 1 if
    player 1 has one, returns -1 if player 2 does. Returns 0 if neither or
    both players have one. It automatically checks the high card if both
    players have a flush and determines a winner.
    """
    result = 0
    player_1_values = []
    player_1_suits = []
    for card in player_1:
        player_1_values.append(card[0])
        player_1_suits.append(card[1])

    player_2_values = []
    player_2_suits = []
    for card in player_2:
        player_2_values.append(card[0])
        player_2_suits.append(card[1])

    if player_1_suits[0] == player_1_suits[1] == player_1_suits[2] == player_1_suits [3] == player_1_suits[4]:
        result += 1
    if player_2_suits[0] == player_2_suits[1] == player_2_suits[2] == player_2_suits [3] == player_2_suits[4]:
        result += -1

    return result

def two_of_a_kind(player_1, player_2):
    """
    function that checks for a two of a kind
    """
    result = 0
    player_1_values = []
    player_1_suits = []
    for card in player_1:
        player_1_values.append(card[0])
        player_1_suits.append(card[1])

    player_2_values = []
    player_2_suits = []
    for card in player_2:
        player_2_values.append(card[0])
        player_2_suits.append(card[1])

    # if len(set(player_1_values)) == 4 and len(set(player_2_values)) == 4:
        # Code to check for number in two of a kind.

    if len(set(player_1_values)) == 4:
        result += 1
    if len(set(player_2_values)) == 4:
        result += -1

    return result

def high_card (player_1, player_2, values):
    result = 0
    player_1_values = []
    player_1_suits = []
    for card in player_1:
        player_1_values.append(card[0])
        player_1_suits.append(card[1])

    player_2_values = []
    player_2_suits = []
    for card in player_2:
        player_2_values.append(card[0])
        player_2_suits.append(card[1])

    player_1_values_new = []
    for value in player_1_values:
        player_1_values_new.append(values.index(value))

    player_2_values_new = []
    for value in player_2_values:
        player_2_values_new.append(values.index(value))

    while len(player_1_values_new) > 0 and result == 0:
        highest_1 = max(player_1_values_new)
        highest_2 = max(player_2_values_new)
        if highest_1 > highest_2:
            result += 1
        elif highest_2 > highest_1:
            result -= 1
        else:
            player_1_values_new.remove(highest_1)
            highest_1 = max(player_1_values_new)
            player_2_values_new.remove(highest_2)
            highest_2 = max(player_2_values_new)

    return result

# First step is to read the file and save its content in a list
values = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
poker_hands = []
filename = "p054_poker.txt"
f = open(filename, "r")
for line in f:
    temp = line.strip('\n').split(' ')
    poker_hands.append(temp)

counter = 0
counters = []
for hand in poker_hands:
    player_1 = hand[:5]
    player_2 = hand[5:]
    # counter += royal_flush(player_1, player_2)
    # counter += flush(player_1, player_2)
    # counter += two_of_a_kind(player_1, player_2)
    counter += high_card(player_1, player_2, values)
    counters.append(counter)
    counters.append(player_1)
    counters.append(player_2)
print(counters)
