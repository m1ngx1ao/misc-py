from academy import heap

def test_parent():
	assert heap.get_parent(0) is None
	assert heap.get_parent(2) == 0
	assert heap.get_parent(3) == 1

def test_children():
	assert heap.get_children(0, 10) == [1, 2]
	assert heap.get_children(2, 10) == [5, 6]
	assert heap.get_children(2, 6) == [5]
	assert not heap.get_children(2, 5)

def test_heapify_empty():
	a = []
	heap.heapify(a)
	assert not a

def test_heapify_one():
	a = [1]
	heap.heapify(a)
	assert a == [1]

def test_heapify_dozen():
	a = [3, 7, 9, 1, 5, 7, 11, 1, 5, 9, 11, 3]
	heap.heapify(a)
	assert a == [11, 11, 9, 5, 9, 7, 7, 1, 1, 3, 5, 3]

def test_heapify_recursively_switch_parent():
	a = [1, 2, 3, 4]
	heap.heapify(a)
	assert a == [4, 3, 2, 1]

def test_remove_first_of_two_element_list():
	a = [2, 1]
	heap.remove_first_to_end(a, 2)
	assert a == [1, 2]

def test_remove_first_of_two_element_list_size_one():
	a = [2, 1]
	heap.remove_first_to_end(a, 1)
	assert a == [2, 1]

def test_remove_first_of_one_element_list():
	a = [1]
	heap.remove_first_to_end(a, 1)
	assert a == [1]

def test_remove_first_of_one_element_list_size_zero():
	a = [1]
	heap.remove_first_to_end(a, 0)
	assert a == [1]

def test_remove_first_of_empty_list():
	a = []
	heap.remove_first_to_end(a, 0)
	assert not a

def test_remove_first_twice_down():
	a = [5, 4, 3, 2, 1]
	heap.remove_first_to_end(a, 5)
	assert a == [4, 2, 3, 1, 5]

def test_remove_first_to_end():
	a = [12, 11, 10, 5, 9, 6, 7, 1, 3, 4, 8, 2]
	heap.remove_first_to_end(a, 12)
	assert a == [11, 9, 10, 5, 8, 6, 7, 1, 3, 4, 2, 12]
	heap.remove_first_to_end(a, 11)
	assert a == [10, 9, 7, 5, 8, 6, 2, 1, 3, 4, 11, 12]
	heap.remove_first_to_end(a, 10)
	assert a == [9, 8, 7, 5, 4, 6, 2, 1, 3, 10, 11, 12]
	heap.remove_first_to_end(a, 9)
	assert a == [8, 5, 7, 3, 4, 6, 2, 1, 9, 10, 11, 12]