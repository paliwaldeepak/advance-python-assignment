#!/usr/bin/env python
# coding: utf-8

# 1. What is the concept of an abstract superclass?
# #ans:-
# An abstract superclass is one way to provide re-usable code. You can extend the abstract class and inherit the code. This is sometimes more convenient than using static methods or object composition to share code.
# 
# 
# 2. What happens when a class statement's top level contains a basic assignment statement?
# #ans:-
# An assignment statement evaluates the expression list and assigns the single resulting object to each of the target lists, from left to right.
# 
# 
# 3. Why does a class need to manually call a superclass's __init__ method?
# #ans:-
# It's because one needs to define something that is NOT done in the base-class' __init__ , and the only possibility to obtain that is to put its execution in a derived-class' __init__ function.
# 
# 
# 4. How can you augment, instead of completely replacing, an inherited method?
# #ans:-
# A more sophisticated way to augment an inherited method involves forwarding. Message forwarding allows you to augment an inherited method in such a way that it can perform its inherited action and some new action.
# 
# 
# 5. How is the local scope of a class different from that of a function?
# #ans:-
# Local scope just refers to the scope available to a given variable, but function scope would refer to variables inside a function.
# 
