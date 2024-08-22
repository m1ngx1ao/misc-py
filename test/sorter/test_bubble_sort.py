import challenges
from sorter import bubble_sort as sorter

def test_empty():
	challenges.empty(sorter)

def test_dozen():
	challenges.dozen(sorter)

def test_dozen_with_duplicates():
	challenges.dozen_with_duplicates(sorter)

def test_fifteen():
	challenges.fifteen(sorter)

def test_mass():
	...
	# takes a minute
	#challenges.mass(sorter)

def test_mass_almost_sorted():
	...
	# takes a minute
	#challenges.mass_almost_sorted(sorter)
