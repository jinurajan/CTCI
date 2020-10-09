"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat'; "atc o eta·; etc.)
"""

def is_palindrome_permutation(s):
	hash_set = {}
	for char in s:
		if char == " ":
			continue
		hash_set[char.lower()] = hash_set.get(char.lower(), 0) + 1

	odd_count = 0
	for key, value in hash_set.items():
		if value % 2 == 1:
			odd_count += 1
		if odd_count > 1:
			return False
	return True


def is_palindrome_permutation_using_bit_vector(s):
	bit_vector = 0
	for char in s:
		if char == " ":
			continue
		bit_vector = toggle(bit_vector, ord(char.lower()) - ord('a'))
	return bit_vector & (bit_vector-1) == 0


def toggle(bit_vector, index):
	mask = 1 << index
	if bit_vector & mask == 0:
		# not set set it
		bit_vector  |= mask
	else:
		bit_vector &= ~ mask
	return bit_vector




print(is_palindrome_permutation('Tact Coa'))
print(is_palindrome_permutation_using_bit_vector('Tact Coa'))
print(is_palindrome_permutation_using_bit_vector('aa'))