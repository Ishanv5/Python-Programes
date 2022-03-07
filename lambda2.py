import abc


def add(a,b):
    return a + b

add2=lambda a,b: a + b
print(add2(2,3))

multiply=lambda a,b: a * b
print(multiply(2,3))

def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False
    
is_even2=lambda a : a % 2 == 0
print(is_even2(2))

# Lambda Expression with if-else statement................................................................

def func(s):
    if len(s)> 5:
        return True
    return False


func=lambda s: True if len(s)>5 else False
print(func('abc'))