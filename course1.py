#Course 1.1: Introduction to Python (Variables)

students_count = 1000 #Integer 
rating = 4.99 #Float
is_published = False #Boolean
#course_name = "Python" #String

course_name = """
Multiple
lines
"""

x = 1
y = 2

x, y = 1, 2

x = y = 1


#Course 1.2: Dynamic Typing

#int students_count = 1000
students_count = 1000
#students_count = True
print(type(students_count)) #type() function is used to check the type of a variable


#Course 1.3: Type Annotation

age: int = 20
age = "Python" #This will not cause an error because Python is a dynamically typed language, but it is not recommended to change the type of a variable after it has been defined with a type annotation.
print(age)


#Course 1.4: Mutable and Immutable Types

x = 1
print(id(x)) #id() function is used to check the memory address of a variable

x = x + 1
print(id(x)) #The memory address of x has changed because integers are immutable types, so a new object is created in memory when we change the value of x.

x = [1, 2, 3]
print(id(x)) #The memory address of x is the same because lists are mutable types, so the same object is modified in memory when we change the value of x.

x.append(4)
print(id(x))


#Course 1.5: Strings

course = "Python Programming"
print(len(course)) #len() function is used to check the length of a string.
print(course[0]) #Indexing
#print(course[-1]) #Indexing from the end
print(course[-2]) #Indexing from the end
print(course[0:3]) #Slicing
print(course[:3]) #If the first index is not specified, it is assumed to be 0.
print(course[0:]) #If the last index is not specified, it is assumed to be the length of the string.

print(id(course))
print(id(course[0])) #The memory address of the character at index 0.

#Key note: The first index always starts at 0, and the last index is always one less than the length of the string.


#Course 1.6: Escape Sequences

# \"
# \'
# \\
# \n
# """"""

message = 'Python "Programming' #Using double quotes inside a string that is defined with single quotes.
print(message)

message = "Python \"Programming" #Using escape sequence to include double quotes inside a string that is defined with double quotes.
print(message)

message = "Python \\Programming" #Using escape sequence to include a backslash inside a string. The first backslash is an escape character, so it is not included in the string, and the second backslash is included in the string.
print(message)

"""message = "Python\nProgramming" #Using escape sequence to include a new line character inside a string.
print(message)"""

message = """Python
Programming""" #Using triple quotes to include multiple lines in a string.
print(message)


#Course 1.7: Formatted Strings

first = "George"
last = "Manea"
#full = first + " " + last #Concatenation
#Concatenation is the process of combining two or more strings into one string.
full = f"{first} {last}" #Using formatted strings to concatenate strings. The f before the string indicates that it is a formatted string, and the variables are included in curly braces {}.
print(full)

full = f"{len(first)} {3 + 3}" #Using formatted strings to include the length of the first name and the result of a mathematical expression. The len() function is used to check the length of a string, and the result of the mathematical expression is included in the formatted string.
print(full)


#Course 1.8: Useful String Methods

course = "Python Programming"
print(course.upper()) #upper() method is used to convert a string to uppercase.
print(course.lower()) #lower() method is used to convert a string to lowercase.
print(course.title()) #title() method is used to convert the first character of each word in a string to uppercase and the rest of the characters to lowercase.
print(course.find("Pro")) #find() method is used to find the index of the first occurrence of a substring in a string. If the substring is not found, it returns -1.
print(course.replace("Python", "C#")) #replace() method is used to replace all occurrences of a substring in a string with another substring.

course = "   Python Programming   "
print(course.strip()) #strip() method is used to remove leading and trailing whitespace from a string.
# rstrip and lstrip methods are used to remove trailing and leading whitespace from a string, respectively.

course = "Pythn Programming"
print("Python" in course)
#print("Python" not in course) #Using the not in operator to check if a substring is not present in a string. It returns True if the substring is not found, and False otherwise.
course = "Python Programming"
print("Python" in course) #Using the in operator to check if a substring is present in a string. It returns True if the substring is found, and False otherwise.


#Course 1.9: Numbers

"""
x = 10
x = 0b10
print(x) #The binary representation of 10 is 0b1010, so when we assign 0b10 to x, it is equivalent to assigning 2 to x.
"""

