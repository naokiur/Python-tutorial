class A:
    def __init__(self):
        self.name = "A"
        self.id = "1"
        self.type = "A"

    def get_id(self):
        return self.name + self.id


class B:
    def __init__(self):
        self.name = "B"
        self.id = "2"
        self.type = "B"

    def get_id(self):
        return self.name + self.id

    def get_type(self):
        return self.type


class C:
    def __init__(self):
        self.name = "C"
        self.id = "3"

    def get_id(self):
        return self.name + self.id

    def get_type(self):
        return "TypeC" + self.id


class Body(A, B, C):
    def __init__(self):
        super().__init__()


body = Body()
print(body.get_id())
print(body.get_id(), body.name, body.get_type())
