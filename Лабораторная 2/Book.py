class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id_ = id_
        self.name = name
        self.pages = None
        self._init_pages(pages)

    def _init_pages(self, pages):
        if pages <= 0:
            raise ValueError("Книга должна содержать не менее одной страницы")
        self.pages = pages

    def __str__(self):
        return f"Книга \"{self.name}\""

    def __repr__(self):
        return f"Book(id_={self.id_}, name='{self.name}', pages={self.pages})"


if __name__ == "__main__":
    new_book = Book(0, "_", 0)
