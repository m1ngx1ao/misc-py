from academy import heap

def sort(unsorted: list[int]) -> list[int]:
	wbsl = unsorted[:]
	heap.heapify(wbsl)
	for size in range(len(wbsl), 0, -1):
		heap.remove_first_to_end(wbsl, size)
	return wbsl