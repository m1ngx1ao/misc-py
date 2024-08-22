def sort(unsorted: list[int]) -> list[int]:
	sortedList = []
	for n in unsorted:
		index = 0
		while index < len(sortedList) and n > sortedList[index]:
			index += 1
		sortedList.insert(index, n)
	return sortedList















