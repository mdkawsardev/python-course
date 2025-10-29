set1 = {"apple", "banana", "cherry"}
set2 = {"pineaple", "papaya", "mango"}
set1.update(set2) # To add items from another set into the current set, use the update() method.
print(len(set1))
print("apple" not in set1) # This will return false
set1.add("watermalon") # To add new items to set
list1 =  ["kawsar", "imran", "emon"]
set1.update(list1) # The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
set1.remove("emon") # To remove items from a set using remove() or discard() methods
set1.discard("watermalon") #  If the item to remove does not exist, discard() will NOT raise an error. But remove() will raise an error
set1.pop() # This method removes random item and returns removed item.
set1.clear() # This method empties the set
del set1 # This deletes permanently the set
for x in set2: # Displaying set's items using for loop
    print(x)

set3 = {"bangladesh", "Australia", "russia"}
set4 = {"America", "Japan", "Germany", "portugal"}
set6 = {"men", "women", "children"}
set7 = {"human", "animal", "etc"}
# set5 = set3.union(set4) same as, set5 = set3 | set4. Both methods join the set
set5 = set3 | set4
set8 = set3.union(set4, set6, set7) # To add multiple sets
set8 = set3 | set4 | set6 | set7 # same as union method. This joins sets to sets not with other data-type like union()
myTuple = ("Phone", "Tv", "Wifi")
set9 = set5.union(myTuple) # The union() method allows you to join a set with other data types, like lists or tuples.
# Both union() and update() will ignore any duplicate items.
set10 = {"mobile", "laptop", "desktop"}
set11 = {"mobile", "pad", "remote"}
set12 = set10.update(set11) # Ignores duplicate items

print(set5)
print(set8)
print(set9)
print(set10)
print(set12)
myfruits = {"apple", "banana", "cherry"}
drinks = {"apple", "mojo", "matha"}
together = myfruits.intersection(drinks) # This returns new set with only duplicate items. Both are same
together = myfruits & drinks # This returns new set with only duplicate items. same as intersection() method but it's just for sets not for other data type, which can intersection()
print(together)
set14 = {"apple", "banana", "cherry"}
set15 = {"mojo", "matha", "banana"}
set16 = set14.intersection_update(set15) # method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
print(set14)
set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", "microsoft", "apple", True}

set3 = set1.intersection(set2)
print(set3)
setsToFroz = frozenset({"hati", "gondar", "bag"})
copy = setsToFroz.copy()
print(setsToFroz)
print(copy)