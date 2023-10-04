numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
even_numbers = [x for x in numbers if x % 2 == 0]
doubled_numbers = list(map(lambda x: x * 2, numbers))

print("Квадрат чисел:", squared_numbers)  # Квадрат чисел: [1, 4, 9, 16, 25]
print("Чётные числа:", even_numbers)  # Чётные числа: [2, 4]
print("Удвоенные числа:", doubled_numbers)  # Удвоенные числа: [2, 4, 6, 8, 10]
