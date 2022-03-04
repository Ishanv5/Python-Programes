def Func(name='unknown',age=18):
    print(name,age)
    
Func("Ishan Vaghela")

def func(name,*args,last_name="unknown",**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
    
func('Ishan',512,a=5,b=1,c=2)