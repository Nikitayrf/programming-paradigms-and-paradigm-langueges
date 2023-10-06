# Определение абстрактного класса Observer для всех наблюдателей
class Observer:
    def update(self, message):
        pass


# Определение конкретного наблюдателя
class ConcreateObserver(Observer):
    def update(self, message):  # Метод вывода полученного сообщения
        print("Received message", message)


# Определяем класс Subject - наблюдаемый объект.
# Объект состояние которого подлежит наблюдению.
class Subject:
    _observers = []  # храниться список присоединенных наблюдателей

    # Метод присоединения наблюдателя к наблюдаемому объекту, т.е. в список _observers
    def attach(self, observer):
        self._observers.append(observer)

    # Метод уведомления наблюдателей о событии. Перебирает список _observers.
    # Вызывает у каждого наблюдателя метод update
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


# Создаём экземпляр наблюдаемого объекта (подлежащего изменениям)
subject = Subject()

# Создаём экземпляр наблюдателей
observer_1 = ConcreateObserver()
observer_2 = ConcreateObserver()

# Присоединяем наблюдателей к наблюдаемому объекту
subject.attach(observer_1)
subject.attach(observer_2)

# Уведомляем наблюдателей о событии
subject.notify("Hello, observers!")  # Вывод: Received message Hello, observers!
