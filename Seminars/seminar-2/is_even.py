# Задача: Написать проверку является ли число чётным

if __name__ == '__main__':
    num = int(input('Enter a number: \n'))
    if num % 2 == 0:
        print(True)
    else:
        print(False)
