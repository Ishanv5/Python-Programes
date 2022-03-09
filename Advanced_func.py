def average(l1,l2):
    avg=[]
    for pair in zip(l1,l2):
        avg.append(sum(pair)/len(pair))
    return avg

print(average([1,2,3],[4,5,6]))

def average(*args):
    avg=[]
    for pair in zip(*args):
        avg.append(sum(pair)/len(pair))
    return avg

average=lambda *args:[sum(pair)/len(pair) for pair in zip(*args)]
print(average([1,2,3],[4,5,6],[7,8,9]))