x = 10
x = 0b10
print(bin(x)) #Using the bin() function to convert an integer to its binary representation. The bin() function returns a string that starts with 0b, followed by the binary representation of the integer.

"""
x = 0x12c
print(x) #The hexadecimal representation of 300 is 0x12c, so when we assign 0x12c to x, it is equivalent to assigning 300 to x.
"""

x = 0x12c
print(hex(x)) #Using the hex() function to convert an integer to its hexadecimal representation. The hex() function returns a string that starts with 0x, followed by the hexadecimal representation of the integer.

# a + bi
x = 1 + 2j #Using the j suffix to define a complex number. The real part of the complex number is 1, and the imaginary part is 2.
print(x)


#Course 1.10: Arithmetic Operators

x = 10 + 3 #Addition
x = 10 - 3 #Subtraction
x = 10 * 3 #Multiplication
x = 10 / 3 #Division
x = 10 // 3 #Floor division. It returns the quotient of the division, rounded down to the nearest integer.
x = 10 % 3 #Modulus. It returns the remainder of the division of the first operand by the second operand.
x = 10 ** 3 #Exponentiation. It returns the result of raising the first operand to the power of the second operand.

print(x)

x = x + 1
x += 1 #Using the += operator to add a value to a variable and assign the result back to the variable. It is equivalent to x = x + 1.

print(x)

#Key note: Unlike Javascript or C++, Python does not have increment (++) or decrement (--) operators. We can use the += and -= operators to achieve the same result.


#Course 1.11: Working with Numbers

import math #Importing the math module to use mathematical functions.

PI = -3.14 #Uppercase variable names are used to indicate that a variable is a constant, which means that its value should not be changed. However, Python does not enforce this convention, so it is still possible to change the value of a constant variable.
print(round(PI)) #Using the round() function to round a floating-point number to the nearest integer. The round() function takes an optional second argument that specifies the number of decimal places to round to. If the second argument is not provided, it rounds to the nearest integer.
print(abs(PI)) #Using the abs() function to get the absolute value of a number. The abs() function returns the non-negative value of a number, regardless of its sign.

print(math.floor(PI)) #Using the floor() function from the math module to round a floating-point number down to the nearest integer. The floor() function returns the largest integer that is less than or equal to the given number.


#Course 1.12: Type Conversion

#x = input("x: ")
#y = x + 1 #This will cause an error because the input() function returns a string, and we cannot add an integer to a string.

"""
"1" + "1" -> "11" 
1 + 1 -> 2 
"""
#Python doesn't know how to do type conversion, because it doesn't do implicit type conversions. 
"""
x = input("x: ")

print(int(x))
print(float(x))
print(bool(x))
#print(str(x))
"""
#Falsy values:
#""
#0
#[]
#None (null)


#Course 1.13: Conditional Statements

age = 22
if age >= 18:
    print("Adult")
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

print("All done!")    
#>= is the greater than or equal to operator, which returns True if the left operand is greater than or equal to the right operand, and False otherwise.    
#== is the equality operator, which returns True if the left operand is equal to the right operand, and False otherwise.
#!= is the inequality operator, which returns True if the left operand is not equal to the right operand, and False otherwise.

if x > 1:
    pass #The pass statement is used as a placeholder for code that will be added later. It does nothing and is used to avoid syntax errors when we have an empty block of code.
else:
    pass


#Course 1.14: Logical Operators

"""
- and #The and operator returns True if both operands are True, and False otherwise.
- or #The or operator returns True if at least one of the operands is True, and False otherwise.
- not #The not operator returns True if the operand is False, and False if the operand is True. It is a unary operator, which means that it only takes one operand.
"""

name = " "

#if not name: #This will evaluate to True if the name variable is an empty string, which is a falsy value in Python. The not operator negates the value of name, so if name is an empty string, not name will be True, and the code inside the if block will be executed.

if not name.strip():
    print("Name is empty")

#0
#""
#None
#[]
#These are all considered falsy in Python.

age = 22
"""
if age >= 18 and age < 65:
    print("Eligible")
"""
if 18 <= age < 65:
    print("Eligible")

