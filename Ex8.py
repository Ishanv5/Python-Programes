


# ask user to input a nos containing more than one digit
# ex 1234
# calculate 1+2+3+4 and print
n=input("Enter a nos of more than more digit : ")
total=0
i=0
while i<len(n):
    total=total+int(n[i])
    i=i+1
print(total)