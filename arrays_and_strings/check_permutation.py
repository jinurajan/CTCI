"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
"""



def check_permutation(s1, s2):
	if len(s1) != len(s2):
		return False
	return sorted(s1.lower()) == sorted(s2.lower())




def check_permutation_using_hash(s1, s2):
	if len(s1) != len(s2):
		return False
	hash_set = {}
	for char in s1:
		hash_set[char] = hash_set.get(char, 0) + 1

	for char in s2:
		if char not in hash_set:
			return False
		hash_set[char] -= 1
		if hash_set[char] < 0:
			return False
	return True







