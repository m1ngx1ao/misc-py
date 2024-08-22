def sort(unsorted: list[int]) -> list[int]:
	wbsl = unsorted[:]
	hasChanged = True
	while hasChanged:
		hasChanged = False
		for index in range(len(wbsl) - 1):
			nextNumber = wbsl[index + 1]
			nowNumber = wbsl[index]
			if nowNumber > nextNumber:
				wbsl[index + 1] = nowNumber
				wbsl[index] = nextNumber
				hasChanged = True
	return wbsl


















