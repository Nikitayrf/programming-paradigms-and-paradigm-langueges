def sort_declarative(numbers):
    res = sorted(numbers, reverse=True)
    return res


array = [1, 2, 1, 5, 8, 3]

print("Array:")
print(array)

print("Sorted Array:")
print(sort_declarative(array))
