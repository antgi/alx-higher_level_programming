#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    Thelastdigit = number % -10
else:
    Thelastdigit = number % 10
if Thelastdigit > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, Thelastdigit))
elif Thelastdigit < 6 and Thelastdigit != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, Thelastdigit))
else:
    print("Last digit of {:d} is 0 and is 0".format(number))

