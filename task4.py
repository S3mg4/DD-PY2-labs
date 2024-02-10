class Car:
    """ Базовый класс автомобиля. """

    def __init__(self, model: str, color: str):
        self._model = model
        self._color = color
        """
            Создание и подготовка к работе объекта "Автомобиль"

            :param model: Марка автомобиля
            :param color: Цвет автомобиля

            Примеры:
            >>> car = Car('Toyota', 'Красный!')  # инициализация экземпляра класса
            """

    @property
    def model(self):
        return self._model
    """
            Модель автомобиля невозможно изменить
            """

    def __str__(self):
        return f"Машина марки {self.model}. Цвет {self.color}"

    def __repr__(self):
        return f"{self.__class__.__name__}(model={self.model!r}, color={self.color!r})"


class PassengerCar(Car):
    """ Дочерний класс. Легковой автомобиль. """

    def __init__(self, model: str, color: str, doors: int):
        super().__init__(model) # Класс написан для завода, выпускающего автомобили одной марки
        self.color = color
        self.doors = doors
        """
        Создание и подготовка к работе объекта "Легковой автомобиль"

            :param model: Марка автомобиля
            :param color: Цвет автомобиля
            :param doors: Количетсво дверей

            Примеры:
            >>> car = PassengerCar('Toyota', 'Красный!', 5)  # инициализация экземпляра класса
        """

    @property
    def doors(self):
        return self._doors
    """
    Количество дверей должно оставаться постоянным (Исходя из техники безопасности)
    """


    @doors.setter
    def doors(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество дверей должно быть целым числом")
        if value <= 0:
            raise ValueError("У автомобиля должна быть хотя бы одна дверь")
        self._pages = value
        """ Проверка вводимого числа на корректность """

    def __str__(self):
        return f"Автомобиль марки {self.model}. Цвет {self.color}. Количество дверей {self.doors}"

    def __repr__(self):
        return f"{self.__class__.__name__}(model={self.model!r}, color={self.color!r}, doors={self.doors!r})"


class Lorry(Car):
    """ Дочерний класс. Грузовой автомобиль. """

    def __init__(self, model: str, color: str, lifting_capacity: int):
        super().__init__(model)
        self.color = color
        self.lifting_capacity = lifting_capacity
    """
            Создание и подготовка к работе объекта "Грузовой автомобиль"

                :param model: Марка автомобиля
                :param color: Цвет автомобиля
                :param lifting_capacity: Грузоподъемность в тоннах

                Примеры:
                >>> car = Lorry('Toyota', 'Красный!', 1)  # инициализация экземпляра класса
            """

    @property
    def lifting_capacity(self):
        return self._dlifting_capacity
    """Грузоподъемность не может быть изменена, параметры подвески задаются при сборке автомобиля"""

    @lifting_capacity.setter
    def lifting_capacity(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Грузоподъемность должна быть числом")
        if value <= 0:
            raise ValueError("Грузоподъемность должна быть больше 0")
        self._lifting_capacity = value
        """ Проверка вводимого числа на корректность """

    def __str__(self):
        return f"Автомобиль марки {self.model}. Цвет {self.color}. Грузоподъемность {self.lifting_capacity}"

    def __repr__(self):
        return f"{self.__class__.__name__}(model={self.model!r}, color={self.color!r}, lifting_capacity={self.lifting_capacity!r})"
