""" Таблица умножения
● Условие
  На вход подается число n.
● Задача
  Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
  Обоснуйте выбор парадигм.
● Пример вывода:
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
..
1 * 9 = 9
"""

# Выбрана структурная парадигма, так важна скорость разработки,
# получить быстро прототип


for i in range(1, int(input("Введите число: ")) + 1):
    print()
    for j in range(1, 10):
        print(f'{i} * {j} = {i * j}')