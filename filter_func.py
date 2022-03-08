def is_even(a):
    return a%2==0

nos=[3,4,2,1,5,6,9,8,10]

evens=tuple(filter(is_even,nos))
print(evens)
evens=tuple(filter(lambda a: a%2==0,nos))
print(evens)