# Python functional paradigm
def sum_squares(lst: list) -> int:
    return sum(map(lambda x: x ** 2, lst))  # 1 + 2**2 + 3**2


print(sum_squares([1, 2, 3]))  # 14


# Haskell
# sumSquares = sum . map (^2)
# ghci> sumSquares [4, 5, 6] # 77


# Python structural-procedural paradigm
def sum_squares(lst: list) -> int:
    current_sum = 0
    for el in lst:
        current_sum += (el ** 2)
    return current_sum


print(sum_squares([1, 2, 3]))  # 14


# Python oop paradigm
class List:
    def __init__(self, lst):
        self.lst = lst

    def calculate_sum_squares(self):
        current_sum = 0
        for el in self.lst:
            current_sum += (el ** 2)
        self.sum_squares = current_sum
