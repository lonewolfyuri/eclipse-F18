from goody import irange
from itertools import product, combinations

# Percentage of time p(...) returns True when called on all the values produced by iterable 
def how_frequent(iterable,p):
    count = 0
    for total,i in enumerate(iterable):
        if p(i):
            count += 1
    return count/total

dice = [1,2,3,4,5,6]

# Print all possible throws of 3 dice
print('All 3-dice throws:', list(product(dice,dice,dice)))
print()

# Print how frequently (.1 means 10%) each possible value of the sum of 3 dice appears
for d_sum in irange(3,18):
    print (d_sum, how_frequent(product(dice,dice,dice), lambda x : sum(x) == d_sum))
print()

suits  = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
values = irange(1,13) # Jack = 11, Queen = 12, King = 13

# Print all possible cards (52) in a deck
print('All cards in a deck:', list(product(values,suits)))
print()

# In the calculations below, at no time do we have a data structure storing all
#   2,598,960 poker; we do generate each of these hands one after another to
#   do something with it (count it; count it if it is a straight flush).

# Print how many 5-card hands can be dealt from a deck
for count,hand in enumerate(combinations(product(values,suits),5),1):
    pass
print('Number of 5-card hands:', count)
print()


# A straight flush is a hand that contains five cards in sequence, all of the same suit.
# Note that because we are representing an ace as 1, the predicate below will not count
#   a royal flush, which is 10, 11, 12, 13, and 1 (considering ace the highest value)

def is_straight_flush(hand):
    suit_count = len( {card[1] for card in hand} )
    values    = {card[0] for card in hand}
    return suit_count == 1 and max(values)-min(values) == 4

print('Likelyhood of a straight flush:',\
      how_frequent(combinations(product(values,suits),5), is_straight_flush) )
