class Dog:
    def speak(self):
        return "Woof!"


class Cat:
    def speak(self):
        return "Meow!"


class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()


factory = AnimalFactory()
animal = factory.create_animal("dog")
animal2 = Dog
print(animal.speak())   # Вывод: "Woof!"
print(animal2.speak())  # Вывод: "Woof!"
