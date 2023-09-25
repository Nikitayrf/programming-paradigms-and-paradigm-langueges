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