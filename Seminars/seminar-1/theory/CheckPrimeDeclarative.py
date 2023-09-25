def is_prime(number):
    gen_list = [i for i in range(2, int(number ** 0.5) + 1)]
    if number < 2:
        return False
    list_of_bool = list(map(lambda x: number % x != 0, gen_list))
    return all(list_of_bool)

print(is_prime(1))
print(is_prime(2))
print(is_prime(4))

