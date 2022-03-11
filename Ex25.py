class Student:
    count_instances = 0
    def __init__(self,first_name,last_name,age):
        Student.count_instances+=1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
s1=Student("Ishan","Vaghela",18)
s2=Student("Meet","Vaghela",17)
s3=Student("Sujal","Gohil",17)
print(Student.count_instances)