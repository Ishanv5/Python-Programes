user_id=['user1','user2,','user3']
names=['Ishan','Meet','Sujal']
last_name=['Vaghela','Vaghela','Gohil']
print(list(zip(user_id,names,last_name)))

l=[(1,2),(3,4),(5,6),(7,8)]
l1,l2=list(zip(*l))
print(list(l1))
print(list(l2))
