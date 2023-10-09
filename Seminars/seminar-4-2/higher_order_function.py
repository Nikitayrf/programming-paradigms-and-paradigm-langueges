# Функции высшего порядка. Объекты первого класса.
### Присвоение функции переменной
def square(x):
    return x * x


# присвоение функции square переменной func
func = square

# теперь переменная func содержит функцию square
result = func(5)
print(result)  # Вывод: 25


### Функция, как объект первого класса
def apply_function(func, x):
    return func(x)


def double(x):
    return x * 2


def triple(x):
    return x * 3


result_1 = apply_function(double, 5)
result_2 = apply_function(triple, 5)

print(result_1)  # Вывод: 10
print(result_2)  # Вывод: 15


### Возвращение функций из других функций
def create_multiplier(factor):
    def multiplier(x):
        return x * factor

    return multiplier


double = create_multiplier(2)
triple = create_multiplier(3)

result_1 = double(5)
result_2 = triple(5)

print(result_1)  # Вывод: 10
print(result_2)  # Вывод: 15


### Хранение функций в структурах данных
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


function_list = [add, subtract]

result_1 = function_list[0](5, 3)
result_2 = function_list[1](10, 4)

print(result_1)  # Вывод: 8
print(result_2)  # Вывод: 6
