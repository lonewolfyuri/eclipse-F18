# Tracking (counting) function calls as decorator class/function

class Track_Calls:
    def __init__(self,f):
        self.f = f
        self.calls = 0
    
    def __call__(self,*args,**kargs):  # bundle arbitrary arguments
        self.calls += 1
        return self.f(*args,**kargs)   # unbundle arbitrary arguments

    def called(self):
        return self.calls
    
    def reset_calls(self):
        self.calls = 0

    def __getattr__(self,attr):        # if attr not here, try self.f
        return getattr(self.f,attr)
    

# Memoizing function calls as decorator class/function

class Memoize:
    def __init__(self,f):
        self.f = f
        self.cache = {}
        
    def __call__(self,*args):
        print('called with',*args,'calls is',self.calls)
        if args in self.cache:
            return self.cache[args]
        else:
            answer = self.f(*args)
            self.cache[args] = answer
        return answer

    def reset_cache(self):
        self.cache = {}
        
    def __getattr__(self,attr):        # if attr not here, try self.f
        return getattr(self.f,attr)





if __name__ == '__main__':
    from goody import irange
    
    @Memoize
    @Track_Calls
    def fib(n):
        if    n == 0: return 1
        elif  n == 1: return 1
        else:         return fib(n-1) + fib(n-2)
    
    print('\nTracking calls for recursive fib(onacci) with Memoizing')    
    for i in irange(0,5): 
            fib.reset_calls()  # if Track_Calls decorator
            fib.reset_cache()  # if Memoize decorator
            print('  Fib('+str(i)+') =', fib(i), 'and # calls for fib('+str(i)+') =', fib.called())
