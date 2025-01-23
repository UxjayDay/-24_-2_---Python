# TODO Написать 3 класса с документацией и аннотацией типов

from abc import ABC, abstractmethod
from typing import List, Optional

class Book(ABC):
    """
    Абстрактный класс, описывающий книгу.
    """

    def __init__(self, title: str, author: str, pages: int):
        """
        Инициализация объекта книги.

        :param title: Название книги.
        :param author: Автор книги.
        :param pages: Количество страниц в книге.
        :raises ValueError: Если количество страниц меньше или равно 0.
        """
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self.title = title
        self.author = author
        self.pages = pages

    @abstractmethod
    def read(self, page: int) -> str:
        """
        Прочитать страницу книги.

        :param page: Номер страницы для чтения.
        :return: Содержание страницы.
        :raises ValueError: Если номер страницы выходит за пределы книги.
        """
        ...

    @abstractmethod
    def get_info(self) -> str:
        """
        Получить информацию о книге.

        :return: Строка с информацией о книге.
        """
        ...

class Cat(ABC):
    """
    Абстрактный класс, описывающий кошку.
    """

    def __init__(self, name: str, age: int, color: str):
        """
        Инициализация объекта кошки.

        :param name: Имя кошки.
        :param age: Возраст кошки в годах.
        :param color: Цвет шерсти кошки.
        :raises ValueError: Если возраст меньше 0.
        """
        if age < 0:
            raise ValueError("Возраст кошки не может быть отрицательным.")
        self.name = name
        self.age = age
        self.color = color

    @abstractmethod
    def meow(self) -> str:
        """
        Кошка издает звук "мяу".

        :return: Строка с звуком, который издает кошка.
        """
        ...

    @abstractmethod
    def sleep(self, hours: float) -> None:
        """
        Кошка спит указанное количество часов.

        :param hours: Количество часов сна.
        :raises ValueError: Если количество часов меньше или равно 0.
        """
        ...

class Earth(ABC):
    """
    Абстрактный класс, описывающий планету Земля.
    """

    def __init__(self, population: int, continents: List[str]):
        """
        Инициализация объекта Земли.

        :param population: Население Земли.
        :param continents: Список континентов на Земле.
        :raises ValueError: Если население меньше 0 или список континентов пуст.
        """
        if population < 0:
            raise ValueError("Население не может быть отрицательным.")
        if not continents:
            raise ValueError("Список континентов не может быть пустым.")
        self.population = population
        self.continents = continents

    @abstractmethod
    def add_population(self, amount: int) -> None:
        """
        Увеличить население Земли на указанное количество.

        :param amount: Количество людей для добавления.
        :raises ValueError: Если количество меньше или равно 0.
        """
        ...

    @abstractmethod
    def get_continent_info(self, continent: str) -> Optional[str]:
        """
        Получить информацию о континенте.

        :param continent: Название континента.
        :return: Информация о континенте, если он существует, иначе None.
        """
        ...

if __name__ == "__main__":
    import doctest

    doctest.testmod()  # тестирование примеров, которые находятся в документации

