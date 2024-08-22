import challenges
from sorter import merge_sort as sorter

def test_empty():
	challenges.empty(sorter)

def test_dozen():
	challenges.dozen(sorter)

def test_dozen_with_duplicates():
	challenges.dozen_with_duplicates(sorter)

def test_fifteen():
	challenges.fifteen(sorter)

def test_mass():
	challenges.mass(sorter)

def test_mass_almost_sorted():
	challenges.mass_almost_sorted(sorter)
