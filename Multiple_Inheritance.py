class A:
    def class_a_method(self):
        return "I am just class A method"
    
    def hello(self):
        return "hello from class A"
    
# instance_a=A()
# print(instance_a.class_a_method())


class B:
    def class_b_method(self):
        return "I am just class B method"
    
    def hello(self):
        return "hello from class B"
    
class C(A,B):
    pass

instance_c= C()
print(instance_c.class_a_method())
print(instance_c.class_b_method())
print(instance_c.hello())
print(help(C))
print(C.mro())
