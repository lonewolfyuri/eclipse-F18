import prompt
from goody import irange


# Helper function
# Returns the list in lol whose length is minimum
def min_len(lol : [[]]):
    assert lol != [], "stamps.min_len: no list to compute minimum from"
    return min((len(s),s) for s in lol)[1]


# Returns the minimum length list of stamps whose postage adds up to amount, and each stamp
#   is chosen from denom 
# For example, mns(18,(1,6,14)) = [6, 6, 6]
def smns(amount:int, denom : (int)) -> [int]:
    if amount == 0:
        return []
    else:
        return min_len([[d]+smns(amount-d, denom) for d in denom if amount-d >= 0])
#         # or, not using min_len
#         from functools import reduce
#         return reduce(lambda x,y: x if len(x) < len(y) else y,[[d]+smns(amount-d, denom) for d in denom if amount-d >= 0])


# Returns the smallest postage requiring the most number of stamps
# That is, if two amounts require the same number of stamps, the smaller will be returned.
def worst(max_amount : int, denom : (int)) -> (int,[int]):
    def max_len(lol : [[]]):
        return max((len(s),-sum(s),s) for s in lol)[2]
    worst = max_len(smns(i,denominations) for i in irange(1,max_amount))
    return (sum(worst),worst)





if __name__ == '__main__':
    denominations = (1,6,14,57)
    amount = prompt.for_int('Enter amount',is_legal = lambda x : x >= 0)
    print('stamps needed   = ', smns(amount,denominations))
    
    # Table of smallest number of stamps needed for each amount of postage
    # At a certain point, printing this table becomes very slow
    for i in range(1,100):
        print('for',i,'stamps needed = ',smns(i,denominations))
    
    # Largest number of stamps for postage from 1 to 100 cents
    # This function is likely to take too long to executes
    print(worst(100,denominations))