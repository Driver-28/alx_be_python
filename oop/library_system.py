class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
class Ebook(Book):
    def __init__(self, file_size):
        super().__init__(title, author)
        self.file_size = file_size
class PrintBook(Book):
    def __init__(self, page_count):
        super().__init__(page_count)
        self.page_count = page_count
class  Library:
    def __init__(self, books):
        self.books = books
    def add_book(self, book):

    def list_books(self):
