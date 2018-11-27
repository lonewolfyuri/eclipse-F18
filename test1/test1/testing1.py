l = [0,1,2,3,4,5,6,7,8,9]
x = iter(l)
y = x

print(next(x))
print(next(y))

print(next(x))
print(next(y))

x = iter(l)

print(next(x))
print(next(y))