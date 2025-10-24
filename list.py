# defining a list with two types
list1 = ['apple', 'banana', 'orange'] # First one
list2 = list(('watermalon', 'strowbry', 'lemon')) # Second one using list() mathod
list1[0:2] = ['mango', 'melon'] # It replaces from zero index to before 2 index. That means 0 to 1 index changed without 2 index
print(list1)

list2[-1] = 'grave' # This replaces last index of an array
list2[-3:-1] = ['rose', 'waterlily'] # This replaces from last index without -1 index/last index
print(list2)
list1.append('pinapple') # This adds items to the last index of an array
print(list1)
list2.insert(2, 'volvo') # This adds items at specified index
print(list2)
list1.extend(list2) # This merges/combines one item to another item
print(list1)
# extend() method works for list, tuple, set, dictionary, etc
list3 = ['volve', 'man', 'mercedez']
tuple1 = ('toyota', 'ferari')
list3.extend(tuple1) # Here I extends list with tuple
print(list3)
for x in list1:
    print(x)
for i in range(len(list1)): # This loop will print items by index number
    print(i)
    print(list1[i])

zero = 0
while zero < len(list1):
    print(list1[zero])
    zero+=1
print(" ")
[print(n) for n in list1] # A short cut way to run for loop with print
flower1 = ['rose', 'waterlily', 'woodrose', 'joba']
newFlower1 = []
for x in flower1:
    if 'o' in x:
        newFlower1.append(x)
print(newFlower1)
flower2 = ['rose1', 'waterlily2', 'woodrose3', 'joba4']
newFlower2 = [x for x in flower2 if 'o' in x] # This is list comprehension/short syntex
print(newFlower2)