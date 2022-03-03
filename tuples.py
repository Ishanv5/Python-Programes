# days=('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
# print(days[::2])
mixed=(1,2,3,4.0)
for i in mixed:
    print(i)
    
nums=(1,)  # Single element in tuples 
print(type(nums))

# *************** Tuples without parenthesis **********
guitars='Yamaha','Baton Rouge','Taylor'
print(type(guitars))

# *************** Tuples Unpacking ************

cricketors=('Virat Kohli','Rohit Sharma','MS Dhoni')
cricketors1,cricketors2,cricketors3=(cricketors)
print(cricketors1)
print(cricketors2)
print(cricketors3)

# ****************** List Inside Tuples *************

wrestlers=('John Cena',['Rock','AJ Styles'])
wrestlers[1].pop()
wrestlers[1].append("Roman Reigns")
print(wrestlers)