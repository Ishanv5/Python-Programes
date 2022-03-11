class Laptop:
    def __init__(self,brand,name,price):
        self.brand = brand
        self.name = name
        self.price = price
Laptop1=Laptop('Asus','Tuf A15',65000)
Laptop2=Laptop('Hp','Omen',630000)
print(Laptop1.brand)
print(Laptop1.name)
print(Laptop1.price)
print(Laptop2.brand)
print(Laptop2.name)
print(Laptop2.price)