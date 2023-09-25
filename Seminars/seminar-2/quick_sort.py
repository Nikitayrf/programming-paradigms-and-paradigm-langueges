def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        base = arr[0]
        less = [i for i in arr[1:] if i <= base]
        greater = [i for i in arr[1:] if i > base]
        return quick_sort(less) + [base] + quick_sort(greater)


list_1 = [10, 5, 2, 3, 3, 6, 1]
print(quick_sort(list_1))  # [1, 2, 3, 3, 5, 6, 10]
