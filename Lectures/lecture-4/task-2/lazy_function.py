# Lazy function
def lazy_function():
    i = 0
    while True:
        yield i  # генератор будет возвращать только текущий шаг
        i += 1


f = lazy_function()
print(next(f))  # 0
print(next(f))  # 1
print(next(f))  # 2
