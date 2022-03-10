
def decorator_function(any_function):
    def wrapper_function(*args, **kwargs):
        print("This is Awesome function..........")
        return  any_function(*args,**kwargs)
    return wrapper_function
@decorator_function
def func(a):
    print(f"This is function with argument {a}..........")
    
func(7)
@decorator_function
def add(a,b):
    return a + b

print(add(4,3))
