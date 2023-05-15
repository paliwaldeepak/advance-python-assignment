#!/usr/bin/env python
# coding: utf-8

# Q1. Can you create a programme or function that employs both positive and negative indexing? Is there any repercussion if you do so?
# #ans:-
# In Python, you can start indexing from the end of an iterable. This is known as negative indexing. This means you can use both positive and negative indexes to access iterables.
# 
# 
# Q2. What is the most effective way of starting with 1,000 elements in a Python list? Assume that all elements should be set to the same value.
# #ans:-
# Using the range() function to create a list from 1 to 100 in Python. In Python, we can use the range() function to create an iterator sequence between two endpoints. We can use this function to create a list from 1 to 100 in Python. The function accepts three parameters start , stop , and step .
# 
# 
# Q3. How do you slice a list to get any other part while missing the rest? (For example, suppose you want to make a new list with the elements first, third, fifth, seventh, and so on.)
# #ans:-
# you can set the value of elements in a list by using a slice on the left hand side of an equal sign
# Ex:- 
# my_list = [1, 2, 3, 4, 5]
# 
# print(my_list[::2])
# 
# Q4. Explain the distinctions between indexing and slicing.
# #ans:-
# Indexing	Slicing
# It returns only 1 item	It returns a new list/tuple
# An IndexError will be thrown if you attempt to use an index that is too large.	When used for slicing, out-of-range indexes are handled gently.
# We cannot change the length of the list by item assignment in indexing.	We can change the length of the list or even clear it by assigning items to slicing.
# We can assign a single element or an iterable to indexing.	When we assign a single element to slicing, we get a TypeError. It will only accept iterables.
# 
# 
# 
# Q5. What happens if one of the slicing expression's indexes is out of range?
# #ans:-
# The slice just takes all elements up to the maximal element. If the start index is out of bounds as well, it returns the empty slice.
# 
# 
# Q6. If you pass a list to a function, and if you want the function to be able to change the values of the list—so that the list is different after the function returns—what action should you avoid?
# #ans:-
# Avoid pass function 
# 
# 
# Q7. What is the concept of an unbalanced matrix?
# #ans:-
# Whenever the cost matrix of an assignment problem is not a square matrix, that is, whenever the number of sources is not equal to the number of destinations, the assignment problem is called an unbalanced assignment problem.
# 
# 
# Q8. Why is it necessary to use either list comprehension or a loop to create arbitrarily large matrices?
# #ans:-
# List comprehensions are the right tool to create lists — it is nevertheless better to use list(range()). For loops are the right tool to perform computations or run functions. In any case, avoid using for loops and list comprehensions altogether: use array computations instead
# 
