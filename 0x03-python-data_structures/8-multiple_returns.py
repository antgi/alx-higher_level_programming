#!/usr/bin/python3
def multiple_returns(sentence):
    My_tuple = ()
    if len(sentence) == 0:
        My_tuple = 0, "None"
    else:
        My_tuple = len(sentence), sentence[0]
    return My_tuple
