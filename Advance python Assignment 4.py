#!/usr/bin/env python
# coding: utf-8

# Q1. Which two operator overloading methods can you use in your classes to support iteration?
# #ans:-
# The __iter__ returns the iterator object and is implicitly called at the start of loops. The __next__ method returns the next value and is implicitly called at each loop increment. __next__ raises a StopIteration exception when there are no more value to return, which is implicitly captured by looping constructs to stop iterating.
# 
# 
# Q2. In what contexts do the two operator overloading methods manage printing?
# #ans:-
# To overload the + operator, we will need to implement __add__() function in the class.
# 
# 
# Q3. In a class, how do you intercept slice operations?
# #ans:-
# The slice() method returns a portion of an iterable as an object of the slice class based on the specified range. It can be used with string, list, tuple, set, bytes, or range objects or custom class object that implements sequence methods __getitem__() and __len__() methods
# 
# 
# Q4. In a class, how do you capture in-place addition?
# #ans:-
# Python provides the operator x += y to add two objects in-place by calculating the sum x + y and assigning the result to the first operands variable name x . You can set up the in-place addition behavior for your own class by overriding the magic “dunder” method __iadd__(self, other) in your class definition.
# 
# 
# Q5. When is it appropriate to use operator overloading?
# #ans:-
# Operator overloading is mostly useful when you're making a new class that falls into an existing "Abstract Base Class" (ABC) -- indeed, many of the ABCs in standard library module collections rely on the presence of certain special methods.
# 
