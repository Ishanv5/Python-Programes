nos=list(range(1,11))
print(nos)
nos.pop()
print(nos.pop())
print(nos)
nos.append("1")
print(nos.index(1))
def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative 

print(negative_list(nos)) 