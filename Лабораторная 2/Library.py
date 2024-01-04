class Library:
    def __init__(self, books=None):
        self.books = books if books is not None else []

    def get_next_book_id(self) -> int:
        if len(self.books) == 0:
            return 1
        return 1 + self.books[-1].id_

    def get_index_by_book_id(self, required_id: int) -> int:
        for i, book in enumerate(self.books):
            if book.id_ == required_id:
                return i
        raise ValueError(f"Книги с id={required_id} не существует")

    def add_book(self, book):
        self.books.append(book)


if __name__ == "__main__":
    new_lib = Library()
    new_lib.get_index_by_book_id(1)
