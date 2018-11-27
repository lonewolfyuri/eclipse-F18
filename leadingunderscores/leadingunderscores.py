# standard attribute name
class C1:
    def __init__(self):
        self.a = 0
        
    def bump(self):
        self.a += 1

print('Using C1')
c = C1()
print('c.a =',c.a)
c.bump()
print('c.a =',c.a)


##############################


# _ attribute name; just advisory; can still access inside/outside of class
class C2:
    def __init__(self):
        self._a = 0
        
    def bump(self):
        self._a += 1


print('Using C2')
c = C2()
print('c._a =',c._a)
c.bump()
print('c._a =',c._a)


##############################


# __ attribute name; can still access inside of class, but outside of class
# we need to write this attribute as _C3__a.
class C3:
    def __init__(self):
        self.__a = 0

    def bump(self):
        self.__a += 1  # DON'T change; __a usable here


print('Using C3')
c = C3()
print('c._a =',c.__a)  # Replace by c._C3__a; __a not usable here
c.bump()
print('c._a =',c.__a)  # Replace by c._C3__a; __a not usable here
