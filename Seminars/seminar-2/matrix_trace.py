# След матрицы: структурный
# ● Контекст
#   След матрицы - это сумма чисел на её главной диагонали. След определён только для квадратных матриц
#   (количество столбцов = количеству строк).
# ● Задача
#   Реализовать чисто структурную реализацию вычисления следа для любой матрицы NxN.

# Structured programming

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
trace = 0
for i, row in enumerate(matrix):
    for j, el in enumerate(row):
        if i == j:
            trace += el

print(trace)  # 15


# Procedural programming

def get_trace(matrix):
    trace = 0
    for i, row in enumerate(matrix):
        for j, el in enumerate(row):
            if i == j:
                trace += el
    return trace


matrix_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(get_trace(matrix_2))  # 15
