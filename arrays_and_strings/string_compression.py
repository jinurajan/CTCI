"""
String Compression: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""



def compress_string(string):
	new_string = ''
	first = 0
	last = 1
	while last < len(string):
			if string[last] == string[first]:
				last += 1
				if last == len(string):
					new_string += "{}{}".format(string[first], last-first)
					break
			else:
				new_string += "{}{}".format(string[first], last-first)
				first = last
				last += 1
	return new_string if len(new_string) < len(string) else string


print(compress_string("aabcccccaaa"))
print(compress_string("abcde"))