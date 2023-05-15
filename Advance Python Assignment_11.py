#!/usr/bin/env python
# coding: utf-8

# Q1. What is the concept of a metaclass?
# #ans:-
# A metaclass in Python is a class of a class that defines how a class behaves. A class is itself an instance of a metaclass. A class in Python defines how the instance of the class will behave. In order to understand metaclasses well, one needs to have prior experience working with Python classes.
# 
# 
# Q2. What is the best way to declare a class's metaclass?
# #ans:-
# class MyMeta(type): pass class MyClass(metaclass=MyMeta): pass class MySubclass(MyClass): pass.
# 
# 
# Q3. How do class decorators overlap with metaclasses for handling classes?
# #ans:-
# Functions can be decorated with classes to extend their functionality. Further, classes that decorate functions can either accept arguments or fall back to a default if no argument is passed. Here, both use-cases are presented to improve the functionality of the original function
# 
# 
# Q4. How do class decorators overlap with metaclasses for handling instances?
# #ans:-
# Decorators provide a simple syntax for calling higher-order functions. By definition, a decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.
# 
