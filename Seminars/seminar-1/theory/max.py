# Задача: Написать функцию нахождения максимального числа в массиве
# в императивном и декларативном стиле.

# Imperative programming

def find_max(array: list) -> int:
    if len(array) > 0:
        max_num = array[0]
        for num in array:
            if num > max_num:
                max_num = num
        return max_num


print(find_max([1, 2, 3, 10, 1, 6]))


# Declarative programming

def find_max(array: list) -> int:
    return max(array)


print(find_max([1, 2, 3, 10, 1, 6]))
