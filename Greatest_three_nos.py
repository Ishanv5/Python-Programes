from calendar import c


def large(a,b,c):
    if a>b & a>c:
        print("a is greater than b and c")
    elif b>a & b>c:
        print("b is greater than a and c") 
        
    else:
        print("c is greater than a and b")
    
large(5,6,3)