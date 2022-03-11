class Laptop:
    discount_percent = 10
    def __init__(self,brand,name,price):
        self.brand = brand
        self.name = name
        self.price = price
    def apply_discount(self,n):
           offer= self.price * (n/100)
           return self.price - offer


Laptop.discount_percent =0
Laptop1=Laptop('Asus','Tuf A15',65000)
Laptop2=Laptop('Hp','Omen',63000)
# print(Laptop2.apply_discount(10))
# print(Laptop1.apply_discount(50))
print(Laptop1.apply_discount())
