# F stringsimport mathme = "Ishan"a1 = 3# a = "this is %s"%(me, a1)# a = "This is {1} {0}"# b = a.format(me, a1)# print(b)a = f"this is {me} {a1} {math.cos(30)}"print(a)