import sys, inspect
from pprint import pprint

class Person:

    """Неизвестная миру личность"""

    def __init__(self, name, s_name):
        self.name = name
        self.second_name = s_name


def introspection_info(obj):
    about = dict()

    """Атрибуты и методы"""

    about["type"] = type(obj)
    temp_list = dir(obj)
    about['methods'] = list()
    about['atribute'] = list()
    for item in temp_list:

        if item == '__module__':
            about['module'] = item
        if item.startswith('__'):
            about['methods'].append(item)
        else:
            about['atribute'].append(item)

    return about

number_info = introspection_info(42)
pprint(number_info)

person = Person("Bob", "Nickson")
number_info = introspection_info(person)
pprint(number_info)




