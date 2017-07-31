class Dog:
    kind = 'canine'

    def __init__(self, name):
        self.name = name


d = Dog('Fido')
e = Dog('Buddy')

print(d.kind)
print(e.kind)
print(d.name)
print(e.name)


class MistakenDog:
    kind = 'canine'
    tricks = []

    def __init__(self, name):
        self.name = name

    def add_tricks(self, tricks):
        self.tricks.append(tricks)

md = MistakenDog('Fido')
me = MistakenDog('Buddy')

md.add_tricks('roll over')
me.add_tricks('play dead')

print(md.tricks)


class MistakeDog:
    kind = 'canine'
    tricks = []

    def __init__(self, name):
        self.name = name

    def add_tricks(self, tricks):
        self.tricks.append(tricks)

md = MistakeDog('Fido')
me = MistakeDog('Buddy')

md.add_tricks('roll over')
me.add_tricks('play dead')

print(md.tricks)


class CorrectDog:
    kind = 'canine'

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_tricks(self, tricks):
        self.tricks.append(tricks)

cd = CorrectDog('Fido')
ce = CorrectDog('Buddy')

cd.add_tricks('roll over')
ce.add_tricks('play dead')

print(cd.tricks)
print(ce.tricks)
