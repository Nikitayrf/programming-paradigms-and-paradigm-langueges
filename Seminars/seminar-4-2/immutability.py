# Пример изменяемых данных
mutable_list = [1, 2, 3]
mutable_list[1] = 10  # Изменение элемента списка

# Пример неизменяемых данных
immutable_tuple = (1, 2, 3)
new_tuple = immutable_tuple + (10,)  # Создание нового кортежа на основе старого


def append_to_list(lst, item):
    """
    Создаёт новый список, добавляя элемент к существующему списку.

    :param lst: Исходный список.
    :param item: Элемент для добавления.
    :return: Новый список с добавленным элементом.
    """
    return lst + [item]  # Создание нового списка на основе старого
