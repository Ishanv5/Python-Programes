# Sum of 1 to 10 
# total=0
# for i in range(1,21):
#     total+=i
#     i=i+1
# print(total)
n=input("Enter a nos from the user : ")
n=int(n)
total=0
for i in range(1,n+1):
    total+=i
    i+=1
print(total)
