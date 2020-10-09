from math import sqrt



def is_prime(n):
	if n < 2:
		return False
	for i in range(2, n-1):
		if n % i == 0:
			return False
	return True


def is_prime_optimized(n):
	if n < 2:
		return False
	limit = int(sqrt(n))
	for i in range(2, limit+1):
		if n % i == 0:
			return False
	return True




print(is_prime(2))
print(is_prime_optimized(2))
print(is_prime(3))
print(is_prime_optimized(3))
print(is_prime(5))
print(is_prime_optimized(5))