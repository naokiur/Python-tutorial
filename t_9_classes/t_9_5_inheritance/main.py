class Animal:
    def __init__(self):
        pass

    def bow(self):
        print('bow!!')


class Dog(Animal):
    def bite(self):
        print('bite!!')

animal = Animal()
dog = Dog()

animal.bow()
dog.bow()
dog.bite()
