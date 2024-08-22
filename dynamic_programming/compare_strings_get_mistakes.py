import functools as ft

print('starting...')

# North and South (tuniques bleues?): y axis increases when moving up
N = (0, 1)
S = (0, -1)
E = (1, 0)
W = (-1, 0)

TTuple = tuple[int, int]
def tuple_add(a: TTuple, b: TTuple, c: TTuple = (0, 0)):
	a1, a2 = a
	b1, b2 = b
	c1, c2 = c
	return a1 + b1 + c1, a2 + b2 + c2

#####################
# runtime O(3^(n+m))
# memory  O(n+m)
#####################

@ft.cache
def __recursive(words: tuple[str, str], prefix_len: TTuple) -> int:
	if min(prefix_len) == 0:
		return max(prefix_len)
	rook_candidate = 1 + min(
		__recursive(words, tuple_add(prefix_len, d))
		for d in [W, S]
	)
	bishop_pos = tuple_add(prefix_len, S, W)
	bishop_pos_chars = set(w[bpi] for w, bpi in zip(words, bishop_pos))
	bishop_candidate = __recursive(words, bishop_pos) + len(bishop_pos_chars) - 1
	return min(rook_candidate, bishop_candidate)

def recursive(word1: str, word2: str) -> int:
	return __recursive((word1, word2), (len(word1), len(word2)))

#####################
# runtime O(n*m)
# memory  O(n*m)
#####################

def __bottom_up_dp_get_best_error_count(d: dict, words: tuple[str, str], prefix_len: tuple[int, int]) -> int:
	rook_candidate = 1 + min(d[tuple_add(prefix_len, S)], d[tuple_add(prefix_len, W)])
	position = tuple_add(prefix_len, S, W)
	chars = set(w[p] for w, p in zip(words, position))
	bishop_candidate = len(chars) - 1 + d[tuple_add(prefix_len, S, W)]
	return min(rook_candidate, bishop_candidate)

def __bottom_up_dp_get_basis_dict(words_len: TTuple) -> dict[TTuple, int]:
	word1_len, word2_len = words_len
	d = {}
	for x in range(word1_len):
		d[x, 0] = x
	for y in range(1, word2_len):
		d[0, y] = y
	return d

def __bottom_up_dp(words: tuple[str, str], words_len: TTuple) -> int:
	word1_len, word2_len = words_len
	d = __bottom_up_dp_get_basis_dict(words_len)
	for y in range(1, word2_len):
		for x in range(1, word1_len):
			d[x, y] = __bottom_up_dp_get_best_error_count(d, words, (x, y))
	return d[word1_len - 1, word2_len - 1]

def bottom_up_dp(word1: str, word2: str) -> int:
	return __bottom_up_dp((word1, word2), (len(word1), len(word2)))

#####################
# runtime O(n*m)
# memory  O(n+m)
#####################

def __bottom_up_dp_min_memory_get_best_error_count(prefix_len: tuple[int, int],
		words: tuple[str, str], current: list[int], previous: list[int]) -> int:
	x, _ = prefix_len
	rook_candidate = 1 + min(current[x - 1], previous[x])
	position = tuple_add(prefix_len, S, W)
	chars = set(w[p] for w, p in zip(words, position))
	bishop_candidate = len(chars) - 1 + previous[x - 1]
	return min(rook_candidate, bishop_candidate)

def __bottom_up_dp_min_memory(words: tuple[str, str], words_len: TTuple) -> int:
	word1_len, word2_len = words_len
	current = list(range(word1_len + 1))
	for y in range(1, word2_len + 1):
		previous = current
		current = [previous[0] + 1]
		for x in range(1, word1_len + 1):
			current.append(__bottom_up_dp_min_memory_get_best_error_count((x, y), words, current, previous))
	return current[-1]

def bottom_up_dp_min_memory(word1: str, word2: str) -> int:
	return __bottom_up_dp_min_memory((word1, word2), (len(word1), len(word2)))
