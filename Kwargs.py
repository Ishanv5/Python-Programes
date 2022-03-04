def func(**kwargs):
    # print(kwargs)
    # print(type(kwargs))
    for k,v in kwargs.items():
        print(f"{k}:{v}")
    
func(First_name="Ishan",Last_name="Vaghela")