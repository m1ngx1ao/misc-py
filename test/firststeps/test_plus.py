from firststeps import api

def test_int_plus():
	assert 13 == api.plus(6, 7)

def test_complex_plus():
	cn = api.ComplexNumber(2, 4)
	cn.plus(api.ComplexNumber(-3, 2))
	assert '(-1, 6)' == str(cn)
