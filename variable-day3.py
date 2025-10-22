import random
# This chapter we will discuss about python variable
# A variable is a container to store data
# In python programming variable is case-sensitive, (age, Age, and AGE) different type of variable
# A variable name can start with alpha-numeric and underscore
# A variable cannot start with a number
a = 5
b = 6
c = "Kawsar"
d = 'imran'
print(a)
print(b)
print(c)
# Here a,b, and c are variable and value 5,6,"kawsar"
# Python allows you to assign values to multiple variables in one line:
x, y, z = "Imran", "kawsar", "emon"
print(y)
print(y)
print(z)

# One value to multiple variables
ami=tumi=she = "kabo"
print(she)

# Unpacking variables
fruits = ['apple', 'banana', 'orange']
apple, banana, orange = fruits
print(banana)

# printing multiple variables separated by comma
py = "Python"
Is = "is"
awe = "awesome"
print(py, Is, awe)

com = 4j
print(type(com))

# to generate random number first random module imported
print(random.randrange(6000, 9000))