#!/usr/bin/env python3

# Define a Person class in lib/person.py. In the class, define an __init__ method that accepts an argument for the person's name. That argument should be stored within a self.name attribute

class Person:
    def __init__(self, name):
        self.name = name


mati = Person('Mati')
print(mati.name)
