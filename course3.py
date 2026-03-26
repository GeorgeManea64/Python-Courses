#Course 3.1: Exceptions

# numbers = [1, 2]
# print(numbers[3])

#It generates a RuntimeError because the item never exists

# age = int(input("Age: "))

#Introducing a different value from the one you used, the program crashes.


#Course 3.2: Handling Exceptions

# try: #try blocks executes every statement where they throw an exception, in which the code is not executed.
#     age = int(input("Age: "))
# except ValueError as ex:
#     print("You didn't enter a valid age.")
#     print(ex)
#     print(type(ex))
# else:
#     print("No exceptions were thrown.")
# print("Execution continues.")

#Error Message:
# Age: a
# You didn't enter a valid age.
# invalid literal for int() with base 10: 'a'
# <class 'ValueError'>
# Execution continues.


#Course 3.3: Handling DIfferent Exceptions

# try:
#     age = int(input("Age: "))
#     xfactor = 10 / age #ZeroDivisionError is caused when an item was divided by 0.
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
# # except ZeroDivisionError:
# #     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown.")


#Course 3.4: Cleaning up

# try:
#     file = open("course3.py")
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown.")
# finally:
#     file.close()


#Course 3.5: The With Statement

# try:
#     # file = open("course3.py")
#     with open("course3.py") as file: #, open("another.text") as target: #Using the with statement, Python will automatically call close() when we have a finally cause or not.
#         print("File opened.")
#         # file.__ #__ are magic items that are used to execute a file, like __enter__ or __exit__
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown.")
# # finally:
# #     file.close()


#Course 3.6: Raising Exceptions

# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age cannot be 0 or less.")
#     return 10 / age

# try:
#     calculate_xfactor(-1)
# except ValueError as error:
#     print(error)


#Course 3.7: Cost of Raising Exceptions

from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    # print(error)
    pass
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age

xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""

print("first code", timeit(code1, number=50))
print("second code", timeit(code2, number=50))