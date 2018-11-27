# Memoizing function calls as decorator class/function

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
        
    def __getattr__(self,attr):        # if attr not here, try self.f
        return getattr(self.f,attr)





if __name__ == '__main__':
    from goody import irange
    
    @Memoize
    def fib(n):
        if    n == 0: return 1
        elif  n == 1: return 1
        else:         return fib(n-1) + fib(n-2)
    
    print('\nacking calls for recursive fib(onacci)')    
    for i in irange(0,50): 
            fib.reset_cache()  # if Memoize decorator
            print('  Fib('+str(i)+') =', fib(i))