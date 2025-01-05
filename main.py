##Lecture 1: Python Basics
## Access List Items
# fruits = ['apple', 'banana', 'cherry', 'grapes', 'watermelon']

# first_fruits = fruits[0]
# fourt_fruits = fruits[3]

# print(first_fruits)
# print(fourt_fruits)

##Lecture 2: Python Basics
## Access Set Items
# fruits = {'apple', 'banana', 'cherry', 'grapes', 'watermelon', 'apple'}
# print("Original Set:", fruits)

# for fruit in fruits:
#     print(f"Fruit: {fruit}")

##Lecture 3: Python Basics
#Access Dictionary Items
# my_dict = {'name': "John", 'age': 25, 'city': "New York"}

# name= my_dict['name']
# age = my_dict['age']
# city = my_dict['city']

# print(f"Name: {name}")
# print(f"Age: {age}")
# print(f"City: {city}")

##Lecture 4: Python Basics
# Access Tuple Items
# books = ("English", "Math", "Science", "History", "Geography")

# f_books = books[0]
# sec_books = books[1]

# print("first Book: ", f_books)
# print("Second Book:", sec_books)

##Lecture 5: Python Basics
# Add & remove List Items
# fruits = ['apple', 'banana', 'cherry', 'grapes', 'watermelon']

# fruits.append('orange')
# fruits += ["pineapple"]
# print("After Adding:", fruits)

# fruits.remove("banana")
# del fruits[4]
# print("After Removing:4", fruits)

##Lecture 6: Python Basics
# Add & remove dictionary Items
# my_dict = {'name': "John", 'age': 25, 'city': "New York"}
# print("Original Dictionary:", my_dict)
# my_dict['salary']= 50000
# my_dict['department']= "IT"
# print("After Adding:", my_dict)

# removed_my_dict = my_dict.pop('age')
# print("After Removing:", my_dict)
# print("Removed Item:", removed_my_dict)

##Lecture 7: Python Basics
# Add & remove Set Items
# fruits = {'apple', 'banana', 'cherry', 'grapes', 'watermelon', 'apple'}
# print("Original Set:", fruits)
# fruits.add('mango')
# print("After Adding:", fruits)
# fruits.discard('cherry')
# print("After removing: ", fruits)
# fruits.remove('apple')
# print("After popping: ", fruits)

##Lecture 8: Python Basics
# Assign Multiple Values
# val_list = [1,2,3]
# a,b,c = val_list

# val_tup = [4,5,6]
# d,e,f = val_tup

# print(val_list)
# print(a,b,c)
# print(val_tup)
# print(d,e,f)

##Lecture 9: Python Basics
# Arrays
# import numpy as np;
# arr1 = np.array([1,2,3,4,5])
# arr2 = np.arange(0,10,2)
# arr3 = np.zeros((2,3))
# arr4 = np.ones((3,2))

# print(arr1)
# print("...............")
# print(arr2)
# print("...............")
# print(arr3)
# print("...............")
# print(arr4)
# print("...............")

##Lecture 10: Python Basics
# Change Disctionary Items
# dict = {'name': 'John', 'age': 24, 'marks': 60}
# print("Original dictionary: ", dict)

# dict['age']= 21
# dict['marks']= 85

# print('Updated dictionary: ', dict)

##Lecture 11: Python Basics
#Change List Items
# fruits = ["mango", "Banana", "Grapes", "Almond", "Papaya"]
# fruits[0]= "name"
# fruits[1]= "Age"
# print(fruits)
# fruits[2:6]= [20,30,40]
# print(fruits)

##Lecture 12: Python Basics
#Booleans Variables
# is_py_fun = True
# is_learning = False

# result_and = is_py_fun and is_learning
# result_or = is_py_fun or is_learning
# result_not = not is_py_fun

# print('Is python fun? ', is_py_fun)
# print('Is Learning? ', is_learning)
# print('Result of AND ',result_and)
# print('Result of Or ',result_or)
# print('Result of Not ',result_not)

##Lecture 13: Python Basics
#Data Types
# name = 'Smith'
# age = 30
# height = 1.75
# is_adult = True

# print('Name: ', type(name))
# print('Age: ', type(age))
# print('Height: ', type(height))
# print('Is Adult: ', type(is_adult))

# grades= [90,85, 92, 88]

# coordinates = (3,7)

# person = {'name': 'John', 'age': 25, 'city': 'New York'}
# print('Grades:', type(grades))
# print('Coordinates:', type(coordinates))
# print('Person:', type(person))

##Lecture 14: Python Basics
# #Classes and Objects
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def bark(self):
#             print(f"{self.name} says Woof!")

# my_dog = Dog("Buddy", 3)

# print(f"My dog name is {my_dog.name} and age is {my_dog.age} years old")
# my_dog.bark()

##Lecture 15: Python Basics
# #Arguments and Parameters

# def display_info(name, age, **additional_info):
#     print(f"Name: {name}")
#     print(f"age: {age}")

#     for key, value in additional_info.items():
#         print(f"{key.capitalize()}: {value}")

# display_info(name="Charlie", age=30, occupation="Engineer", city="Canada")

