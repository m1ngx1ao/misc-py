#import functools as ft

print('starting...')

first = 'Lasagne'
first_length = len(first)
second = 'Banane'
second_length = len(second)

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

print(recursive(first, second))
