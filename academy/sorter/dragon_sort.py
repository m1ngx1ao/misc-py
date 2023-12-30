def sort(unsorted: list[int]) -> list[int]:
	wbsl = unsorted[:]
	step = 1
	index = 0
	while index < len(wbsl) - 1:
		nextNumber = wbsl[index + 1]
		nowNumber = wbsl[index]
		if nowNumber > nextNumber:
			wbsl[index + 1] = nowNumber
			wbsl[index] = nextNumber
			step = -1
		else:
			step = 1
		if index == 0:
			step = 1
		index += step
	return wbsl