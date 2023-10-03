from statistics import mean
from math import sqrt

array_1 = [1, 2, 3, 4, 5]
array_2 = [2, 3, 4, 5, 6]

avg_1 = mean(array_1)
avg_2 = mean(array_2)

array_x_avg_1 = list(map(lambda x: x - avg_1, array_1))
array_x_avg_2 = list(map(lambda x: x - avg_2, array_2))

res_top = sum(list(map(lambda x, y: x * y, array_x_avg_1, array_x_avg_2)))

array_1_pow = sum(list(map(lambda x: x * x, array_x_avg_1)))
array_2_pow = sum(list(map(lambda x: x * x, array_x_avg_2)))

res_bottom = sqrt(array_1_pow * array_2_pow)

res = res_top / res_bottom
print(res)












# print(res_array_1_test)
# print(res_array_2_test)
#
#
# def calc_x_avg(data):
#     avg = mean(data)
#
#     def calc_el(x):
#         return x - avg
#
#     return list(map(calc_el, data))
#
#
# res_array_1 = calc_x_avg(array_1)
#
# res_array_2 = calc_x_avg(array_2)

# res_top = sum(list(map(lambda x, y: x * y, res_array_1, res_array_2)))
#
# res_array_1_pow = sum(list(map(lambda x: x * x, res_array_1)))
#
# res_array_2_pow = sum(list(map(lambda x: x * x, res_array_2)))





