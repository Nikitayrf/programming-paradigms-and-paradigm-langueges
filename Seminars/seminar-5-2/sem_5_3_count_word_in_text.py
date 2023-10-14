str = "Python is a powerful programming language. Python is used for web development, data analysis, machine learning, and more."
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
print(lib)
