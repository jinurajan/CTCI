"""
The sieve of Eratosthenes
"""
from math import sqrt


def generate_primes(max):
	flags = [1] * (max+1)
	prime = 2
	while prime <= sqrt(max):
		crossoff(flags, prime)
		prime = get_next_prime(flags, prime) 
	return [i for i in range(2, len(flags)) if flags[i] == 1]


def crossoff(flags, prime):
	for i in range(prime*prime, len(flags), prime):
		flags[i] = 0


def get_next_prime(flags, prime):
	next = prime + 1
	while next < len(flags) and flags[next] != 1:
		next += 1
	return next




import pdb; pdb.set_trace()
print(generate_primes(10))