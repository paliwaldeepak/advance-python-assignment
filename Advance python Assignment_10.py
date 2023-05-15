#!/usr/bin/env python
# coding: utf-8

# Q1. What is the difference between __getattr__ and __getattribute__?
# #ans:-
# The main difference between __getattr__ and __getattribute__ is that if the attribute was not found by the usual way then __getattr__ is used. Whereas the __getattribute__ is used before looking at the actual attributes on the object.
# 
# 
# Q2. What is the difference between properties and descriptors?
# #ans:-
# descriptors are a low-level mechanism that lets you hook into an object's attributes being accessed. Properties are a high-level application of this; that is, properties are implemented using descriptors.
# 
# 
# Q3. What are the key differences in functionality between __getattr__ and __getattribute__, as well as properties and descriptors?
# #ans:-
# The main difference between __getattr__ and __getattribute__ is that if the attribute was not found by the usual way then __getattr__ is used. Whereas the __getattribute__ is used before looking at the actual attributes on the object.
# descriptors are a low-level mechanism that lets you hook into an object's attributes being accessed. Properties are a high-level application of this; that is, properties are implemented using descriptors.
# 
# 
