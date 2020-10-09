"""
Insertion: You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method to insert M into N such that M starts at bit j and ends at bit i. You can assume that the bits j through i have enough space to fit all of M. That is, if M = 10011, you can assume that there are at least 5 bits between j and i. You would not, for example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.
EXAMPLE
Input: N 10000000000, M 10011, i 2, j 6 Output:N = 10001001100
Hints: #137, #769, #215
"""


def insert(M, N, i, j):
	print("{0:b}".format(N))
	print("{0:b}".format(M))
	mask = (~0 << j) | (1 << i)-1
	result = (N & mask) | M << i
	print("{0:b}".format(result))
	return result



N = (2 ** 10) #1023
M = 19 

insert(M, N, 2, 6) #1100
