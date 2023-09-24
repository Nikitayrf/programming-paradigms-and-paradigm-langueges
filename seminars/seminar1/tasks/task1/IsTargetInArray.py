# Контекст
# Предположим, что нам хочется для любого массива чисел array и любого числа target узнать содержится
# ли target в array. Такую процедуру будем называть поиском.
# 💡
# Задача
# Реализовать императивную функцию поиска элементов на языке Python.


# Императивная парадигма
def search_imperative(target, array):
    for num in array:
        if num == target:
            return True
    return False


print(search_imperative(4, [1, 2, 3, 4, 5, 6]))


# Декларативная парадигма
def search_declarative(target, array):
    return target in array


print(search_declarative(2, [1, 2, 3, 4, 5, 6]))
