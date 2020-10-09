"""
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. (Note: if implementing in Java, please use a character array so that you can perform this operation in place.)
EXAMPLE
Input: "Mr John Smith ", 13 Output: "Mr%20John%20Smith"
"""
import ctypes


def urlify(s, length):
	count = 0 
	for i in range(length):
		if s[i] == " ":
			count += 1
	index = length + count*2
	if length < len(s):
		s[length] = '\0'
	for i in range(length-1, -1, -1):
		if s[i] == ' ':
			s[index-1] = '0'
			s[index-2] = '2'
			s[index-3] = '%'
			index -= 3
		else:
			s[index-1] = s[i]
			index -= 1

string = "Mr John Smith      "
mutable = ctypes.create_string_buffer(string)
urlify(mutable, 13)
print(mutable.value)