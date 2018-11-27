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


# Returns the minimum number of stamps (MNS) needed for amount postage, where the stamp
#   denominations are chosen from denom:
# For example, mns(18,(1,6,14)) = 3
@Memoize        
def mns(amount : int, denom : (int)) -> int:
    if amount == 0:
        return 0
    else:
        return 1+min([mns(amount-d,denom) for d in denom if amount-d >= 0])



# Returns the smallest postage requiring the most number of stamps
# That is, if two amounts require the same number of stamps, the smaller will be returned.
def worst(max_amount : int, denom : (int)) -> (int,[int]):
    return max( ((i,mns(i,denom)) for i in irange(1,max_amount)), key = lambda x : x[1])





if __name__ == '__main__':
    denominations = (1,6,14,57)
    amount = prompt.for_int('Enter amount',is_legal = lambda x : x >= 0)
    print('# stamps needed   = ', mns(amount,denominations))
    
    # Table of smallest number of stamps needed for each amount of possage
    for i in irange(1,100):
        print('For postage =',i,' minimum stamps needed =',mns(i,denominations))
    print()
        
    # Largest number of stamps for postage from 1 to 100 cents
    print('The worst postage (1-100) in terms of # of stamps =', worst(100,denominations))