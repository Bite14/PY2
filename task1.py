class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    def __str__(self):
        return f'Книга {self.__name}. Автор {self.__author}'

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})'

class PaperBook (Book):
    def __init__(self, name: str, author: str, pages: int):
        self.pages = None
        self.set_pages(pages)
        super().__init__(name, author)

    def get_pages(self) -> int:
        return self.pages

    def set_pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = new_pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._Book__name!r}, author={self._Book__author!r}, pages={self.pages!r})"

class AudioBook (Book):
    def __init__(self, name: str, author: str, duration: float):
        self.duration = None
        self.set_duration(duration)
        super().__init__(name, author)

    def get_duration(self) -> float:
        return self.duration

    def set_duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность книги должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Продолжительность книги должна быть положительным числом")
        self.duration = new_duration

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self._Book__name!r}, author={self._Book__author!r}, duration={self.duration!r})'
