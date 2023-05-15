#!/usr/bin/env python
# coding: utf-8

# Q1. Does assigning a value to a string's indexed character violate Python's string immutability?
# #ans:-
# yes they are immutable because the second line creates a new string. s is only a name or label assigned to the string.
# 
# 
# Q2. Does using the += operator to concatenate strings violate Python's string immutability? Why or why not?
# #ans:-
# This optimization violates the normal rules for id and += . Normally, += on immutable objects is supposed to create a new object before clearing the reference to the old object, so the new and old objects should have overlapping lifetimes, forbidding equal id values.
# 
# 
# Q3. In Python, how many different ways are there to index a character?
# #ans:-
# Basic Slicing and Advanced Indexing in NumPy Python
# 
# 
# Q4. What is the relationship between indexing and slicing?
# #ans:-
# “Indexing” means referring to an element of an iterable by its position within the iterable. 
# “Slicing” means getting a subset of elements from an iterable based on their indices.
# 
# 
# Q5. What is an indexed character's exact data type? What is the data form of a slicing-generated substring?
# #ans:-
# String indexing in Python is zero-based: the first character in the string has index 0 , the next has index 1 , and so on. The index of the last character will be the length of the string minus one.
# Slicing is the process of obtaining a portion (substring) of a string by using its indices. start is the index from where we want the substring to start. end is the index where we want our substring to end.
# 
# Q6. What is the relationship between string and character "types" in Python?
# #ans:-
# strings in Python are arrays of bytes representing unicode characters. However, Python does not have a character data type, a single character is simply a string with a length of 1.
# 
# 
# Q7. Identify at least two operators and one method that allow you to combine one or more smaller strings to create a larger string.
# #ams:
# You can combine both string variables and string literals using the “+” operator. The string operator (&) can be used in formulas to concatenate, or join, two or more strings or the contents of referenced cells.
# The join() method is the fastest, cleanest, most elegant, and most readable method when you need to concatenate many small pieces of string into a larger string.
# 
# Q8. What is the benefit of first checking the target string with in or not in before using the index method to find a substring?
# #ans:-
# To find the position of first occurrence of a string, you can use string. find() method. where string is the string in which you have to find the index of first occurrence of substring . start and end are optional and are starting and ending positions respectively in which substring has to be found.
# 
# 
# Q9. Which operators and built-in string methods produce simple Boolean (true/false) results?
# #ans:-
# True , False , not , and , and or are the only built-in Python Boolean operators.
# 
