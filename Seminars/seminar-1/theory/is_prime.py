# Задача: Написать функцию, проверяющую, является ли число простым
# в императивном и декларативном стиле

# Imperative programming

def check_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


print(check_prime(1))
print(check_prime(2))
print(check_prime(4))


# Declarative programming

def is_prime(number):
    gen_list = [i for i in range(2, int(number ** 0.5) + 1)]
    if number < 2:
        return False
    list_of_bool = list(map(lambda x: number % x != 0, gen_list))
    return all(list_of_bool)


print(is_prime(1))
print(is_prime(2))
print(is_prime(4))
