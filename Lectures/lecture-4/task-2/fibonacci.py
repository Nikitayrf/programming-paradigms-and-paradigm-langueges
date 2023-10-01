# Числа Фибоначчи 0, 1, 1, 2, 3, 5, 8
def fibonacci(n):
    if 0 <= n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


result = fibonacci(6)
print(result)  # 8

result = fibonacci(2)
print(result)  # 1
