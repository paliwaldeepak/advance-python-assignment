#!/usr/bin/env python
# coding: utf-8

# Q1. What is the benefit of regular expressions?
# #ans:-
# Regular expressions are useful in search and replace operations. The typical use case is to look for a sub-string that matches a pattern and replace it with something else. Most APIs using regular expressions allow you to reference capture groups from the search pattern in the replacement string
# 
# 
# Q2. Describe the difference between the effects of "(ab)c+" and "a(bc)+." Which of these, if any, is the unqualified pattern "abc+"?
# 
# 
# 
# Q3. How much do you need to use the following sentence while using regular expressions?
# 
# 
# 
# import re
# 
# #ans:-
# A regular expression (or RE) specifies a set of strings that matches it; the functions in this module let you check if a particular string matches a given regular expression (or if a given regular expression matches a particular string, which comes down to the same thing).
# 
# 
# 
# Q4. Which characters have special significance in square brackets when expressing a range, and under what circumstances?
# #ans:-
# 3 BRE Special Characters. The <period>, <left-square-bracket>, and <backslash> shall be special except when used in a bracket expression (see RE Bracket Expression). An expression containing a '[' that is unescaped and is not part of a bracket expression produces undefined results.
# 
# 
# Q5. How does compiling a regular-expression object benefit you?
# #ans:-
# Another advantage of compiling a regular expression is that, when you compile a regular expression, you can specify a number of options modifying the way that Python will treat the regular expression. Each option is defined as a constant in the re module in two forms; a long form and a single letter abbreviation.
# 
# 
# Q6. What are some examples of how to use the match object returned by re.match and re.search?
# #ans:-
# re. match attempts to match a pattern at the beginning of the string. re.search attempts to match the pattern throughout the string until it finds a match.
# # import re module
# import re
#  
# Substring ='string'
#  
#  
# String1 ='''We are learning regex with geeksforgeeks
#          regex is very useful for string matching.
#           It is fast too.'''
# String2 ='''string We are learning regex with geeksforgeeks
#          regex is very useful for string matching.
#           It is fast too.'''
#  
# # Use of re.search() Method
# print(re.search(Substring, String1, re.IGNORECASE))
# # Use of re.match() Method
# print(re.match(Substring, String1, re.IGNORECASE))
#  
# # Use of re.search() Method
# print(re.search(Substring, String2, re.IGNORECASE))
# # Use of re.match() Method
# print(re.match(Substring, String2, re.IGNORECASE))
# 
# 
# Q7. What is the difference between using a vertical bar (|) as an alteration and using square brackets as a character set?
# #ans:- 
# This allows you to apply a quantifier to the entire group or to restrict alternation to part of the regex. Only parentheses can be used for grouping. Square brackets define a character class, and curly braces are used by a quantifier with specific limits.
# 
# 
# Q8. In regular-expression search patterns, why is it necessary to use the raw-string indicator (r)? In   replacement strings?
# #ans:-
# Python raw string treats the backslash character (\) as a literal character. Raw string is useful when a string needs to contain a backslash, such as for a regular expression or Windows directory path, and you don't want it to be treated as an escape character.
# 
# 
