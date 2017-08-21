class Animal:
    def __init__(self, name):
        self.name = name

    def bow(self):
        print(self.name, 'bow!!')


class Dog(Animal):
    def bite(self):
        print(self.name, 'bite!!')

animal = Animal('animal')
dog = Dog('dog')

animal.bow()
dog.bow()
dog.bite()

print(isinstance(animal, Animal))
print(isinstance(dog, Animal))
print(issubclass(Dog, Animal))
