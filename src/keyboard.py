from src.item import Item


class LayoutMixin:
    __language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'RU':
            self.__language = 'EN'
        else:
            self.__language = 'RU'


class Keyboard(Item, LayoutMixin):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def __str__(self):
        return self.name
