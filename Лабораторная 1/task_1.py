import doctest


class Cat:
    def __init__(self, name: str, noise: str, age: float):
        """
        Создание и подготовка к работе объекта "Кот/Кошка"

        :param name: Кличка кота/кошки
        :param noise: Произносимый звук
        :param age: Возраст кота/кошки

        Примеры:
        >>> cat = Cat('Мурзик', 'Мяу!', 5)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Кличка должна быть типа str")
        self.name = name

        if not isinstance(noise, str):
            raise TypeError("Звук должен быть типа str")
        self.noise = noise

        if not isinstance(age, (int, float)):
            raise TypeError('Возраст должен быть типа int ли float')
        if age < 0:
            raise ValueError('Возраст должен быть положительным числом')
        self.age = age

    def feed_cat(self, hunger: float) -> bool:
        """
        Покормить кота.

        :param hunger: Показатель голода кота. Изменяется от 0 до 1.
        :raise ValueError: Если показатель hunger меньше нуля, то возвращается ошибка.

        :return: Если hunger больше или равен единице, то нужно покормить кота

        Примеры:
        >>> cat = Cat('Мурзик', 'Мяу!', 5)
        >>> cat.feed_cat(0.65)
        """
        ...

    def is_cat_is_a_kitty(self) -> bool:
        """
        Проверка является ли кот/кошка котенком
        :return: Если age меньше 1, то кот/кошка является котенком

        Примеры:
        >>> cat = Cat('Мурзик', 'Мяу!', 5)
        >>> cat.is_cat_is_a_kitty()
        """
        ...


class Game:
    def __init__(self, name: str, hours_in_game: float, total_achievements: int):
        """
        Создание и подготовка к работе объекта "Игра"

        :param name: Название игры
        :param hours_in_game: Количество проведенных в игре часов
        :param total_achievements: Полное количесвто ачивок в игре

        Примеры:
        >>> game = Game('Симулятор камня', 100, 2500)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название должно быть типа str")
        self.name = name

        if not isinstance(hours_in_game, (int, float)):
            raise TypeError('Количество часов в игре должно быть типа int ли float')
        if hours_in_game < 0:
            raise ValueError('Количество часов в игре должно быть положительным числом')
        self.hours_in_game = hours_in_game

        if not isinstance(total_achievements, int):
            raise TypeError('Полное количество ачивок в игре должно быть типа int')
        if total_achievements < 0:
            raise ValueError('Полное количество ачивок в игре должно быть положительным числом')
        self.total_achievements = total_achievements

    def is_platinum_achieved(self, current_achievements: int) -> bool:
        """
        Сравнивает количество полученных ачивок со всеми имеющимися и проверяет,
        пройдена ли игра на платину.

        :param current_achievements: Количество полученных ачивок игроком
        :raise ValueError: Если показатель current_achievements меньше нуля, то возвращается ошибка.

        :return: Если количество полученных достижений игроком равно полному количеству ачивок,
         то игра пройдена на платину

         Примеры:
         >>> game = Game('Симулятор камня', 100, 2500)
         >>> game.is_platinum_achieved(125)
        """
        ...

    def hours_to_pass_the_game(self) -> None:
        """
        Подсчет количества часов, потребовавшихся игроку для прохождения игры

        :return: Выводит количество часов, потраченных на игру, после завершения основной сюжетной линии

         Примеры:
         >>> game = Game('Симулятор камня', 100, 2500)
         >>> game.hours_to_pass_the_game()
        """
        ...


class Car:
    def __init__(self, car_model: str, power: float, color: str):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param car_model: Марка автомобиля
        :param power: Мощность автомобиля в лошадиных силах
        :param color: Цвет автомобиля

        Примеры:
        >>> car = Car('Жигули', 750, "Оливковый")  # инициализация экземпляра класса
        """
        if not isinstance(car_model, str):
            raise TypeError("Марка автомобиля должна быть типа str")
        self.car_model = car_model

        if not isinstance(power, (int, float)):
            raise TypeError('Мощность автомобиля должна быть типа int ли float')
        if power < 0:
            raise ValueError('Мощность автомобиля должна быть положительным числом')
        self.power = power

        if not isinstance(color, str):
            raise TypeError("Цвет автомобиля должен быть типа str")
        self.color = color

    def is_car_color_is_yellow(self) -> bool:
        """
        Проверка, является ли цвет автомобиля желтым

        :return: Стукнуть собеседника по плечу, если автомобиль желтый, иначе ничего не делать

        Пример:
        >>> car = Car('Жигули', 750, "Оливковый")
        >>> car.is_car_color_is_yellow()
        """
        ...

    def drag_racing(self, opponent_power: float) -> None:
        """
        Гонка по прямой с другим автомобилем

        :param opponent_power: Мощность двигателя в лошадиных силах автомобиля соперника

        :return: Выводится победитель заезда

        Примерыы:
        >>> car = Car('Жигули', 750, "Оливковый")
        >>> car.drag_racing(120)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
