d1 = {}
print(type(d1))
d2 = {"Ishan":"Pizza", "Meet":"Burger", "Sujal":"Dosa", "Nikita":{"B":"maggie", "L":"roti", "D":"Sandwich"}}
print(d2)
print(d2["Ishan"])
print(d2["Nikita"])
d2["Ansh"] = "Bindi"
d2["Palak"] = "Kurkure"
print(d2)
del d2["Palak"]
print(d2)
d3 = d2.copy()
print(d3)
d2.update({"Raj":"Tofee"})
print(d2)
print(d2.keys())
print(d2.items())