from src.phone import Phone, Item


def test_number_of_sim():
    """
    Тестирует кол-во сим-карт
    """
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.number_of_sim == 2


def test_add_method():
    """
    Тестирует метод add
    """
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone2 = Phone("Phone 15", 150_000, 6, 0)
    item1 = Item("Mixer", 4500, 5)
    item2 = Item("Headphones", 2500, 2)
    assert item1 + item2 == 7
    assert item1 + phone1 == 10
    assert phone1 + phone2 == 11
