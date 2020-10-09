"""
One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
EXAMPLE
pale, ple true pales, pale -> true pale, bale -> true pale, bae -> false
"""


def one_edit_away(s1, s2):
	n1 = len(s1)
	n2 = len(s2)
	if abs(len(s1)-len(s2)) > 1:
		return False
	first = s1 if n1 > n2 else s2
	sec = s1 if first is s2 else s2
	hash_set = {}
	for char in first:
		hash_set[char] = hash_set.get(char, 0) + 1
	not_found = 0
	for char in sec:
		if char not in hash_set:
			not_found += 1
			if not_found > 1:
				return False
			continue
		hash_set[char] -= 1
		if hash_set[char] < 0 :
			return False
	extra_val = 0
	for key, value in hash_set.items():
		if value == 1:
			extra_val += 1
	return extra_val <= 1

print(one_edit_away('pale', 'ple'))
print(one_edit_away('pales', 'pale'))
print(one_edit_away('pale', 'bale'))
print(one_edit_away('pale', 'bae'))
