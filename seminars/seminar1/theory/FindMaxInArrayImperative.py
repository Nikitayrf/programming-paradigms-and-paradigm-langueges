### Imperative programming
def find_max(array: list) -> int:
    if len(array) > 0:
        max_num = array[0]
        for num in array:
            if num > max_num:
                max_num = num
        return max_num

print(find_max([1,2,3,10,1,6]))