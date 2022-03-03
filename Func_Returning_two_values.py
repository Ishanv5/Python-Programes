from audioop import add


def func(int1,int2):
    add=int1+int2
    multiple=int1*int2
    return add,multiple

print(func(10,20))
add,multiple=func(10,20)
print(add)
print(multiple)