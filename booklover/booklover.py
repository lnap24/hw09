import pandas as pd
class BookLover():
    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = 0
        self.book_list = pd.DataFrame({'book_name': [],
                                       'book_rating': []
                                      })
    def add_book(self, book_name, rating):
        if book_name in self.book_list['book_name'].values:
            print("You've already rated this book!")
        else:
            new_book = pd.DataFrame({'book_name': [book_name],
                                 'book_rating': [rating]
                                    })
            self.book_list = pd.concat([self.book_list, new_book], 
                                       ignore_index = True)
            self.num_books +=1
    def has_read(self, book_name):
        if book_name in self.book_list['book_name'].values:
            return True
        else:
            return False
    
    #def has_read(self, book_name):
    #    return self.book_list['book_name'].isin([book_name]).any()
    
    def num_books_read(self):
        return self.num_books
    
    def fav_books(self):
        filtered_books = self.book_list[self.book_list['book_rating'] > 3]
        return filtered_books.sort_values(by = 'book_rating', ascending = False)