# 18 <= age < 65 is a chained comparison, which is a more concise way to write the same condition. It checks if age is greater than or equal to 18 and less than 65 at the same time.


#Course 1.15: Ternary Operator

age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"

#message = age >= 18 ? "Eligible" : "Not eligible" #Using the ternary operator to assign a value to a variable based on a condition. The syntax is: variable = condition ? value_if_true : value_if_false. However, Python does not have a built-in ternary operator, so we can use a conditional expression instead.

message = "Eligible" if age >= 18 else "Not eligible" #Using a conditional expression to achieve the same result as the ternary operator. The syntax is: variable = value_if_true if condition else value_if_false.

print(message)


#Course 1.16: For Loops

#for loops are used to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code for each item in the sequence.
#while loops are used to execute a block of code repeatedly as long as a certain condition is true.

# for x in "Python":
#     print(x)

# for x in ['a', 'b', 'c']:
#     print(x)

# for x in range(0, 10, 2):
# #The range() function is used to generate a sequence of numbers. The syntax is: range(start, stop, step). The start parameter is the starting number of the sequence (inclusive), the stop parameter is the ending number of the sequence (exclusive), and the step parameter is the increment between each number in the sequence. If the start parameter is not provided, it defaults to 0. If the step parameter is not provided, it defaults to 1.
#     print(x)

print(range(5))


#Course 1.17 For..Else

names = ["George", "Manea"]
# found = False
for name in names:
    if name.startswith("G"): #The startswith() method is used to check if a string starts with a specified prefix. It returns True if the string starts with the prefix, and False otherwise.
        print("Found")
        # found = True
        break #The break statement is used to exit a loop prematurely. When the break statement is executed, the loop is terminated, and the program continues with the next statement after the loop.
# if not found:
else: #The else block after a for loop is executed only if the loop completes without encountering a break statement. If the loop is terminated by a break statement, the else block is skipped.
    print("Not found")


#Course 1.18: While Loops

# guess = 0
# answer = 5

# while answer != guess:
#     guess = int(input("Guess: "))
# else:
#     pass
# while loops are used to execute a block of code repeatedly as long as a certain condition is true. The else block after a while loop is executed only if the loop completes without encountering a break statement. If the loop is terminated by a break statement, the else block is skipped.

#Course 1.19: Functions
# numbers = [1, 2, 3]
# numbers = (1, 2, 3)

# def increment(number, by): #Defining a function named increment that takes two parameters: numbers and by. The numbers parameter is expected to be a list of numbers, and the by parameter is expected to be a number that will be added to each element in the numbers list.
#     return (number, number + by)

# print(increment(2, 3))

# def increment(number, by=1):
#     return (number, number + by)

# print(increment(2))

def increment(number: int, by: int = 1) -> tuple:
    return (number, number + by)

print(increment(2))

#Course 1.20: Arguments- xargs

# def multiply(a, b): #defining a function named multiply that takes two parameters: a and b. The function returns the product of a and b.
#     return a * b

# multiply(2, 3)

# def multiply(list):
#     return a * b #This will cause an error because the function is expecting two parameters, but we are passing a list as a single parameter. We need to unpack the list into individual arguments.

# multiply([2, 3, 4, 5])

# def multiply(*list):
# #The * operator is used to unpack a list of arguments into individual arguments. When we use *list in the function definition, it allows us to pass a variable number of arguments to the function, and they will be collected into a tuple named list.
#     print(list)

# multiply(2, 3, 4, 5)

def multiply(*list):
    total = 1
    for number in list:
        total *= number
    return total

print(multiply(2, 3, 4, 5))

#Course 1.21: Arguments- xxargs

def save_user(**user):
#The ** operator is used to unpack a dictionary of keyword arguments into individual keyword arguments. When we use **user in the function definition, it allows us to pass a variable number of keyword arguments to the function, and they will be collected into a dictionary named user.
    print(user)
    # print(user["id"])
    # print(user["name"])


save_user(id=1, name="admin")
#The save_user function takes a variable number of keyword arguments and prints them as a dictionary. When we call save_user(id=1, name="admin"), the id and name keyword arguments are passed to the function, and they are collected into a dictionary named user, which is then printed. The output will be: {'id': 1, 'name': 'admin'}

