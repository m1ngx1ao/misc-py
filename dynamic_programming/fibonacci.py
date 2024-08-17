import time
import functools as ft

index = 20
#############################
# runtime O(2 ^ n)
# memory O(1)
#############################

def recursive(n: int) -> int:
	if n <= 1:
		return n
	return recursive(n - 1) + recursive (n - 2)

start = time.time()
end = time.time()
#print(recursive(index))
print(end - start)

#############################
# runtime O(n)
# memory O(n)
#############################

@ft.cache
def memoized_recursive(n: int) -> int:
	if n <= 1:
		return n
	return recursive(n - 1) + recursive (n - 2)

start = time.time()
end = time.time()
print(memoized_recursive(index))
print(end - start)

def top_down_dp(n: int, d: dict[int, int]) -> int:
	if n in d:
		return d[n]
	if n in (0, 1):
		d[n] = n
	else:
		d[n] = top_down_dp(n - 1, d) + top_down_dp(n - 2, d)
	return d[n]

start = time.time()
end = time.time()
print(top_down_dp(index, {}))
print(end - start)

#############################
# runtime O(n)
# memory O(n)
#############################

def bottom_up_dp(n: int) -> int:
	fib_numbers = [0, 1]
	for i in range(2, n + 1):
		fib_numbers.append(fib_numbers[i - 1] + fib_numbers[i - 2])
	return fib_numbers[n]

start = time.time()
print(bottom_up_dp(index))
end = time.time()
print(end - start)

#############################
# runtime O(n)
# memory O(1)
#############################

def bottom_up_const_memory_dp(n: int) -> int:
	if n <= 1:
		return n
	a = 0
	b = 1
	for _ in range(2, n + 1):
		c = a + b
		a = b
		b = c
	return c

start = time.time()
print(bottom_up_const_memory_dp(index))
end = time.time()
print(end - start)