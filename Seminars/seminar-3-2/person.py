class Person:
    def __init__(self, name, age):  # создание конструктор
        self.name = name  # присвоение атрибута name классу Person
        self.age = age  # присвоение атрибута age классу Person

    def great(self):  # метод great класса Person
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


person1 = Person("Alice", 20)
person2 = Person("Bob", 25)

print(person1.name)  # вывод: "Alice"
print(person2.age)  # вывод: 25

person1.great()  # Hello, my name is Alice and I am 20 years old.
person2.great()  # Hello, my name is Bob and I am 25 years old.
