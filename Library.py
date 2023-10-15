class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Добавлен: {book}")

    def remove_book(self, title):
        removed_books = [book for book in self.books if book.title == title]
        if removed_books:
            self.books = [book for book in self.books if book.title != title]
            print(f"Удаленный {len(removed_books)} book(s) with the title '{title}'")
        else:
            print(f"Нет книг с таким названием '{title}' found.")

    def list_books(self):
        if not self.books:
            print("Библиотека пуста.")
        else:
            print("Библиотечные книги:")
            for book in self.books:
                print(book)

    def search_by_title(self, title):
        found_books = [book for book in self.books if book.title == title]
        if found_books:
            print(f"Найденный {len(found_books)} книга(и) с названием '{title}':")
            for book in found_books:
                print(book)
        else:
            print(f"Нет книг с таким названием '{title}' Найденный.")

    def search_by_author(self, author):
        found_books = [book for book in self.books if book.author == author]
        if found_books:
            print(f"Найденный {len(found_books)} книга(и) автора '{author}':")
            for book in found_books:
                print(book)
        else:
            print(f"Нет книг автора '{author}' Найденный.")

    def search_by_year(self, year):
        found_books = [book for book in self.books if book.year == year]
        if found_books:
            print(f"Найденный {len(found_books)} книга(и), изданная в году {year}:")
            for book in found_books:
                print(book)
        else:
            print(f"Ни одной книги, изданной в этом году {year} найденный.")