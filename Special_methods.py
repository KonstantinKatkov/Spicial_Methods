# Создайте новый класс House
# Создайте инициализатор для класса House, который будет задавать атрибут этажности self.numberOfFloors = 0
# Создайте метод setNewNumberOfFloors(floors), который будет изменять атрибут numberOfFloors
# на параметр floors и выводить в консоль numberOfFloors

class House:
    def __init__(self):
        self.numberOfFloors = 0
        print(f'Начальная точка атрибута этажности {self.numberOfFloors}')
        print()

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(f'Новый этаж {self.numberOfFloors}')


h1 = House()
h1.setNewNumberOfFloors(10)