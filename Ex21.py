def func(l,**kwargs):
    if kwargs.get('reverse_str')==True:
        return [name[::-1].title for name in l]
    else:
        return [name.title() for name in l]

name=['ishan','vaghela']
print(func(name))    
print(func(name,reverse_str=True))    