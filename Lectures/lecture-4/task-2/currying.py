# Before currying

def add(x, y):
    return x + y


print(add(2, 5))  # 7


# After currying

def add(x):
    def add_x(y):
        return x + y

    return add_x


print(add(2)(5))  # 7
