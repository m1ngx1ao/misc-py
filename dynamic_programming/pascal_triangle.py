import functools as ft

print('starting...')

#####################
# runtime O(2^n)
# memory  O(1)
#####################

def recursive(n: int, k: int) -> int:
	if n == 0 or k in (0, n):
		return 1
	return recursive(n - 1, k - 1) + recursive(n - 1, k)

#####################
# runtime O(n^2)
# memory  O(n^2)
#####################

@ft.cache
def memoized_recursive(n: int, k: int) -> int:
	if n == 0 or k in (0, n):
		return 1
	return memoized_recursive(n - 1, k - 1) + memoized_recursive(n - 1, k)

#####################
# runtime O(n^2)
# memory  O(n^2)
#####################

def top_down_dp(n: int, k: int, lookup: dict[tuple[int, int], int]) -> int:
	nk = n, k
	if nk in lookup:
		return lookup[nk]
	if n == 0 or k in (0, n):
		lookup[nk] = 1
	else:
		lookup[nk] = top_down_dp(n - 1, k - 1, lookup) + top_down_dp(n - 1, k, lookup)
	return lookup[nk]

#####################
# runtime O(n^2)
# memory  O(n^2)
#####################

def bottom_up_dp(n: int, k: int) -> int:
	pascal = {}
	for nn in range(n + 1):
		for kk in range(nn + 1):
			if nn == 0 or kk in (0, nn):
				pascal[nn, kk] = 1
			else:
				pascal[nn, kk] = pascal[nn - 1, kk - 1] + pascal[nn - 1, kk]
	return pascal[n, k]

#####################
# runtime O(n^2)
# memory  O(1)
#####################

def bottom_up_dp_const_memory(n: int, k: int) -> int:
	old_line = [1]
	for nn in range(1, n + 1):
		new_line = []
		for kk in range(nn + 1):
			if kk in (0, nn):
				new_line.append(1)
			else:
				new_line.append(old_line[kk - 1] + old_line[kk])
		old_line = new_line
	return old_line[k]
