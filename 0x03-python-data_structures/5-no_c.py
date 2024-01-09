#!/usr/bin/python3
def no_c(my_string):
    The_new_string = my_string.translate({ord(i): None for i in 'cC'})
    return The_new_string
