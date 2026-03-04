class Book:

    def __init__(self, name: str, author: str):

        if not isinstance(name, str):
            raise TypeError("Название должно быть строкой")
        if not name:
            raise ValueError("Название не может быть пустым")

        if not isinstance(author, str):
            raise TypeError("Автор должен быть строкой")
        if not author:
            raise ValueError("Автор не может быть пустым")

        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга '{self.name}'. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть int")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным")

        self._pages = value

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"(name={self.name!r}, author={self.author!r}, pages={self.pages})"
        )

class AudioBook(Book):

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("Длительность должна быть числом")
        if value <= 0:
            raise ValueError("Длительность должна быть положительной")

        self._duration = float(value)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"(name={self.name!r}, author={self.author!r}, duration={self.duration})"
        )