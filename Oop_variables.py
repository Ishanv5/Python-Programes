class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius = radius
        
    def calc_circumference(self):
        return 2*Circle.pi*self.radius
    
    
c=Circle(4)
c1=Circle(5)
print(c.calc_circumference())

class Laptop:
    discount_percent = 10
    def __init__(self,brand,name,price):
        self.brand = brand
        self.name = name
        self.price = price
    def apply_discount(self):
           offer= self.price * (self.discount_percent/100)
           return self.price - offer


Laptop.discount_percent =10
Laptop1=Laptop('Asus','Tuf A15',65000)
Laptop2=Laptop('Hp','Omen',63000)
Laptop1.discount_percent =50
# print(Laptop2.apply_discount(10))
# print(Laptop1.apply_discount(50))

print(Laptop1.__dict__)
print(Laptop1.apply_discount())