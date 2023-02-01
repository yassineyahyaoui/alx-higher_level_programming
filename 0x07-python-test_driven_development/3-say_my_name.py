#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    if first_name is None or type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if last_name is None or type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print("My name is {:s} {:s}".format(first_name, last_name))
