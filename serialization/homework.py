from __future__ import annotations
from ruamel.yaml import YAML
import uuid
import random
from objects_and_classes.homework.constants import CARS_TYPES, CARS_PRODUCER, TOWNS
from objects_and_classes.homework.homework import Cesar, Car, Garage
from typing import Union, List
import json
from json_utils import JsonEncoder, json_hook
import pickle
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


class YamlConverter:
    yaml = YAML()

    @classmethod
    def to_damp(cls, data):
        data = data.__dict__
        if data.get('garages'):
            ces = {key: data[key] for key in data}
            garages = [garage.__dict__ for garage in ces['garages']]
            garages_list = []
            for item in garages:
                garages_dict = {}
                for key in item:
                    garages_dict[key] = item[key]
                    if key == 'cars':
                        cars_list = []
                        for item_car in item[key]:
                            item_car.__dict__['number'] = str(
                                item_car.__dict__['number']
                            )
                            cars_list.append(item_car.__dict__)
                        garages_dict['cars'] = cars_list
                        garages_list.append(garages_dict)
            data = {'Cesar': {'name': data['name'],
                              'register_id': str(data['register_id']),
                              'garages': garages_list
                              }
                    }
            return data

        if data.get('type_car'):
            data['number'] = str(data['number'])
            return dict(data)

        if data.get('town'):
            garages_list = []
            garages_dict = {}
            for key in data:
                garages_dict[key] = data[key]
                if key == 'cars':
                    cars_list = []
                    for item_car in data[key]:
                        item_car.__dict__['number'] = str(
                            item_car.__dict__['number']
                        )
                        cars_list.append(item_car.__dict__)
                    garages_dict['cars'] = cars_list
                    garages_list.append(garages_dict)
            return garages_list

    @classmethod
    def yaml_damp(cls, file_name, data):
        data = cls.to_damp(data)
        yaml_format = '{}.yaml'.format(file_name)
        with open(yaml_format, "w") as file:
            config = cls.yaml.dump(data, file)
        return config

    @classmethod
    def yaml_load(cls, file_name):
        yaml_format = '{}.yaml'.format(file_name)
        with open(yaml_format, "r") as file:
            config = cls.yaml.load(file)
        return config


class PicleConverter:

    @staticmethod
    def picle_damp(file_name, data):
        file_picle = '{}.txt'.format(file_name)
        with open(file_picle, "wb") as file:
            pickle.dump(data, file)

    @staticmethod
    def picle_load(file_name):
        file_picle = '{}.txt'.format(file_name)
        with open(file_picle, "rb") as file:
            load_file = pickle.load(file)
        return load_file

    @staticmethod
    def picle_damps(obj):
        return pickle.dumps(obj)

    @staticmethod
    def picle_loads(obj):
        return pickle.loads(obj)


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

    yaml_damp_cesar = YamlConverter.yaml_damp('yaml_damp_cesar', cesas)
    yaml_damp_cesar = YamlConverter.yaml_damp('yaml_damp_car', bmw)
    yaml_damp_cesar = YamlConverter.yaml_damp('yaml_damp_garage', gara)

    yaml_load_cesar = YamlConverter.yaml_load('yaml_damp_cesar')

    picle_damp_cesar = PicleConverter.picle_damp('picle_damp_cesar', cesas)
    picle_load_cesar = PicleConverter.picle_load('picle_damp_cesar')

    picle_damps_cesar = PicleConverter.picle_damps(cesas)
    picle_loads_cesar = PicleConverter.picle_loads(picle_damps_cesar)
