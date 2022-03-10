
def decorator_function(any_function):
    def wrapper_function():
        print("This is Awesome function..........")
        any_function()
    return wrapper_function


@decorator_function
def func1():
    print("This is function 1.....")
    
def func2():
    print("This is ffunction 2.....")
func1()

var=decorator_function(func1)
var1=decorator_function(func2)
var()
var1()