# Задача: Напишем программу, которая проверяет, является ли заданное слово палиндромом.

str = input("Введите слово: ")
if str == str[::-1]:
    print("Полиндром")
else:
    print("НЕ полиндром")
