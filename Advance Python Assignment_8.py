#!/usr/bin/env python
# coding: utf-8

# Q1. What are the two latest user-defined exception constraints in Python 3.X?
# #ans:-
# •	class JustException(Exception): def __init__(self, message): print(message)
# •	raise JustException("Raise an Exception")
# 
# 
# Q2. How are class-based exceptions that have been raised matched to handlers?
# #ans:-
# summary, raised class-based exceptions are matched to handlers based on the class hierarchy of the exception classes, starting from the point where the exception was raised and moving up the call stack until a suitable handler is found or the exception becomes unhandled.
# 
# Q3. Describe two methods for attaching context information to exception artefacts.
# #ans:-
# Python has two types of exceptions namely, Built-In Exceptions and User-Defined Exceptions.
# 
# Q4. Describe two methods for specifying the text of an exception object's error message.
# #ans:-
# Using printStackTrace Method.
# Using getMessage() Method.
# 
# 
# Q5. Why do you no longer use string-based exceptions?
# #ans:-
# Python doesn't subscribe to the idea that exceptions should only be used for exceptional cases, in fact the idiom is 'ask for forgiveness, not permission'. This means that using exceptions as a routine part of your flow control is perfectly acceptable, and in fact, encouraged.
# 
