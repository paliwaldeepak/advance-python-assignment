#!/usr/bin/env python
# coding: utf-8

# Q1. In Python 3.X, what are the names and functions of string object types?
# #ans:-
# Method	True if
# str.isalnum()	String consists of only alphanumeric characters (no symbols)
# str.isalpha()	String consists of only alphabetic characters (no symbols)
# str.islower()	String’s alphabetic characters are all lower case
# str.isnumeric()	String consists of only numeric characters
# str.isspace()	String consists of only whitespace characters
# str.istitle()	String is in title case
# str.isupper()	String’s alphabetic characters are all upper case
# 
# 
# Q2. How do the string forms in Python 3.X vary in terms of operations?
# #ans:-
# String Operations can be done in three ways:
# 1.	Using f-strings.
# 2.	By format() method.
# 3.	Using % operator.
# 
# 
# Q3. In 3.X, how do you put non-ASCII Unicode characters in a string?
# #ans:-
# To insert a Unicode character, type the character code, press ALT, and then press X.
# 
# 
# Q4. In Python 3.X, what are the key differences between text-mode and binary-mode files?
# #ans:-
# Text mode is the default mode, and it is used for reading and writing text files, while the binary mode is used for reading and writing binary files. Text files are files that contain text data, such as strings or characters.
# 
# 
# Q5. How can you interpret a Unicode text file containing text encoded in a different encoding than your platform's default?
# #ans:-
# You should either use normal open() and encode the unicode yourself, or (usually a better idea) use codecs. open() and not encode the data yourself
# 
# 
# Q6. What is the best way to make a Unicode text file in a particular encoding format?
# #ans:-
# You should either use normal open() and encode the unicode yourself, or (usually a better idea) use codecs. open() and not encode the data yourself.
# 
# 
# Q7. What qualifies ASCII text as a form of Unicode text?
# #ans:-
# ASCII encodes symbols, digits, letters, etc., whereas Unicode encodes special texts from different languages, letters, symbols, etc.
# 
# 
# Q8. How much of an effect does the change in string types in Python 3.X have on your code?
# #ans:-
# We can use the Python built-in method string. replace() to replace a string in python. We can also use loops to replace a character in a string in Python. String slicing method can also be used to replace a string in python.
# 
