def sort_list_declarative(numbers):
    res = sorted(numbers, reverse=True)
    return res


array = [1, 2, 1, 5, 8, 3]

print("Array:")
print(array)

print(sort_list_declarative(array))

print("Sorted Array:")
print(array)
