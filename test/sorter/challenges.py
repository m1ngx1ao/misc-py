DOZEN = [3, 6, 9, 12, 4, 7, 10, 1, 5, 8, 11, 2]
DOZEN_SORTED = sorted(DOZEN)
DOZEN_W_DUPLICATES = [3, 7, 9, 1, 5, 7, 11, 1, 5, 9, 11, 3]
DOZEN_W_DUPLICATES_SORTED = sorted(DOZEN_W_DUPLICATES)
FIFTEEN = [3, 6, 9, 12, 15, 4, 7, 10, 13, 1, 5, 8, 11, 14, 2]
FIFTEEN_SORTED = sorted(FIFTEEN)

MASS_SIZE_EXP = 5
def norm_num(i):
	return (('0' * MASS_SIZE_EXP) + str(i))[-MASS_SIZE_EXP:]

MASS = [int(norm_num(i)[::-1]) for i in range(10 ** MASS_SIZE_EXP)]
MASS_SORTED = list(range(10 ** MASS_SIZE_EXP))

MASS_ALMOST_SORTED = [i ^ 1 for i in MASS_SORTED]

def empty(sorter):
	assert [] == sorter.sort([])

def dozen(sorter):
	assert DOZEN_SORTED == sorter.sort(DOZEN[::])

def dozen_with_duplicates(sorter):
	assert DOZEN_W_DUPLICATES_SORTED == sorter.sort(DOZEN_W_DUPLICATES[::])

def fifteen(sorter):
	assert FIFTEEN_SORTED == sorter.sort(FIFTEEN[::])

def mass(sorter):
	assert MASS_SORTED == sorter.sort(MASS[::])

def mass_almost_sorted(sorter):
	assert MASS_SORTED == sorter.sort(MASS_ALMOST_SORTED[::])
