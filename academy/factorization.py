def factorize(n: int) -> list[int]:
	l = []
	i = 2
	while i <= n:
		if n % i == 0:
			n = n // i
			l = l + [i]
		else:
			i = i + 1
	if l:
		return l
	return [n]		

def factorize_to_str(n: int) -> str:
	return '1'

def is_prime(n: int) -> bool:
	return len(factorize(n)) < 2

def gcf(m: int, n: int) -> int:
	firstFactors = factorize(m)
	secondFactors = factorize(n)
	pointerTwo = 0
	commonFactors = []
	for factor in firstFactors:
		while pointerTwo < len(secondFactors) and factor > secondFactors[pointerTwo]:
			pointerTwo += 1
		if pointerTwo < len(secondFactors) and factor == secondFactors[pointerTwo]:
			commonFactors.append(factor)
			pointerTwo += 1
	result = 1 
	for factor in commonFactors:
		result *= factor
	return result

def gcfcv(m: int, n: int) -> int:
	if n > m:
		m, n = n, m
	while n != 0:
		newn = m % n
		m = n
		n = newn
	return m

def lcm(m: int, n: int) -> int:
	firstFactors = factorize(m)
	secondFactors = factorize(n)
	secondLength = len(secondFactors)
	indexSecond = 0
	result = 1
	for firstFactor in firstFactors:
		while indexSecond < secondLength and secondFactors[indexSecond] < firstFactor:
			result *= secondFactors[indexSecond]
			indexSecond += 1
		result *= firstFactor
		if indexSecond < secondLength and secondFactors[indexSecond] == firstFactor:
			indexSecond += 1
	while indexSecond < secondLength:
		result *= secondFactors[indexSecond]
		indexSecond += 1
	return result