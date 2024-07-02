import unittest
import pandas as pd
from hw08.booklover import BookLover
from pandas.testing import assert_frame_equal

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        my_test = BookLover("Luke","luke.nap@comcast.net","Sci-Fi")
        my_test.add_book("Song of Solomon", 5)
        expected = pd.DataFrame({
            'book_name': ["Song of Solomon"],
            'book_rating': [5]
        })
        try:
            assert_frame_equal(my_test.book_list, expected)
        except AssertionError as e:
            self.fail(f"DataFrames are not equal: {e}")
        
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        my_test = BookLover("Luke","luke.nap@comcast.net","Sci-Fi")
        my_test.add_book("Song of Solomon", 5)
        my_test.add_book("Song of Solomon", 5)
        expected = pd.DataFrame({
            'book_name': ["Song of Solomon"],
            'book_rating': [5]
        })
        try:
            assert_frame_equal(my_test.book_list, expected)
        except AssertionError as e:
            self.fail(f"DataFrames are not equal: {e}")     
        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        my_test = BookLover("Luke","luke.nap@comcast.net","Sci-Fi")
        my_test.add_book("Song of Solomon", 5)
        expected = True
        self.assertEqual(my_test.has_read("Song of Solomon"), expected)
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        my_test = BookLover("Luke","luke.nap@comcast.net","Sci-Fi")
        my_test.add_book("Song of Solomon", 5)
        message = "You haven't read this book...yet!"
        self.assertFalse(my_test.has_read("The Moon is a Harsh Mistress"), message)
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        my_test = BookLover("Luke","luke.nap@comcast.net","Sci-Fi")
        my_test.add_book("Song of Solomon", 5)
        my_test.add_book("Operation Hail Mary", 4)
        my_test.add_book("Blood Meridian", 5)
        my_test.add_book("Data and Goliath", 4)
        my_test.add_book("From Counterculture to Cyberculture",5)
        expected = 5
        self.assertEqual(my_test.num_books_read, expected)
        
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        my_test = BookLover("Luke","luke.nap@comcast.net","Sci-Fi")
        my_test.add_book("Song of Solomon", 5)
        my_test.add_book("Operation Hail Mary", 4)
        my_test.add_book("Blood Meridian", 2)
        my_test.add_book("Data and Goliath", 3)
        my_test.add_book("From Counterculture to Cyberculture", 2)
        my_test.add_book("How We Became Our Data", 2)
        expected = 5
        self.assertTrue((self.fav_books['book_rating'] > 3).all(), "Not all book ratings are greater than 3")
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)