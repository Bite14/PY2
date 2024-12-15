import doctest

class Dachshund:
    def __init__(self, color: str, name: str):
        """
        Создание и подготовка к работе объекта "Такса"

        :param color: Цвет таксы
        :param name: кличка

        Примеры:
        >>> dog = Dachshund('чёрно-коричневая', 'Чоппи') # инициализация экземпляра класса
        """
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть типа str")
        self.color = color

        if not isinstance(name, str):
            raise TypeError("Кличка должна быть типа str")
        self.name = name

    def call_dog (self) -> None:
        """
        Функция, с помощью которой можно вызвать собаку

        Примеры:
        >>> dog = Dachshund('чёрно-коричневая', 'Чоппи')
        >>> dog.call_dog()
        """
        ...

    def feed_dog(self, bone: int) -> None:
        """
        Кормление таксы косточками.
        :param bone: Количество костей

        Примеры:
        >>> dog = Dachshund('чёрно-коричневая', 'Чоппи')
        >>> dog.feed_dog(2)
        """
        if not isinstance(bone, int):
            raise TypeError("Количество костей должно быть типа int")
        if bone < 0:
            raise ValueError("Количество костей должно быть положительным числом")
        ...

class Teapot:
    def __init__(self, volume: float, manufacturer: str):
        """
        Создание и подготовка к работе объекта "Чайник"

        :param volume: Объём чайника
        :param manufacturer: Производитель

        Примеры:
        >>> teapot = Teapot(1.5,'Dexp') # инициализация экземпляра класса
        """
        if not isinstance(volume, (int,float)):
            raise TypeError("Объём должен быть типа int или float")
        self.volume = volume

        if not isinstance(manufacturer, str):
            raise TypeError("Производитель должен быть типа str")
        self.manufacturer = manufacturer

    def add_water(self, water: float)->None:
        """
        Добавление воды в чайник.
        :param water: Объём добавляемой жидкости

        Примеры:
        >>> teapot = Teapot(1.5,'Dexp')
        >>> teapot.add_water(0.2)
        """
        if not isinstance(water, (int,float)):
            raise TypeError("Добавляемая жидкость должна быть типа int или float")
        if water < 0:
            raise ValueError("Добавляемая жидкость должна положительным числом")
        ...

    def teapot_is_heated(self) -> bool:
        """
        Функция, которая проверяет, нагрет ли чайник

        :return: Является ли чайник нагретым

        Примеры:
        >>> teapot = Teapot(1.5,'Dexp')
        >>> teapot.teapot_is_heated()
        """
        ...

class SSD:
    def __init__(self, storage_capacity: float, manufacturer: str):
        """
        Создание и подготовка к работе объекта "Чайник"

        :param storage_capacity: Объём SSD накопителя
        :param manufacturer: Производитель

        Примеры:
        >>> ssd = SSD(128,'Samsung') # инициализация экземпляра класса
        """
        if not isinstance(storage_capacity, int):
            raise TypeError("Объём накопителя должен быть типа int")
        self.storage_capacity = storage_capacity

        if not isinstance(manufacturer, str):
            raise TypeError("Производитель должен быть типа str")
        self.manufacturer = manufacturer

    def add_data_to_ssd(self, data: str)->None:
        """
        Запись информации на диск.
        :param data: Данные

        Примеры:
        >>> ssd = SSD(128,'Samsung')
        >>> ssd.add_data_to_ssd('Телефонная книга')
        """
        if not isinstance(data,str):
            raise TypeError("Записываемые данные должны быть типа str")

        ...

    def ssd_inserted_in_pc(self) -> bool:
        """
        Функция, которая проверяет, вставлен ли ссд в компьютер

        :return: Вставлен ли ссд

        Примеры:
        >>> ssd = SSD(128,'Samsung')
        >>> ssd.ssd_inserted_in_pc()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

