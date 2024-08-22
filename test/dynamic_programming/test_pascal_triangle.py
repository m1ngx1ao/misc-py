from dynamic_programming import pascal_triangle as pt

def test_n_2_k_1():
	assert pt.recursive(2, 1) == 2
	assert pt.memoized_recursive(2, 1) == 2
	assert pt.top_down_dp(2, 1, {}) == 2
	assert pt.bottom_up_dp(2, 1) == 2
	assert pt.bottom_up_dp_const_memory(2, 1) == 2

def test_n_22_k_13():
	assert pt.recursive(22, 13) == 497420
	assert pt.memoized_recursive(22, 13) == 497420
	assert pt.top_down_dp(22, 13, {}) == 497420
	assert pt.bottom_up_dp(22, 13) == 497420
	assert pt.bottom_up_dp_const_memory(22, 13) == 497420

def test_n_10000_k_88():
	res = 36724997600468624596335407583496306067134037998817200329438020517352863208620561740850159350058066878341314585780415251323402600119259291080426566234176420182545801958052738650270327089842628908880408017521199623980000
	# takes about 30sec
	#assert pt.bottom_up_dp_const_memory(10000, 88) == res
