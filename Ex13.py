nos=list(range(1,5))
print(nos)

def Square_list(l):
    Square=[]
    for i in l:
        Square.append(i*i)
    return Square

print(Square_list(nos))