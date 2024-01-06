class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._init_pages(pages)

    def _init_pages(self, pages):
        if not isinstance(pages, int):
            raise ValueError("Число страниц должно быть целым числом (int)")
        if pages <= 0:
            raise ValueError("Число страниц должно быть положительным числом")
        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._init_duration(duration)

    def _init_duration(self, duration):
        if not isinstance(duration, (float, int)):
            raise ValueError("Продолжительность книги должна быть числом (float или int)")
        if duration <= 0:
            raise ValueError("Продолжительность книги должна быть положительным числом")
        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration})"


if __name__ == "__main__":
    books = [Book("Book1", "Author1"),
             PaperBook("Book2", "Author2", 100),
             AudioBook("Book3", "Author3", 1.5)]

    for book in books:
        ''' Нам не важно, какой класс у книги и другие атрибуты,
            если нужны лишь название и автор, определённые 
            в базовом классе '''
        print(type(book).__name__)
        print(book, end="\n"*2)

    for book in books:
        ''' Но можно получить строковое представление 
            объекта (для возможности воссоздания)
            с указанием всех необходимых атрибутов,
            учитывая использованный класс '''
        print(repr(book))
