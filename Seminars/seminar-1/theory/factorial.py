# Задача: Написать функцию нахождения факториала числа
# в императивном и декларативном стиле.

# Imperative programming

def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


print(calculate_factorial(5))


# Declarative programming

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)


print(calculate_factorial(5))
