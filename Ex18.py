from itertools import count


def sublist(l):
    count=0
    for i in l:
        if type(i)==list:
            count+=1
    return count

mixed=[1,2,3,[4,5],[4,9]]
print(sublist(mixed))