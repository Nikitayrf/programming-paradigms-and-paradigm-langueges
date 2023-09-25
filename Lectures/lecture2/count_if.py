# Рассмотрим следующую задачу. Необходимо реализовать программу, которая:
# Получает на вход: список li и число n
# Возвращает: количество элементов в списке li равных этому заданному числу n

# Structered Programming
li = [1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 4]
n = 6
counter = 0
for el in li:
    if el == n:
        counter += 1
print(counter)  # 2


# Procedural Programming
def count_if(li, n):
    counter = 0
    for el in li:
        if el == n:
            counter += 1
    return  counter


print(count_if([1, 2, 3, 4, 5, 6, 6, 5, 4, 2, 2, 4], 3))  # 1
