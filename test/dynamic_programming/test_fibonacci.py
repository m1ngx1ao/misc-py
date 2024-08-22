from dynamic_programming import fibonacci as fib

def test_five():
	assert fib.recursive(5) == 5
	assert fib.memoized_recursive(5) == 5
	assert fib.top_down_dp(5, {}) == 5
	assert fib.bottom_up_dp(5) == 5
	assert fib.bottom_up_const_memory_dp(5) == 5

def test_twenty():
	assert fib.recursive(20) == 6765
	assert fib.memoized_recursive(20) == 6765
	assert fib.top_down_dp(20, {}) == 6765
	assert fib.bottom_up_dp(20) == 6765
	assert fib.bottom_up_const_memory_dp(20) == 6765