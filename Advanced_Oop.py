# Encapsulation , Abstraction , Naming Conventions,Name mangling................................................................
class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = price
        self._price = price
        self.__price = price
        
    def make_a_call(self,phone_nos):
        print(f"calling {phone_nos}")
    def full_name(self):
        return f"{self.brand} {self.model_name}" 
    def send_message(self):
        pass
    
    
ph1=Phone("Nokia","1100","2000")
print(ph1._price)
print(ph1._Phone__price)
print(ph1.__dict__)
# _name  // Conventions of private name
# __name__ //dunder/magic methods

l=[3,4,1,2]
l.sort()
print(l)
