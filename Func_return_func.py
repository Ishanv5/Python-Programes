def outer_func():
    def inner_func():
        print('Inside inner Func')
    return  inner_func

var=outer_func()
var()
def outer_func2(msg):
    def inner_func2():
        print(f"message is {msg}") 
    return inner_func2

var=outer_func2("Hi This is Ishan Vaghela.........")
var()