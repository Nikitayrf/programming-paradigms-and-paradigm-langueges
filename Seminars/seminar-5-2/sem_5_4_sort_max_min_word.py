# Напишем программу для анализа текста и определения самых часто встречающихся слов в нем.
str = "Python is a powerful programming a language. Python is used for a web development, data a analysis, machine is learning, and more."
str.lower()
str = str.replace(".", "")
str = str.replace(",", "")
sp = str.split()

lib = {}
for i in sp:
    if i in lib:
        lib[i] += 1
    else:
        lib[i] = 1
# print (lib)

lib2 = sorted(lib.items(), key=lambda item: item[1], reverse=True)
print(lib2)
