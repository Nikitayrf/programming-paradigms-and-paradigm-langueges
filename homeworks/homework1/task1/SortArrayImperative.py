# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки
def sort_list_imperative(numbers):
    flag = False
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                flag = False
            else:
                flag = True
    if flag:
        return numbers


print(sort_list_imperative([1, 5, 1, 5, 8, 3]))
