from cgitb import small


class Phone:    # parent class
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = price
        self._price = max(price,0)
        
    def full_name(self):
        return f"{self.brand} {self.model_name}"
    
    def make_a_call(self,nos):
        return f"calling {nos}....."
    
class Smartphone(Phone):  #derived class /child class
       def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
            Phone.__init__(self,brand,model_name,price)
            # self.brand = brand
            # self.model_name = model_name
            # self.price = price
            # super().__init__(self,brand,model_name,price)   another method for inherit
            self.ram = ram
            self.internal_memory = internal_memory
            self.rear_camera = rear_camera
            # self._price = max(price,0)
        
       def full_name(self):
        return f"{self.brand} {self.model_name}"
    
       def make_a_call(self,nos):
        return f"calling {nos}....."
    
class SuperPhone(Smartphone):
     def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera,processor):
            super().__init__(self,brand,model_name,price,ram,internal_memory,rear_camera)
            self.processor = processor
    
smartphone=Smartphone('Redmi ','Note 9 pro max',20000,'6gb ram','128gb storage','64mp')
oneplus=Smartphone('Redmi ','Note 9 pro max',20000,'6gb ram','128gb storage','64mp')
print(oneplus.full_name())
print(help(Smartphone))