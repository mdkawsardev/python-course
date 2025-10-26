tuple1 = ("Name", "Email", "Age", "Name")
short = [t for t in tuple1 if "A" in t]
print(short)
print(len(tuple1))
tuple2 = ("Name",) # If we add just one sinlge value in tuples then we have to add a ("," comma ) after that value. Otherwise python will take is as tring not tuples
print(type(tuple2))
tuple3 = ("Animal", 34, True, "Human", 23, False) # Tuple contains any data type
print(tuple3)
tuple4 = tuple(("Fruits", "Vagetables", "Meat")) # Using tuple method
print(type(tuple4))
print(tuple1[0]) # Accessing items by index
print(tuple3[-1]) # Accessing items by negative index
print(tuple3[1:5]) # Accessing items by range from 2nd items to 5th item. The search will start at index 2 (included) and end at index 5 (not included).
if "Meat" in tuple4:
    print("Yeah! We got Meat in tuple4")
else: print("Ops! Meat is not in tuple4")

# We know that tuple is unchangeable. But I need to change the items. For that reason 
# First created a tuple then it has been converted into a list then I changed one item
# After changing the item. Here I back to tuple again. Finally, the problem is solved
tuple5 = ("Apple", "Banana", "Cherry")
x = list(tuple5)
x[1] = "Mango"
tuple5 = tuple(x)
print(tuple5)

tuple6 = ("Bangladesh", "Australia", "Germany") # Created a tuple with 3 items but I want to add another item
y = list(tuple6) # Converted tuple into a list
y.append("England") # Now, List is changeable so I added one item to the list
tuple6 = tuple(y) # And back to the tuple
print(tuple6) # Now, the result is done. A tuple is with 4 items

tuple7 = ("Japan",) # I have created a tuple with a single value
tuple6 += tuple7 # Now, I added one tuple to another tuple
print(tuple6)

tuple8 = ("Water", "Gas", "Oil") # To remove items. Same as above without removing
z = list(tuple8)
z.remove("Gas")
tuple8 = tuple(z)
del tuple8 # to delete tuple completely

# Creating a tuple is called packing
tuple9 = ("apple", "banana", "cherry", "mango", "watermalon")
# Now, unpacking tuple. Assigning values into variable
(green, yellow, *red) = tuple9 # (* =Asterisk) means extra values will be stored in red variable as a list. Asterisk can be above on any variable
print(green)
print(yellow)
print(red)
# Print all items by referring to their index number:
for tu in range(len(tuple9)):
    print(tuple9[tu])
print(" ") # For a space
# Printing all items using while loop by index number
i = 0
while i < len(tuple9):
    print(tuple9[i])
    i += 1
multipleTuple = tuple9 * 2 # To multiple tuples or more dependig on numbers. Here number is 2
print(multipleTuple)

# Joining two tuples into a variale
joinTuples = tuple1 + tuple3
print(joinTuples)

print(multipleTuple.count("apple")) # This method counts specified value, how many times item is used in tuple
print(multipleTuple.index("apple")) # This method finds index number of specified value