##Lecture 16: Python Basics
# Create, Read and Delete file

# file_path = 'example.txt'
# with open(file_path, 'w') as file:
#     file.write("Hello, Python!")

# try:
#     with open(file_path, 'r') as file:
#             content = file.read()
#             print("File content: ")
#             print(content)

# except FileNotFoundError:
#     print(f"Error: file not found: {file_path}")

# file_to_delete = 'example.txt'

# try:
#     import os
#     os.remove(file_to_delete)
#     print(f"file {file_to_delete} deleted successfully")

# except FileNotFoundError:
#     print(f"Error: file not found: {file_to_delete}")

# except Exception as e:
#     print(f"error: {e}")

##Lecture 17 : Python Basics
# List

# fruits = ["Apple", "Banana", "Orange", "Grapes"]

# first_fruit = fruits[0]
# last_fruit = fruits[-1]

# selected_fruits = fruits[1:3]
# fruits[3] = 'mango'
# fruits.append('cherry')
# removed_fruit = fruits.pop(1)

# print(fruits)
# print(first_fruit)
# print(last_fruit)
# print(selected_fruits)
# print(fruits)
# print(removed_fruit)

##Lecture 18 : Python Basics
#Loop sets

# fruits = {'apple', 'banana', 'orange', 'mango'}
# for fruit in fruits:
#     print(f"Fruits: {fruit}")

# set_a = {1,2,3,4,5}
# set_b = {4,5,6,7,8}

# union_set = set_a.union(set_b)
# for number in union_set:
#     print(f"Number : {number}")

##Lecture 19 : Python Basics
# Loop Tuples

# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#     print(x)

# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):
#     print(thistuple[i])

# thistuple = ("apple", "banana", "cherry")
# i=0
# while i < len(thistuple):
#     print(thistuple[i])
#     i = i + 1

##Lecture 20 : Python Basics
# Modify String
# original_string = "Hello, World"
# lowercase_string = original_string.lower()
# uppercase_string = original_string.upper()
# concatenated_string = lowercase_string + " " +  uppercase_string

# print(original_string)
# print(lowercase_string)
# print(uppercase_string)
# print(concatenated_string)

##Lecture 21 : Python Basics
# Module

# import math

# angle = 45
# radians = math.radians(angle)
# sin_value = math.sin(radians)

# print(radians)
# print(sin_value)

##Lecture 22 : Python Basics
# Nested Dictionaries

# student_data = {
#     'John': {'math': 90, 'english': 85},
#     'Alice': {'math': 96, 'english': 56},
#     'Smith': {'math': 78, 'english': 68},
# }
# print("student Data: ", student_data)

# john_math_grade = student_data['John']['math']
# print(f"Jogn's math grade: {john_math_grade}")

##Lecture 23 : Python Basics
#  Operators
# a = 10
# b = 3
# addition = a+b
# subtraction = a-b
# multiplication = a * b
# division = a / b
# remainder = a % b
# exponentiation = a ** b
# print(addition)
# print(subtraction)
# print(multiplication)
# print(division)
# print(remainder)
# print(exponentiation)

##Lecture 24 : Python Basics
# Output Variables
# name = "ALice"
# age = 30
# print( "Name: ", name)
# print("Age: ", age)
# print(f"Person: {name}, Age: {age}")

##Lecture 25 : Python Basics
# Print and Return

# def greet_user(name):
#     print(f"Hello, {name}")

# greet_user("Bob")

# def add_number(a,b):
#     result = a + b
#     return result

# sum_result = add_number(5,6)
# print(f"The sum is: {sum_result}")

##Lecture 26 : Python Basics
# Regular Expression
# import re
# text = "Hello, python ! welcome to the world of regex."

# match_result = re.search(r"python", text)
# if match_result:
#     print(f"pattern 'python' found at index {match_result.start()}")
# else:
#     print("pattern not found.")

##Lecture 27 : Python Basics
# Set Methods

# fruits = {"Apple", "Orange", "Banana"}
# fruits.add("Cherry")
# print("Updated fruits ser: ", fruits)

# colors = {"Red", "Blus", "Green"}
# colors.remove("Green")
# print('Updated Colors: ', colors)

##Lecture 28 : Python Basics
# Sets
# thisset = {"Apple", "Banana", "Orange"}
# print(thisset)

# fruits_set = {'orange', 'banana', 'apple', 'cherry'}

# fruits_set.add('grape')

# fruits_set.remove('banana')

# print('Original fruits set: ', fruits_set)

##Lecture 29 : Python Basics
# Slicing strings
# test = "Python Programming"
# substring = test[7:18]
# print("Original String: ", test)
# print("Extract substring: ", substring)

# Phrase = "Data science is amazing"
# reversed_phrase = Phrase[::-1]
# print("Original : ", Phrase)
# print("Extract : ", reversed_phrase)

##Lecture 30 : Python Basics
# String Methods
# sentence = "Python is versatile and Python is powerful"
# modified_sentence = sentence.replace('Python', 'Java')
# word_list = sentence.split()
# print(sentence)
# print(modified_sentence)
# print(word_list)