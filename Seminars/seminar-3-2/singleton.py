class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # Вывод: True
print(singleton1)

# private Singleton() {
#     // Приватный конструктор, чтобы предотвратить создание через new
# }

# public static Singleton getInstance() {
#     if (isinstance == null) {
#         instance = new Singleton();
#     }
#     return instance;
# }