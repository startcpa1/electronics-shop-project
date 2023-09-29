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
