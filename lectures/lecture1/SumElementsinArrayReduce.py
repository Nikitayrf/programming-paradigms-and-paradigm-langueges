### Example 3: map and reduce
from functools import reduce

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # объявляем массив arr
res = reduce(lambda x, y: x+y, arr)
print(res)
