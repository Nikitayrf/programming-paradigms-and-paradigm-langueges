"""
● Контекст.
    Ещё один известный и довольно эффективный алгоритм
    сортировки массива - сортировка слиянием (merge sort).
    Алгоритм делится на два этапа:
        ○ этап разбиения - массив разбивается на пару
            массивов до тех пор, пока, полученные массивы не
            станут массивами длины 1 (состоящими из одного элемента).
        ○ этап слияния - соединяем пары массивов в большие
            массивы так, чтобы полученные массивы были отсортированы.
● Ваша задача.
    Реализовать сортировку слиянием на любом языке в любой
    парадигме. На вход ваша программа получает массив из
    чисел, а вернуть должна отсортированный массив.
"""


def input_arr(arr):
    if len(arr) > 1:
        left = list(arr[:len(arr) // 2])
        right = list(arr[len(arr) // 2:])
        left = input_arr(left)
        right = input_arr(right)
        return concat(left, right)
    return arr


def concat(arr_1, arr_2):
    arr_res = []
    i = 0
    j = 0

    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] < arr_2[j]:
            arr_res.append(arr_1[i])
            i += 1
        else:
            arr_res.append(arr_2[j])
            j += 1

    while i < len(arr_1):
        arr_res.append(arr_1[i])
        i += 1

    while j < len(arr_2):
        arr_res.append(arr_2[j])
        j += 1
    return arr_res


array = [1, 54, 1, 6, 2, 9, 0]
print(input_arr(array))
