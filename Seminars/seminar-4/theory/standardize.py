from math import sqrt
from statistics import mean, variance


def standardize(data):
    avg = mean(data)
    var = variance(data)
    std = sqrt(var)

    def standardize_element(x):
        return (x - avg) / std

    return list(map(standardize_element, data))


data = [1, 2, 3, 4, 5]
print(standardize(data))
# [-1.2649110640673518, -0.6324555320336759, 0.0, 0.6324555320336759, 1.2649110640673518]
