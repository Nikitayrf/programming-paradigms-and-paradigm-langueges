### Example 1: loop sum
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # объявляем массив arr
summ = 0                               # объявляем переменную summ равную нулю
for el in arr:                         # перебираем элементы массива arr
    summ += el                         # на каждом шаге увеличиваем summ на arr
print(summ)                            # выводим summ в терминал
