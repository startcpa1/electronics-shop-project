"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def tests_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000

    # устанавливаем новый уровень цен
    Item.pay_rate = 0.8
    # применяем скидку
    item1.apply_discount()

    assert item1.price == 8000.0
    assert item2.price == 20000

    # assert Item.all == '[<src.item.Item object at 0x10e5f6490>, <src.item.Item object at 0x10e5f5b10>]'


def test_name():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("СуперСмартфон", 10000, 20)
    assert item1.name == 'Смартфон'
    assert item1.price == 10000
    assert item1.quantity == 20
    assert item2.name == 'СуперСмартфон'


def tests_string_to_number():  # проверка перевода строки в число
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_instantiate_from_csv():
    Item.instantiate_from_csv('../src/items.csv')  # создание объектов из данных файла
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам


def test_name_len():
    item1 = Item("СуперСмартфон", 10000, 20)
    assert len(item1.name) == 13  # проверяет длину названия товара


def test_repr_method():
    item1 = Item("Телефон", 5000, 20)
    assert repr(item1) == "Item('Телефон', 5000, 20)"  # проверяет метод repr


def test_str_method():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'  # проверяет метод str
