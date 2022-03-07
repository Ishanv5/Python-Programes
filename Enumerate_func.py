from unicodedata import name


name=['abc','abd','cab']
# pos=0
# for names in name:
#     print(f"{pos} ------> {names}")
#     pos+=1
    
# with Enumerate Func ................
for  pos, names in enumerate(name):
    print(f"{pos} ------> {names}")\
        
def find_pos(l,target):
    for pos, name in enumerate(l):
       if name == target:
           return pos
       else:
           return -1
       
print(find_pos(name,'abc'))
print(find_pos(name,'Ishan'))