number = 12
if number > 0:
    print("Number is positive")
a = 12
b = 12
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal b")
print("")
# user = int(input("Enter you score "))
# if user >= 90:
#     print("Your grage is: A")
# elif user >= 80:
#     print("Your grade is: B")
# elif user >= 70:
#     print("Your grade is: C")
# elif user >= 60:
#     print("Your grade is: D")
# else:
#     print("You're failed!")

x = 44
y = 34
# Shorthand if-else statement
print("X is greater than Y") if x > y else print("Y is greater then X")
# Assign the value with if-else and finding the maximum number of two numbers
greater = x if x > y else y
print(f"Greater is {greater}")
print("")
# Setting a default value:
username = ""
display_name = username if username else "Guest"
print(display_name)

# match 
point = 33
match point:
    case a if point >= 90:
        print("Your grade is: A+")
    case b if point >= 80:
        print("Your grade is: A")
    case c if point >= 70:
        print("Your grade is: A-")
    case d if point >= 60:
        print("Your grade is: B")
    case e if point >= 50:
        print("Your grade is: C")
    case f if point >= 33:
        print("Your grade is: D")
    case _:
        print("You're fail")
