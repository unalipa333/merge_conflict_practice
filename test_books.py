import pytest

from book_class import *


@pytest.fixture
def my_library():
	my_library = Booklist()

	# add the books
	my_library.add(title = 'Just Mercy', author = 'Bryan Stevenson')
	my_library.add(title = 'The New Jim Crow', author = 'Michelle Alexander')
	my_library.add(title = 'The Truths We Hold', author = 'Kamala Harris')
	my_library.add(title = "My Grandmother's Hands", author = 'Resmaa Menakem')

	return(my_library)

# make sure count_books() method works
def test_count_books(my_library):
	assert my_library.count_books() == 4, 'Book count incorrect!'

# make sure remove_title() and display_titles() methods work
def test_remove_title(my_library):
	my_library.remove_title('Just Mercy')
	expected_titles = ["My Grandmother's Hands", "The New Jim Crow","The Truths We Hold"]
	assert my_library.display_titles() == expected_titles, 'Did not remove book correctly!'
