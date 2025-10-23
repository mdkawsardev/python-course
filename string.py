name = 'Kawsar Ahmed Imran.'
# for n in name:
#     print(n)
# fullName = "imran ahmed kawsar"
# if "ahmed" in fullName:
#     print("Yes! You're right")
# if "rebel" not in fullName:
#     print("Yes! You're right rebel is not in fullname")
# if len(fullName) > 15:
#     print("It's greater than 15")
print(name[-4:])
wel = "welcome"
print(wel[3:5])
print(name.upper())
print(name.lower())
print(name.replace('Kawsar', 'Imran'))
print(name.split(","))
print(name.casefold())
print(name.center(40))
print(name.count("a"))
print(name.encode())
print(name.endswith('Imran.'))
tab = 'H\te\tl\tl\to'
print(tab)
print(tab.expandtabs())
print(tab.expandtabs(10))
print(name.find('r'))
price = "T-shirt {price: 0}"
print(price.format(price = 400))
myself = "my name is {fname}, I'm {age} years old"
print(myself.format(fname = "kawsar", age = 23))
dictionary = {"name": "Kawsar", "age": 23}
txt = "Happy birthday {name} you're now level of {age}"
print(txt.format_map(dictionary))
print(name.index('h'))

# f-string and format both are same
# Using format mathod. Here .2f used for two float 00
text1 = "I'm kawsar and I'm {age} years old. I'm in {level:.2f}".format(age = 23, level = 12)
print(text1)
# Using f-string
identity = 'Web developer'
iden = "Developer"
text2 = f"I'm kawsar and I'm a {identity} and a python {iden}"
print(text2)
math = f"""
math 1 = {2 + 2}
math 2 = {3 + 3}
math 3 = {4 + 4}
"""
print(math)