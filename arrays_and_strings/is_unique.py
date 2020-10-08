"""
    Is Unique: Implement an algorithm to determine if a string has all unique characters. 
    What if you cannot use additional data structures?
"""

from sys import getsizeof
from math import ceil


def is_unique_using_array(string):
    hash_array = [0] * 128
    for each in string:
        if hash_array[ord(each)] == 1:
            return False
        else:
            hash_array[ord(each)] += 1
    return True


def is_unique_bitmap(string):
    # int occupies 3 bytes in python ie 24 bits. we need 6 len array here
    len_array = int(ceil(128.0 / getsizeof(int())))
    hash_array = [0] * len_array
    for each in string:
        # if a-z always index will be 4 / 5
        index = ord(each) / getsizeof(int())
        if exists(hash_array, index, ord(each)):
            return False
        else:
            set(hash_array, index, ord(each))
    return True


def exists(hash_array, index, inputvalue):
    position = inputvalue % getsizeof(int())
    return True if hash_array[index] & (1 << position) else False


def set(hash_array, index, inputvalue):
    position = inputvalue % getsizeof(int())
    hash_array[index] |= 1 << position


def unset(hash_array, index, inputvalue):
    position = inputvalue % getsizeof(int())
    hash_array[index] ^= 1 << position


if __name__ == "__main__":
    string = "abcdea"
    string1 = "abceda"
    string2 = ""
    string3 = " "
    string4 = "  "
    print is_unique_using_array(string)
    print is_unique_using_array(string1)
    print is_unique_using_array(string2)
    print is_unique_using_array(string3)
    print is_unique_using_array(string4)
    print "Using bitvectorset"
    print is_unique_bitmap(string)
    print is_unique_bitmap(string1)
    print is_unique_bitmap(string2)
    print is_unique_bitmap(string3)
    print is_unique_bitmap(string4)
