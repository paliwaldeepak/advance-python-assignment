#!/usr/bin/env python
# coding: utf-8

# Q1. Is an assignment operator like += only for show? Is it possible that it would lead to faster results at the runtime?
# #ans:-
# The plus-equals operator += provides a convenient way to add a value to an existing variable and assign the new value back to the same variable. In the case where the variable and the value are strings, this operator performs string concatenation instead of addition.
# 
# 
# Q2. What is the smallest number of statements you'd have to write in most programming languages to replace the Python expression a, b = a + b, a?
# #ans:-
# Smallest no.-b
# 
# 
# Q3. In Python, what is the most effective way to set a list of 100 integers to 0?
# #ans:-
# you simply use the list(range(0, 101)) function call.
# 
# 
# Q4. What is the most effective way to initialise a list of 99 integers that repeats the sequence 1, 2, 3? S If necessary, show step-by-step instructions on how to accomplish this.
# #ans:-
# you simply use the list(range(0, 101)) function call.
# 
# 
# Q5. If you're using IDLE to run a Python application, explain how to print a multidimensional list as efficiently?
# #ans:-
# To execute a file in IDLE, simply press the F5 key on your keyboard. You can also select Run → Run Module from the menu bar. Either option will restart the Python interpreter and then run the code that you've written with a fresh interpreter. use the np. array() function and pass in a nested list of values as an argument.
# 
# 
# Q6. Is it possible to use list comprehension with a string? If so, how can you go about doing it?
# #ans:-
# List comprehension works with string lists also. To convert a list to a string, use Python List Comprehension and the join() function. The list comprehension will traverse the elements one by one, and the join() method will concatenate the list's elements into a new string and return it as output.
# 
# 
# Q7. From the command line, how do you get support with a user-written Python programme? Is this possible from inside IDLE?
# #ans:- 
# Using the command line to make IDLE pop up with a filename.py to run; ie >>> idle filename.py. From the command line, just do “python filename.py”. If you want to edit the file with Idle (and then optionnally run it), you can do “python -m idlelib filename.py”
# 
# 
# Q8. Functions are said to be “first-class objects” in Python but not in most other languages, such as C++ or Java. What can you do in Python with a function (callable object) that you can't do in C or C++?
# #ans:-
# Speed Python is slower than C++, it supports dynamic typing, and it also uses the interpreter, which makes the process of compilation slower.
# 
# 
# Q9. How do you distinguish between a wrapper, a wrapped feature, and a decorator?
# #ans:-
# “Wrapper” is the alternative nickname for the Decorator pattern that clearly expresses the main idea of the pattern. A wrapper is an object that can be linked with some target object. The wrapper contains the same set of methods as the target and delegates to it all requests it receives.
# 
# Q10. If a function is a generator function, what does it return?
# #ans:-
# A generator is a special type of function which does not return a single value, instead, it returns an iterator object with a sequence of values.
# 
# 
# Q11. What is the one improvement that must be made to a function in order for it to become a generator function in the Python language?
# #ans:-
# Its perform faster and avoid to written code again and again 
# 
# 
# Q12. Identify at least one benefit of generators.
# #ans:-
# Generators allow you to create iterators in a very pythonic manner. Iterators allow lazy evaluation, only generating the next element of an iterable object when requested. This is useful for very large data sets. Iterators and generators can only be iterated over once.
# 
