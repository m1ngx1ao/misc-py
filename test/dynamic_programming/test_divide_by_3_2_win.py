from dynamic_programming import divide_by_3_2_win as dbttw

def test_2_even_3_zero():
	assert not dbttw.bottom_up_dp_const_mem(2 ** 4)
	assert not dbttw.bottom_up_dp_const_mem(2 ** 8)
	assert not dbttw.solved_with_math(2 ** 8)

def test_2_odd_3_zero():
	assert dbttw.bottom_up_dp_const_mem(2 ** 3)
	assert dbttw.bottom_up_dp_const_mem(2 ** 5)
	assert dbttw.solved_with_math(2 ** 5)

def test_2_zero_3_even():
	assert not dbttw.bottom_up_dp_const_mem(3 ** 4)
	assert not dbttw.bottom_up_dp_const_mem(3 ** 8)
	assert not dbttw.solved_with_math(3 ** 8)

def test_2_zero_3_odd():
	assert dbttw.bottom_up_dp_const_mem(3 ** 3)
	assert dbttw.bottom_up_dp_const_mem(3 ** 5)
	assert dbttw.solved_with_math(3 ** 5)

def test_2_even_3_even():
	assert not dbttw.bottom_up_dp_const_mem((2 ** 2) * (3 ** 2))
	assert not dbttw.bottom_up_dp_const_mem((2 ** 10) * (3 ** 6))
	assert not dbttw.solved_with_math((2 ** 10) * (3 ** 6))

def test_2_odd_3_even():
	assert dbttw.bottom_up_dp_const_mem((2 ** 3) * (3 ** 2))
	assert dbttw.bottom_up_dp_const_mem((2 ** 5) * (3 ** 6))
	assert dbttw.solved_with_math((2 ** 5) * (3 ** 6))

def test_2_even_3_odd():
	assert dbttw.bottom_up_dp_const_mem((2 ** 2) * (3 ** 5))
	assert dbttw.bottom_up_dp_const_mem((2 ** 10) * (3 ** 11))
	assert dbttw.solved_with_math((2 ** 10) * (3 ** 11))

def test_2_odd_3_odd():
	assert dbttw.bottom_up_dp_const_mem((2 ** 3) * (3 ** 5))
	assert dbttw.bottom_up_dp_const_mem((2 ** 5) * (3 ** 11))
	assert dbttw.solved_with_math((2 ** 5) * (3 ** 11))
