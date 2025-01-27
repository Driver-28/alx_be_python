class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"Book: "
class EBook(Book):
    def __init__(self, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    def __str__(self):
        return f"EBook: "
class PrintBook(Book):
    def __init__(self, page_count):
        super().__init__(page_count)
        self.page_count = page_count
    def __str__(str):
        return f"PrintBook: "
class  Library:
    def __init__(self, books):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def list_books(self):
        for book in self.books:
            print (book)
