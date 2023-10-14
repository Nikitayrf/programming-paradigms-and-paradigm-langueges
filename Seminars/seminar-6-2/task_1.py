'''
Объектно-ориентированное программирование:
Задача: Магазин и продукты
Создайте классы Product и Store для моделирования магазина 
и продуктов. У магазина должны быть методы для добавления 
продуктов, отображения ассортимента и расчета общей стоимости 
покупки. Продукты могут иметь атрибуты, такие как название, 
цена и количество.
'''


class Product:
    def __init__(self, name, price, quantity):

        self.name = name


        self.price = price
        self.quantity = quantity


class Store:
    def __init__(self):

        self.products = []


def add_product(self, product):
    self.products.append(product)


def display_products(self):
    print("Ассортимент магазина:")


    for product in self.products:
        print(f"{product.name} - Цена: {product.price} руб, Количество: {product.quantity}")


def calculate_total(self, shopping_list):
    total_cost = 0


    for item in shopping_list:
        for product in self.products:
            if item["name"] == product.name:
                total_cost += product.price * item["quantity"]
                break
    return total_cost

# Создание продуктов
product1 = Product("Яблоко", 50, 10)
product2 = Product("Молоко", 80, 5)
product3 = Product("Хлеб", 30, 8)

# Создание магазина и добавление продуктов
store = Store()
store.add_product(product1)
store.add_product(product2)
store.add_product(product3)

# Отображение ассортимента магазина
store.display_products()

# Список покупок
shopping_list = [
    {"name": "Яблоко", "quantity": 3},
    {"name": "Молоко", "quantity": 2},
    {"name": "Хлеб", "quantity": 1}
]

# Расчет общей стоимости покупки
total_cost = store.calculate_total(shopping_list)
print(f"Общая стоимость покупки: {total_cost} руб.")
