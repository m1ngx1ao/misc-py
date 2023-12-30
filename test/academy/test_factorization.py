from academy import factorization as fct

def test_one_factors():
	assert [1] == fct.factorize(1)

def test_seven_factors():
	assert [7] == fct.factorize(7)

def test_twelve_factors():
	assert [2, 2, 3] == fct.factorize(12)

def test_primes():
	assert fct.is_prime(1)
	assert fct.is_prime(7)
	assert not fct.is_prime(12)

def test_greatest_common_factor_with_pointer():
	assert 1 == fct.gcf(3, 5)
	assert 3 == fct.gcf(111, 51)
	assert 4 == fct.gcf(12, 16)

def test_greatest_common_factor_chinese_variant():
	assert 1 == fct.gcfcv(3, 5)
	assert 3 == fct.gcfcv(111, 51)
	assert 4 == fct.gcfcv(12, 16)

def test_least_common_multiple():
	assert 1887 == fct.lcm(111, 51)
	assert 15 == fct.lcm(3, 5)
	assert 48 == fct.lcm(12, 16)
	assert 48 == fct.lcm(12, 48)
	assert 256 == fct.lcm(32, 256)
	assert 5000 == fct.lcm(625, 8)
	assert 6000 == fct.lcm(1500, 48)

def test_factorization_string():
	assert '7' == fct.factorize_to_str(7)
	assert '2^2 * 3' == fct.factorize_to_str(12)
	assert '2^3 * 3^2 * 5' == fct.factorize_to_str(360)
