#DICTIONARY IS NOTHING BUT KEY VALUE PAIRS
d1 = { }
l1 = [ ]
t1 = ( )
print(type(d1)) #dictionary
print(type(l1)) #list
print(type(t1)) #tuples

#making a dictionary
d2 = {"Ahana" : "pasta", "Akib":"Burger", "Tanim" : "Fish"}
print(d2)
print(d2["Ahana"])

#dictionary in a dictionary
d3 = {"Name":"Ahana","Age":"24","Friends":{"Ema":"Noodles","Fariya":"Coffee"}}
print(d3)
print(d3["Friends"])
d3["Anika"] = "Junk food"
d3[420] = "home food"
print(d3)

#deleting element from dictionary
del d3[420]
print(d3)


#FUNCTIONS IN DICTIONARY

# 1. COPY
d3 = d2.copy()
del d2["Ahana"]
print(d2)

# 2. get

print(d2.get("Tanim"))

# 3. update
d2.update({"Ema":"Meat"})
print(d2)

#printing keys
print(d2.keys())

#printing items
print(d2.items())
