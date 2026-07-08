#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for number in my_list:
        print("{:d}".format(number))
numbers = [98, 402, -3, 5]
print_list_integer(numbers)
