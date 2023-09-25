# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # меняем элементы местами
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Example usage
print(bubble_sort([42, 34, 54, 62, 45, 4]))  # [4, 34, 42, 45, 54, 62]
