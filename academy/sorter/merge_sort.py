def sort(unsorted: list[int]) -> list[int]:
	if len(unsorted) <= 1:
		return unsorted
	right_start_index = len(unsorted) // 2
	left = unsorted[:right_start_index]
	right = unsorted[right_start_index:]
	left = sort(left)
	right = sort(right)
	sortedList = []
	indexLeft = indexRight = 0
	while indexLeft < len(left) and indexRight < len(right):
		if left[indexLeft] <= right[indexRight]:
			sortedList.append(left[indexLeft])
			indexLeft += 1
		else:
			sortedList.append(right[indexRight])
			indexRight += 1
	sortedList += left[indexLeft:] + right[indexRight:]
	return sortedList