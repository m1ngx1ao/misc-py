from dynamic_programming import minimum_coins_for_sum as mcfs

mcfs.coins = [1, 7, 5]

def test_eleven():
	#assert mcfs.dummy(11) == 3
	assert mcfs.recursive(11) == 3
	assert mcfs.memoized_recursive(11) == 3
	assert mcfs.top_down_dp(11, {}) == 3
	assert mcfs.bottom_up_dp(11) == 3
	assert mcfs.bottom_up_dp_constant_memory(11) == 3

mcfs.coins = [6, 4, 1]

def test_nine():
	#assert mcfs.dummy(9) == 3
	assert mcfs.recursive(9) == 3
	assert mcfs.memoized_recursive(9) == 3
	assert mcfs.top_down_dp(9, {}) == 3
	assert mcfs.bottom_up_dp(9) == 3
	assert mcfs.bottom_up_dp_constant_memory(9) == 3