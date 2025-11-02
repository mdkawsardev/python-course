# Function in python
def greet():
    print("Good morning everyone")

greet()
greet()
greet()
greet()
def Greet():
    print("Hello World")
Greet()

# Getting fahrenheit ot celsius
def fahrenheit_to_celsius(fahrenheit):
    return((fahrenheit - 32) * 5 / 9)
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

# function with default value
def customerName(name = "Customer"):
    return(f"Hello dear {name}")
print(customerName("Kawsar"))
print(customerName())
print(customerName("Imran"))

print("")

def animal(animal, name):
    print(f"My animal is {animal}")
    print(f"My animal's name is {name}")
# You can send arguments with the key = value syntax.
animal(animal = "Dog", name = "Rocky")

print("")

# passing a list as an argument
def listing(lists):
    for list in lists:
        print(list)

myList = ["apple", "banana", "cherry", "mango"]
listing(myList)

print("")
# passing a dictionary as an argument
def dic(person):
    print(f"Name is: {person["name"]}")
    print(f"Age is: {person["age"]}")

person = {"name": "Kawsar", "age": 23}
dic(person)

print("")
# Positional-Only Arguments
def my_function(name, /):
    print("Hello", name)

my_function("Emil")

# Keyword-Only Arguments
def keywords_only(*, name):
    print(f"Hello {name}")
keywords_only(name = "kawsar")

# Combining Positional-Only and Keyword-Only
def combining(a, b, /, *, c, d):
    return(a + b + c + d)
print(combining(10, 20, c = 5, d = 10))

# A function that calculates the sum of any number of values:
def calculate(*number):
    total = 0
    for num in number:
        total += num
    return total
print(calculate(2, 2, 6))