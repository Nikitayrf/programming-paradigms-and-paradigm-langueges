# Условие
# На вход подается: список целых чисел arr
#
# Задача
# Реализовать императивную функцию, которая возвращает три числа:
# ○ Долю позитивных чисел
# ○ Долю нулей
# ○ Долю отрицательных чисел

# Imperative programming

def proportion_imperative(array):
    positive = 0
    negative = 0
    zero = 0
    for i in array:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1
    res_positive = positive / len(array)
    negative = negative / len(array)
    zero = zero / len(array)
    return res_positive, negative, zero


print(proportion_imperative([1, 2, -1, -3, 5, 0]))


# Declarative programming

def proportion_declarative(array):
    positive = len(list(filter(lambda x: x > 0, array)))
    negative = len(list(filter(lambda x: x < 0, array)))
    zero = len(list(filter(lambda x: x == 0, array)))
    count = [positive, negative, zero]
    return list(map(lambda x: x / len(array), count))


print(proportion_declarative([1, 2, -1, -3, 5, 0]))
