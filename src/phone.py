from src.item import Item


class Phone(Item):  # создает класс Phone
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    @property
    def number_of_sim(self):  # возвращает значение кол-ва сим-карт
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):  # проверяет что количество больше нуля
        if value <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        else:
            self._number_of_sim = value

    def __repr__(self):  # возвращаем метод repr
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self._number_of_sim})"

    def __str__(self):  # возвращаем метод str
        return f"{self.name}"
