import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        """Возвращаем название товара"""
        return self.__name

    @name.setter
    def name(self, value):
        """Проверяем длину названия товара"""
        if len(value) > 10:
            self.__name = value[:10]
        else:
            self.__name = value

    @classmethod
    def instantiate_from_csv(cls):
        """Загружает данные из файла csv разбирая по названию, цене, кол-ву"""
        cls.all = []
        filename = '../src/items.csv'
        with open(filename, 'r', encoding='cp1251') as f:
            get_load_data = csv.DictReader(f)
            for row in get_load_data:
                name = row['name']
                price = cls.string_to_number(row['price'])
                quantity = cls.string_to_number(row['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(num):
        """Переводит из числа строки в число"""
        return int(float(num))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    def __repr__(self):
        """
        Возвращает метод repr в заданном формате: товар, цена, количество
        """
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Возвращает метод str в заданном формате
        """
        return f'{self.name}'

    def __add__(self, other):
        """
        Складывает количество товаров
        """
        if issubclass(other.__class__, self.__class__) or issubclass(self.__class__, other.__class__):
            return self.quantity + other.quantity
        else:
            raise TypeError('Невозможно сложить объекты разных типов')
