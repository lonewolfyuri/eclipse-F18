# Illustrating the recursive structure (calls/returns) of recursive functions

class Illustrate_Recursive:
    def __init__(self,f):
        self.f = f
        self.trace = False
        
    def illustrate(self,*args,**kargs):
        self.indent = 0
        self.trace = True
        answer = self.__call__(*args,**kargs)
        self.trace = False
        return answer
    
    def __call__(self,*args,**kargs):
        if self.trace:
            if self.indent == 0:
                print('Starting recursive illustration'+30*'-')
            print (self.indent*"."+"calling", self.f.__name__+str(args)+str(kargs))
            self.indent += 2
        answer = self.f(*args,**kargs)
        if self.trace:
            self.indent -= 2
            print (self.indent*"."+self.f.__name__+str(args)+str(kargs)+" returns", answer)
            if self.indent == 0:
                print('Ending recursive illustration'+30*'-')
        return answer

    def __getattr__(self,attr):        # if attr not here, try self.f
        return getattr(self.f,attr)





if __name__ == '__main__':
    from goody import irange
    
    @Illustrate_Recursive
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n*factorial(n-1)
    
    print('Illustrating recursive factorial')    
    factorial.illustrate(5)     # For Illustrate_Recursive
    

    @Illustrate_Recursive
    def fib(n):
        if    n == 0: return 1
        elif  n == 1: return 1
        else:         return fib(n-1) + fib(n-2)
    
    print('\nIllustrating recursive fib(onacci)')    
    fib.illustrate(5)           # For Illustrate_Recursive