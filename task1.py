class Gas_Stove:
    """ Базовый класс газовой плиты. """
    def __init__(self, number_of_burners: int, color: str):
        self.number_of_burners = number_of_burners
        self.color = color

    """Метод для открытия газа в плите. Должен быть скрыт от пользователя, так как менять его извне нет необходимости."""
    @property
    def __open_gas (self)->None: 
        ...
    
    """Метод для поджигания спички. Должен быть скрыт от пользователя, так как менять его извне нет необходимости."""
    @property
    def __light_a_match (self)->None:
        ...

    """Метод для поджигания газа спичкой. Должен быть скрыт от пользователя, так как менять его извне нет необходимости."""
    @property
    def __ignite_gas (self)->None: 
        ...

    """Метод, который включает плиту. Для плиты с авторозжигом может быть перезагружен, так как не нужно доставать спички и поджигать газ."""
    def turn_on_the_stove (self)->None:
        self.__open_gas()
        self.__light_a_match()
        self.__ignite_gas()
    
    def __str__(self):
        return f'Количество комфорок: {self.number_of_burners}. Цвет {self.color}.'

    def __repr__(self):
        return f'{self.__class__.__name__}(number_of_burners={self.number_of_burners!r}, color={self.color!r})'

class Gas_Stove_Auto_Ignition (Gas_Stove):
    """ Класс газовой плиты с авторозжигом. """

    """Метод для включения авторозжига. Должен быть скрыт от пользователя, так как менять его извне нет необходимости."""
    @property
    def __turn_on_auto_ignition (self)->None:
        ...

    def turn_on_the_stove (self)->None:
        self.__open_gas()
        self.__turn_on_auto_ignition()

if __name__ == "__main__":
    
    gas_stove = Gas_Stove(4, 'чёрный')
    auto_ign_stove = Gas_Stove_Auto_Ignition(2, 'белый') 
    
    print(gas_stove)
    print(auto_ign_stove)
    print(repr(gas_stove))
    print(repr(auto_ign_stove))
    
    pass