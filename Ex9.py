# ask user for name
# Ex Ishan Vaghela
# print count of each WORD
# i 1
# s 2 
# h 3
# a 4
# n 5
temp_var=""
name=input("Plz enter your name")
i=0
while i< len(name):
    if name[i] not in temp_var:
        temp_var+=name[i]
        print(f"{name[i]} :{name.count(name[i])}")
    i=i+1