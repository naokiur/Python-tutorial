class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update


class MappingSubclass(Mapping):

    # noinspection PyMethodOverriding
    def update(self, keys, values):
        # provides new signature for update
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

first_list = range(1, 4)
mapping = Mapping(first_list)
print(mapping.items_list)

second_list = range(4, 7)
mapping.update(second_list)
print(mapping.items_list)

sub_mapping = MappingSubclass(first_list)
# Because subclass method does not break based method, __init__() can create array in sub_mapping.
print(sub_mapping.items_list)

sub_mapping.update(first_list, second_list)
print(sub_mapping.items_list)


class BreakMapping:
    def __init__(self, iterable):
        self.item_list = []
        self.update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.item_list.append(item)


class BreakSubMapping(BreakMapping):
    def update(self, keys, values):
        for item in zip(keys, values):
            self.item_list.append(item)

# Will be type error because update() of BreakMapping class is overrode by update() of BreakSubMapping class.
break_sub_mapping = BreakSubMapping(first_list)
print(break_sub_mapping.item_list)
