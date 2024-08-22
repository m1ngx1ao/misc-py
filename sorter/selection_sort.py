def sort(unsorted: list[int]) -> list[int]:
	sortedNumbers = []
	for _ in range(len(unsorted)):
		lowestNumberIndex = 0
		for index in range(1, len(unsorted)):
			if unsorted[index] < unsorted[lowestNumberIndex]:
				lowestNumberIndex = index
		sortedNumbers.append(unsorted[lowestNumberIndex])
		del unsorted[lowestNumberIndex]
	return sortedNumbers