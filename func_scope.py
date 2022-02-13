from re import X


x=5 #global variablr
def func():
    global x
    x=7   #local variablr
    return x
print(x)
print(func())
print(x)
    

