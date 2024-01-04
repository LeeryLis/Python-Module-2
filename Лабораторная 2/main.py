import random

from Book import Book
from Library import Library


def main():
    great_library = Library()

    names_list = ["First", "Second", "Nothing", "The Book", "Анекдоты"]
    for name in names_list:
        id_ = great_library.get_next_book_id()
        book = Book(id_=id_, name=name, pages=random.randint(1, 500))
        great_library.add_book(book)

    for book in great_library.books:
        print(f"id=[{book.id_}] {book} {book.pages} стр.")

    print()
    taken_id = 3
    taken_index = great_library.get_index_by_book_id(taken_id)
    print(f"id={taken_id} -> index={taken_index}")
    taken_book = great_library.books[taken_index]
    print(repr(taken_book))


if __name__ == "__main__":
    main()
