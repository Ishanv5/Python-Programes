class Person:
    count_instances =0
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    
    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instances} of Person classes."
       
    def full_name(self):
        return f"{self.first_name}  {self.last_name}"
    
    def is_above_18(self):
        return self.age > 18
        
p1=Person("Ishan","Vaghela",18)
p2=Person("Meet","Vaghela",16)
p3=Person("Sujal","Gohil",17)
print(p1.first_name)
print(p1.last_name)
print(p1.age)
print(p2.first_name)
print(p2.last_name)
print(p2.age)
print(p3.first_name)
print(p3.last_name)
print(p3.age)
print(Person.count_instances())