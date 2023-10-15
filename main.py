from Library import Library
from book import Book
def main():
    my_library = Library()

    while True:
        print("\nСистема управления библиотекой")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Список книг")
        print("4. Найти по названию")
        print("5. Найти по автору")
        print("6. Найти по году выпуска")
        print("7. Выход")

        choice = input("Введите ваш выбор: ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Год выпуска: ")
            new_book = Book(title, author, year)
            my_library.add_book(new_book)
        elif choice == "2":
            title = input("Введите название книги, которую нужно удалить: ")
            my_library.remove_book(title)
        elif choice == "3":
            my_library.list_books()
        elif choice == "4":
            title = input("Введите заголовок для поиска: ")
            my_library.search_by_title(title)
        elif choice == "5":
            author = input("Введите автора для поиска: ")
            my_library.search_by_author(author)
        elif choice == "6":
            year = input("Введите год для поиска: ")
            my_library.search_by_year(year)
        elif choice == "7":
            print("Пока!")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте еще раз.")

if __name__ == "__main__":
    main()