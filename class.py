# class Person:
#     name = "Kawsar"
#     age = 23
#     nationality = "Bangladeshi"
#     occupation = "Software Developer"
#     def info(self):
#         print(f"{self.name} is {self.age} years old, he is a {self.occupation}, and he is {self.nationality}")

# p1 = Person()
# p1.name = "Imran"
# p1.age = 22
# p1.nationality = "American"
# p1.occupation = "Student"
# p1.info()

# p2 = Person()
# p2.name = "Emon"
# p2.age = 21
# p2.nationality = "British"
# p2.occupation = "Cyber Security"
# p2.info()

# p3 = Person()
# p3.info()

class Person:
    def __init__(self, name, occ): # This is a constructor
        self.name = name
        self.occ = occ
    def info(self):
        print(f"Hey I'm {self.name}, I'm a {self.occ}")

a = Person("Kawsar", "Developer")
a.info()
b = Person("Imran", "Designer")
b.info()
# c = Person("Emon", "Architect")
# c.info()