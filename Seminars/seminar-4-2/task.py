# Функция, как определенные данные
def sum_list(numbers):
    return sum(numbers)


array = [1, 2, 3, 4, 5]
total = sum_list(array)
print(total)  # Вывод: 15


# Применение функции к каждому элементу списка
def apply_fuction(func, numbers):
    return [func(x) for x in numbers]


def square(x):
    return x ** 2


numbers = [1, 2, 3, 4, 5]
square_numbers = apply_fuction(square, numbers)
print(square_numbers)  # Вывод: [1, 4, 9, 16, 25]


# Пример использования функций высшего порядка
def custom_sort(numbers, comparison_func):
    return sorted(numbers, key=comparison_func)


def descending_order(x):
    return -x


arr = [5, 2, 8, 1, 9, 3]
sorted_numbers = custom_sort(arr, descending_order)
print(sorted_numbers)  # Вывод: [9, 8, 5, 3, 2, 1]


# Замыкание
def outer_function(x):
    def inner_function(y):
        return x + y

    return inner_function


add_five = outer_function(5)
result = add_five(10)  # Замыкание захватывает x = 5
print(result)  # Вывод: 15


# Замыкание для счётчиков
def counter():
    count = 0

    def increment():
        nonlocal count  # Используется nonlocal для изменения переменной из внешней области
        count += 1
        return count

    return increment


counter_func = counter()
print(counter_func())  # Вывод: 1
print(counter_func())  # Вывод: 2
print(counter_func())  # Вывод: 3


# Замыкание с сохранением состояния
def make_multiplier(factor):
    def multiplier(number):
        return number * factor

    return multiplier


double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # Вывод: 10
print(triple(5))  # Вывод: 15

from functools import reduce


# Функция редуктор
def sum_reducer(acc, value):
    return acc * value


numbers = [1, 2, 3, 4, 5]
result = reduce(sum_reducer, numbers, 0)
print(result)


# Функция редуктора для нахождения макс элемента в списке
def max_reducer(acc, value):
    return max(acc, value)


numbers = [12, 34, 25, 45, 60]
result = reduce(max_reducer, numbers)
print(result)  # Вывод: 60

# Функция редуктора для конкатенации строк
def concat_reduce(acc, value):
    return acc + value

strings = ["Hello, ", "world", "!", " Welcome"]
result = reduce(concat_reduce, strings)
print(result)  # Вывод: Hello, world! Welcome