from __future__ import annotations
import sys
sys.path.append('..')
from json_utils import JsonEncoder, json_hook
import json
from typing import Union, List
from objects_and_classes.homework.homework import Cesar, Car, Garage
from objects_and_classes.homework.constants import CARS_TYPES, CARS_PRODUCER, TOWNS
import random
import uuid
import random
"""
Для попереднього домашнього завдання.
Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) файлу відповідно

Для класів Колекціонер Машина і Гараж написати методи, які зберігають стан обєкту в файли формату
yaml, json, pickle відповідно.

Для класів Колекціонер Машина і Гараж написати методи, які конвертують обєкт в строку формату
yaml, json, pickle відповідно.

Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) строки відповідно


Advanced
Добавити опрацьовку формату ini

"""
CT = Union[float, str, str, type(uuid.uuid4), float]


class JsonConverter:

    @staticmethod
    def json_loads(data):
        return json.loads(data, object_hook=json_hook)

    @staticmethod
    def json_damps(obj):
        return json.dumps(obj, cls=JsonEncoder)

    @staticmethod
    def json_damp(file_name: str, obj: object):
        json_format = '{}.json'.format(file_name)
        with open(json_format, 'w') as file:
            json.dump(obj, file, indent=4, cls=JsonEncoder)

    def json_load(file_name: str):
        json_format = '{}.json'.format(file_name)
        with open(json_format, 'r') as file:
            js_damp = json.load(file, object_hook=json_hook)

        return js_damp


if __name__ == '__main__':

    bmw = Car(price=35000.145, type_car='Sedan', producer='BMW', mileage=1)
    ford = Car(price=25000.145, type_car='Sedan', producer='Ford', mileage=1)
    cr_damp = JsonConverter.json_damps(bmw)
    print("Success")
    print(type(cr_damp), cr_damp)
    bmw2 = JsonConverter.json_loads(cr_damp)
    print(type(bmw2), bmw2)

    cars_list = []
    cars_list2 = []
    for _ in range(5):
        cars_list.append(
            Car(
                price=random.randint(1000, 100000) * 1.2,
                type_car=random.choice(CARS_TYPES),
                producer=random.choice(CARS_PRODUCER),
                mileage=random.randint(10, 1000) * 1.2
            )
        )

    for _ in range(3):
        cars_list2.append(
            Car(
                price=random.randint(1000, 100000) * 1.2,
                type_car=random.choice(CARS_TYPES),
                producer=random.choice(CARS_PRODUCER),
                mileage=random.randint(10, 1000) * 1.2
            )
        )

    garages_list = [Garage(town=random.choice(TOWNS), places=random.randint(1, 7))
                    for _ in range(3)]
    garages_list2 = [Garage(town=random.choice(TOWNS), places=3) for _ in range(4)]

    gara = Garage(town='Amsterdam', places=3)
    for car in cars_list:
        gara.add(car)

    cesas = Cesar('Petro', garages_list)
    cesas2 = Cesar('Vasia', garages_list2)

    cr_gara_damps = JsonConverter.json_damps(gara)
    loads_gara_damps = JsonConverter.json_loads(cr_gara_damps)

    cr_cesar_damps = JsonConverter.json_damps(cesas)
    loads_cesar_damps = JsonConverter.json_loads(cr_cesar_damps)

    cr_cesar_damp = JsonConverter.json_damp('cesar_damp', cesas)
    load_cesar_damp = JsonConverter.json_load('cesar_damp')
    import ipdb; ipdb.set_trace()