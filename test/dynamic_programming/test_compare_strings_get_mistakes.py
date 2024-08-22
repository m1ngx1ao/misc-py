from dynamic_programming import compare_strings_get_mistakes as csgm

def test_one_mistake():
	assert csgm.bottom_up_dp_min_memory('LongYang', 'LongJang') == 1
	assert csgm.bottom_up_dp('LongYang', 'LongJang') == 1
	assert csgm.recursive('LongYang', 'LongJang') == 1

def test_three_mistakes():
	assert csgm.bottom_up_dp_min_memory('Lasagne', 'Banane') == 3
	assert csgm.bottom_up_dp('Lasagne', 'Banane') == 3
	assert csgm.recursive('Lasagne', 'Banane') == 3