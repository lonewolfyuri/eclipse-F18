import prompt
from goody import irange


# Memoize decorator to speed up the smns recursive function
class Memoize:
    def __init__(self,f):
        self.f = f
        self.cache = {}

    def __call__(self,*args):
        if args in self.cache:
            return self.cache[args]
        else:
            answer = self.f(*args)
            self.cache[args] = answer
        return answer

    def reset_cache(self):
        self.cache = {}


# Helper function
# Returns the list in lol whose length is minimum
def min_len(lol : [[]]):
    assert lol != [], "stamps.min_len: no list to compute minimum from"
    return min((len(s),s) for s in lol)[1]


# Returns the minimum length list of stamps whose postage adds up to amount, and each stamp
#   is chosen from denom 
# For example, mns(18,(1,6,14)) = [6, 6, 6]
@Memoize        
def smns(amount:int, denom : (int)) -> [int]:
    if amount == 0:
        return []
    else:
        return min_len([[d]+smns(amount-d, denom) for d in denom if amount-d >= 0])
#         # or, not using min_len
#         from functools import reduce
#         return reduce(lambda x,y: x if len(x) < len(y) else y,[[d]+smns(amount-d, denom) for d in denom if amount-d >= 0])




if __name__ == '__main__':
    denominations = (1,6,14,57)
    amount = prompt.for_int('Enter amount',is_legal = lambda x : x >= 0)
    print('stamps needed   = ', smns(amount,denominations))
    
    # Table of smallest number of stamps needed for each amount of possage
    for i in irange(1,100):
        print('For postage =',i,'stamps needed =',smns(i,denominations))   
    print()