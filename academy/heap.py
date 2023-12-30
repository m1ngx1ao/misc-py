def get_parent(idx: int) -> int | None:
	return (idx - 1) // 2 if idx else None

def get_children(idx: int, heap_size: int) -> list[int]:
	return [r for r in [idx * 2 + 1, idx * 2 + 2] if r < heap_size]
		
def heapify(a: list[int]):
	if len(a) < 2:
		return
	for new_index in range(len(a)):
		idx = new_index
		while (parent_idx := get_parent(idx)) is not None and a[idx] > a[parent_idx]:
			swap(a, idx, parent_idx)
			idx = parent_idx

def remove_first_to_end(h: list[int], size):
	if size < 2:
		return
	swap(h, 0, size - 1)
	idx = 0
	while (best_idx := get_best_idx_of_me_children(h, idx, size - 1)) != idx:
		swap(h, best_idx, idx)
		idx = best_idx

def get_best_idx_of_me_children(a: list[int], idx: int, size: int):
	best_idx = idx
	for child_idx in get_children(idx, size):
		if a[child_idx] > a[best_idx]:
			best_idx = child_idx
	return best_idx

def swap(l, a, b):
	l[a], l[b] = l[b], l[a]