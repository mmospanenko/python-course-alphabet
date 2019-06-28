from __future__ import annotations

import os
import random
import json
import pickle

from ruamel.yaml import YAML
from serialization.json_utils import JsonEncoder, json_hook
from tests.homework.objects_and_classes.homework.constants import (
    CARS_TYPES,
    CARS_PRODUCER,
    TOWNS
)
from tests.homework.objects_and_classes.homework.homework import (
    Car,
    Cesar,
    Garage
)

yaml = YAML()


"""
Для попереднього домашнього завдання.
Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс
обєкту
з (yaml, json, pickle) файлу відповідно

Для класів Колекціонер Машина і Гараж написати методи, які зберігають стан
обєкту в файли формату
yaml, json, pickle відповідно.

Для класів Колекціонер Машина і Гараж написати методи, які конвертують обєкт в
строку формату
yaml, json, pickle відповідно.

Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс
обєкту
з (yaml, json, pickle) строки відповідно

Advanced
Добавити опрацьовку формату ini

"""


def custom_dir():
    home_path = os.path.dirname(os.path.abspath(__file__))
    damp_dir = os.path.join(home_path, 'damp/')
    if not os.path.isdir(damp_dir):
        os.mkdir('damp')
    return damp_dir


def auto_select_dir(file_name, new_dir=None):
    if not new_dir:
        _format = f'{custom_dir()}{file_name}'
        return _format
    if new_dir:
        _format = f'{new_dir}{file_name}'
        return _format


class JsonConverter:

    @staticmethod
    def json_loads(data):
        return json.loads(data, object_hook=json_hook)

    @staticmethod
    def json_damps(obj):
        return json.dumps(obj, cls=JsonEncoder)

    @staticmethod
    def json_damp(file_name: str, obj: object, new_dir=None):
        json_format = auto_select_dir(file_name, new_dir)
        with open(f'{json_format}.json', 'w') as file:
            json.dump(obj, file, indent=4, cls=JsonEncoder)

    @staticmethod
    def json_load(file_name: str, new_dir=None):
        json_format = auto_select_dir(file_name, new_dir)
        with open(f'{json_format}.json', 'r') as file:
            js_damp = json.load(file, object_hook=json_hook)
        return js_damp


class YamlConverter:
    yaml = YAML()

    @classmethod
    def yaml_damp(cls, file_name, data, new_dir=None):

        yaml_format = auto_select_dir(file_name, new_dir)

        with open(f'{yaml_format}.yaml', 'w') as file:
            cls.yaml.indent(mapping=4, sequence=10, offset=8)
            config = cls.yaml.dump(data, file)
        return config

    @classmethod
    def yaml_load(cls, file_name, new_dir=None):
        yaml_format = auto_select_dir(file_name, new_dir)
        with open(f'{yaml_format}.yaml', "r") as file:
            config = cls.yaml.load(file)
        return config


class PickleConverter:

    @staticmethod
    def pickle_damp(file_name, data, new_dir=None):
        file_pickle = auto_select_dir(file_name, new_dir)
        with open(f'{file_pickle}.pickle', "wb") as file:
            pickle.dump(data, file)

    @staticmethod
    def pickle_load(file_name, new_dir=None):
        file_pickle = auto_select_dir(file_name, new_dir)
        with open(f'{file_pickle}.pickle', "rb") as file:
            load_file = pickle.load(file)
        return load_file

    @staticmethod
    def pickle_damps(obj):
        return pickle.dumps(obj)

    @staticmethod
    def pickle_loads(obj):
        return pickle.loads(obj)


if __name__ == '__main__':

    bmw = Car(price=35000.145, type_car='Sedan', producer='BMW', mileage=1)
    bmw3 = Car(
        price=random.randint(1000, 100000) * 1.2,
        type_car=random.choice(CARS_TYPES),
        producer=random.choice(CARS_PRODUCER),
        mileage=random.randint(10, 1000) * 1.2
    )
    bmw4 = Car(
        price=random.randint(1000, 100000) * 1.2,
        type_car=random.choice(CARS_TYPES),
        producer=random.choice(CARS_PRODUCER),
        mileage=random.randint(10, 1000) * 1.2
    )
    ford = Car(price=25000.145, type_car='Sedan', producer='Ford', mileage=1)

    cars_list = [bmw3, bmw4, ford]

    garages_list = [Garage(town=random.choice(TOWNS),
                           places=random.randint(1, 7)) for _ in range(3)]
    garages_list2 = [Garage(town=random.choice(TOWNS), places=3)
                     for _ in range(4)]

    gara = Garage(town='Amsterdam', places=3)
    gara2 = Garage(town='Prague', places=2)
    gara3 = Garage(town='Kiev', places=5)
    for car in cars_list:
        gara.add(car)
    gara.add(ford)
    gara2.add(ford)
    gara2.add(bmw)
    cesas = Cesar('Petro', [gara, gara2, gara3])
    cesas2 = Cesar('Vasia', garages_list2)
    cesas3 = Cesar('Oleg', [gara])

    print('*' * 20, 'JSON', '*' * 20)
    cr_damp = JsonConverter.json_damps(bmw)
    print(type(cr_damp), cr_damp)
    bmw2 = JsonConverter.json_loads(cr_damp)
    print(type(bmw2), bmw2)
    cr_gara_damps = JsonConverter.json_damps(gara)
    loads_gara_damps = JsonConverter.json_loads(cr_gara_damps)

    cr_cesar_damps = JsonConverter.json_damps(cesas)
    loads_cesar_damps = JsonConverter.json_loads(cr_cesar_damps)

    cr_cesar_damp = JsonConverter.json_damp('cesar_damp', cesas)
    load_cesar_damp = JsonConverter.json_load('cesar_damp')
    print('load_cesar', load_cesar_damp.hit_hat())
    print('loads_cesar', loads_cesar_damps.hit_hat())
    print(cesas.hit_hat())

    print('*' * 20, 'YAML', '*' * 20)
    yaml_damp_car = YamlConverter.yaml_damp('yaml_damp_car', bmw)
    yaml_damp_garage = YamlConverter.yaml_damp('yaml_damp_garage', gara)
    yaml_damp_cesar = YamlConverter.yaml_damp('yaml_damp_cesar', cesas)

    yaml_load_cesar = YamlConverter.yaml_load('yaml_damp_cesar')
    yaml_load_garage = YamlConverter.yaml_load('yaml_damp_garage')
    yaml_load_car = YamlConverter.yaml_load('yaml_damp_car')
    print('yaml_load', yaml_load_cesar.hit_hat())
    print(cesas.hit_hat())

    print('*' * 20, 'PICKLE', '*' * 20)
    pickle_damp_cesar = PickleConverter.pickle_damp('pickle_damp_cesar', cesas)
    picle_load_cesar = PickleConverter.pickle_load('pickle_damp_cesar')

    pickle_damps_cesar = PickleConverter.pickle_damps(cesas)
    pickle_loads_cesar = PickleConverter.pickle_loads(pickle_damps_cesar)
    print('pickle_loads', pickle_loads_cesar.hit_hat())
    print('pickle_load', picle_load_cesar.hit_hat())
    print(cesas.hit_hat())
