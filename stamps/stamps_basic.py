import prompt
from goody import irange

# Returns the minimum number of stamps (MNS) needed for amount postage, where the stamp
#   denominations are chosen from denom:
# For example, mns(18,(1,6,14)) = 3
def mns(amount : int, denom : (int)) -> int:
    if amount == 0:
        return 0
    else:
        return 1+min([mns(amount-d,denom) for d in denom if amount-d >= 0])



if __name__ == '__main__':
    denominations = (1,6,14,57)
    amount = prompt.for_int('Enter amount',is_legal = lambda x : x >= 0)
    print('# stamps needed = ',  mns(amount,denominations))
    
    # Table of smallest number of stamps needed for each amount of postage
    # At a certain point, printing this table becomes very slow
    for i in irange(1,100):
        print('For postage =',i,' minimum stamps needed =',mns(i,denominations))