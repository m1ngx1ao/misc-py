import functools as ft

coins = [1, 7, 5]
target = 11

print('starting...')

def dummy(n: int) -> int:
	rest = n
	counter = 0
	for c in sorted(coins, reverse=True):
		while c <= rest:
			rest -= c
			counter += 1
	return counter

print(dummy(target))

#####################
# runtime O(2^n)
# memory  O(1)
#####################

def recursive(n : int) -> int:
	if n == 0:
		return 0	
	return 1 + min(
		recursive(n - coin)
		for coin in coins
		if n - coin >= 0
	)

print(recursive(target))	

#####################
# runtime O(n)
# memory  O(n)
#####################

@ft.cache
def memoized_recursive(n : int) -> int:
	if n == 0:
		return 0	
	return 1 + min(
		memoized_recursive(n - coin)
		for coin in coins
		if n - coin >= 0
	)	

print(memoized_recursive(target))	

#####################
# runtime O(n)
# memory  O(n)
#####################

def top_down_dp(n : int, d: dict[int, int]) -> int:
	if n in d:
		return d[n]
	if n == 0:
		d[n] = 0
	else: 
		d[n] = 1 + min(
			top_down_dp(n - coin, d)
			for coin in coins
			if n - coin >= 0
		)
	return d[n]

print(top_down_dp(target, {}))

#####################
# runtime O(n)
# memory  O(n)
#####################

def bottom_up_dp(n : int) -> int:
	coins_needed = [0]
	for i in range(1, n + 1):
		coins_needed.append(
			1 + min(
				coins_needed[i - coin]
				for coin in coins
				if i - coin >= 0
			)
		)
	return coins_needed[n]

print(bottom_up_dp(target))	

#####################
# runtime O(n)
# memory  O(1)
#####################

def bottom_up_dp_constant_memory(n : int) -> int:
	biggest_coin = max(coins)
	coins_needed = [0] * biggest_coin
	for i in range(1, n + 1):
		coins_needed[i % biggest_coin] = 1 + min(
			coins_needed[(i - coin) % biggest_coin]
			for coin in coins
			if i - coin >= 0
		)
	return coins_needed[n % biggest_coin]

print(bottom_up_dp_constant_memory(target))	
