# Dictionary items are ordered, changeable, and do not allow duplicates.
dictionary1 = {
    "Name": "Kawsar",
    "Age": 23,
    "Single": True, # This will be ignored
    "Single": False
}
print(dictionary1["Age"]) # To access specified item
print(type(dictionary1))
print(len(dictionary1))
# It is also possible to use the dict() constructor to make a dictionary.
dictionary2 = dict(name="kawsar", age= 23, single= True)
# You can access the items of a dictionary by referring to its key name, inside square brackets:
print(dictionary2["name"])
# There is also a method called get() that will give you the same result: 
print(dictionary2.get("age"))
# The keys() method will return a list of all the keys in the dictionary.
print(dictionary2.keys())
# Add a new item to the original dictionary, and see that the keys list gets updated as well: 
dictionary3 = {"Bangladesh": "Dhaka", "Australia": "Seadney", "America": "Washington"}
allKeys = dictionary3.keys()
print(allKeys) # Prints all keys
dictionary3["India"] = "Delhi"
print(allKeys) # Prints all keys after adding new key
# The values() method will return a list of all the values in the dictionary.
allValues = dictionary3.values()
print(allValues)
# Make a change in the original dictionary, and see that the values list gets updated as well:
dictionary3["India"] = "New Delhi"
print(dictionary3)
# The items() method will return each item in a dictionary, as tuples in a list.
print(dictionary3.items())
# To determine if a specified key is present in a dictionary use the in keyword:
if "Bangladesh" in dictionary3:
    print("Yes, Bangladesh is a key in this dictionary")

# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.
dictionary5 = dict(primary=12, high=23, college=32)
# This updates/changes the values
dictionary5.update({"primary": 32})
# This adds new items
dictionary5["university"] = 50
# This adds new items as well
dictionary5.update({"phd": 46})


# The pop() method removes the item with the specified key name:
dictionary5.pop("high")
# The popitem() method removes the last inserted item
dictionary5.popitem()
# The del keyword removes the item with the specified key name:
del dictionary5["primary"]
#* The del keyword can also delete the dictionary completely: del dictionary5
# The clear() method empties the dictionary:
dictionary5.clear()
print(dictionary5.items())
# This will return all keys
for x in dictionary1:
    print(x)
# This will return all values
for y in dictionary1:
    print(dictionary1[y])
# You can use these also
print(dictionary1.keys())
print(dictionary1.values())
# Loop through both keys and values, by using the items() method:
for a, b in dictionary2.items():
    print(a, b)
print("")
# Make a copy of a dictionary with the copy() method:
copyDic = dictionary3.copy()
print(copyDic)
# Another way to make a copy is to use the built-in function dict().
anotherCopy = dict(dictionary3)
print(anotherCopy)
print("")
child1 = {
    "Name": "Akib",
    "Age": 12
}
child2 = {
    "Name": "Rakib",
    "Age": 15
}
child3 = {
    "Name": "Muskil",
    "Age": 20
}
# Nesting dictionary
myFamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
# You can loop through a dictionary by using the items() method like this:
for z, obj in myFamily.items():
    print(z)
    for k in obj:
        print(k + ":", obj[k])