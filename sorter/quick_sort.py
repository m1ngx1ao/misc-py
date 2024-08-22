def sort(unsorted: list[int]) -> list[int]:
	wbsl = unsorted[:]
	qs(wbsl, 0, len(wbsl) - 1)
	return wbsl
	
def qs(wbsl, left_start, right_end):
	if left_start >= right_end:
		return
	pivot_index = int((right_end + left_start) / 2)
	pivot = wbsl[pivot_index]
	front = left_start
	back = right_end
	# all left of front: left half
	# all right of back: right half
	while front <= back:
		while front <= back and wbsl[front] <= pivot:
			front += 1
		while front <= back and wbsl[back] > pivot:
			back -= 1
		if front < back:
			swap(wbsl, front, back)
	if front > right_end:
		swap(wbsl, pivot_index, right_end)
		qs(wbsl, left_start, right_end - 1)
	else:
		qs(wbsl, left_start, back)
		qs(wbsl, front, right_end)

def swap(wbsl, a, b):
	wbsl[a], wbsl[b] = wbsl[b], wbsl[a]