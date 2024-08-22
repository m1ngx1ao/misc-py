from dynamic_programming import pascal_triangle_v0 as ptv

def test_n_2_k_1():
	assert ptv.get_result(2, 1) == 2
	assert ptv.get_result_slower(2, 1) == 2

def test_n_22_k_13():
	assert ptv.get_result(22, 13) == 497420
	assert ptv.get_result_slower(22, 13) == 497420

def test_n_10000_k_88():
 res = 36724997600468624596335407583496306067134037998817200329438020517352863208620561740850159350058066878341314585780415251323402600119259291080426566234176420182545801958052738650270327089842628908880408017521199623980000
 assert ptv.get_result(10000, 88) == res
 assert ptv.get_result_slower(10000, 88) == res