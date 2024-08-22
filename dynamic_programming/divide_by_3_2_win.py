def bottom_up_dp_const_mem(number: int) -> bool:
	"""
	Returns true if the current player for given number will win
	(=find a sure way to leave the other with no further action)

	Possible player actions are:
	(A) number -> number/2
	(B) number -> number/3
	(C) number -> 2/3 * number
	"""
	m, n = __get_primes_23(number)
	current = __get_first_column(m, n)
	for _ in range(n):
		previous = current
		current = __get_current_column(previous)
	return current[-1]

def __get_current_column(previous: list[bool]) -> list[bool]:
	result = [not(previous[0] and previous[1])]
	for y in range(1, len(previous) - 1):
		# abc according to list of possible actions
		a, b, c = result[y - 1], previous[y], previous[y + 1]
		is_winnable = not(a and b and c)
		result.append(is_winnable)
	return result

def __get_first_column(m: int, n: int) -> list[bool]:
	return [
		i % 2 != 0 # number can only be cut in half - last one left loses (false)
		for i in range(n + m + 1) # increased range for diagonal recursing (down left)
	]

def __get_prime_occurrence(number: int, prime: int) -> int:
	result = 0
	while number % prime == 0:
		result += 1
		number //= prime
	return result

def __get_primes_23(number: int) -> tuple[int,...]:
	"""
	pow(3, 5) -> m = 0 , n = 5
	pow(2, 6) -> m = 6 , n = 0
	"""
	return tuple(
		__get_prime_occurrence(number, prime)
		for prime in range(2, 4)
	)

########################################

def solved_with_math(number: int) -> bool:
	m, n = __get_primes_23(number)
	return m % 2 != 0 or n % 2 != 0 # provable by induction
