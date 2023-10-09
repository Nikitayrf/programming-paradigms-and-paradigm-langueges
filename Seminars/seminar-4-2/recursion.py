def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(5)
print(result)  # Вывод: 120


def sum_list(numbers):
    if not numbers:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])


numbers = [1, 2, 3, 4, 5]
result = sum_list(numbers)
print(result)  # Вывод: 15
