from __future__ import annotations

from ruamel.yaml import YAML
import uuid
import random

from objects_and_classes.homework.constants import CARS_TYPES, CARS_PRODUCER,\
    TOWNS
from json_utils import JsonEncoder, json_hook

from typing import Union, List
import json
import pickle
import inspect
from ruamel.yaml import YAML, yaml_object
import ruamel.yaml

CT = Union[float, str, str, type(uuid.uuid4), float]
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


@yaml_object(yaml)
class Cesar:
    yaml_tag = '!cesar'
    garages: List[Garage]

    def __init__(self, name: str, garages=0):
        self.name = name
        self.garages = garages if garages else []
        self.register_id = uuid.uuid4()

    def __repr__(self):
        return f'Cesar {self.name} have {self.garages} and hes register id '\
            f'{self.register_id}'

    def hit_hat(self):
        return sum(map(lambda garage: garage.hit_hat(), self.garages))

    def garages_count(self):
        return len(self.garages)

    def cars_count(self):
        return sum(map(lambda garage: len(garage.cars), self.garages))

    def add_car(self, car, garage=None):

        if garage:
            return garage.add(car)

        # count is free counts cars in garage, free_garage is object garage
        count, free_garage = max(
            [(item.places - len(item.cars), item) for item in self.garages]
        )
        if not count:
            print(f'Sorry all the places are taken')
            return
        return free_garage.add(car)

    def __lt__(self, other):
        return self.hit_hat() < other.hit_hat()

    def __gt__(self, other):
        return self.hit_hat() > other.hit_hat()

    def __eq__(self, other):
        return self.hit_hat() == other.hit_hat()

    def __ge__(self, other):
        return self.hit_hat() >= other.hit_hat()

    def __le__(self, other):
        return self.hit_hat() <= other.hit_hat()

    @classmethod
    def to_yaml(cls, representer, node):
        node.__dict__['register_id'] = str(node.__dict__['register_id'])
        return representer.represent_mapping(cls.yaml_tag, node.__dict__)

    @classmethod
    def from_yaml(cls, constructor, node):
        value = ruamel.yaml.constructor.SafeConstructor.construct_mapping(
            constructor, node, deep=True
        )
        instance = cls(name=value['name'], garages=value['garages'])
        instance.register_id = value['register_id']
        return instance


@yaml_object(yaml)
class Car:
    yaml_tag = '!car'

    def __init__(self, price: float, type_car, producer, mileage: float):
        self.price = price
        self.type_car = type_car if type_car in CARS_TYPES else []
        self.producer = producer if producer in CARS_PRODUCER else []
        self.number = uuid.uuid4()
        self.mileage = mileage
        assert self.type_car, f'Bad type car {type_car}. '\
            f'Select type from list {CARS_TYPES}'
        assert self.producer, f'Bad producer {producer}. '\
            f'Select producer from list {CARS_TYPES}'

    def __repr__(self):
        return f'Car(price={self.price}, type={self.type_car}, ' \
            f'producer={self.producer}, number={self.number}, '\
            f'mileage={self.mileage})'

    def __lt__(self, other: Car):
        return self.price < other.price

    def __gt__(self, other: Car):
        return self.price > other.price

    def __eq__(self, other: Car):
        return self.price == other.price

    def __le__(self, other: Car):
        return self.price <= other.price

    def __ge__(self, other: Car):
        return self.price >= other.price

    @property
    def new_number(self):
        self.number = uuid.uuid4()
        return self.number

    @classmethod
    def to_yaml(cls, representer, node):
        node.__dict__['number'] = str(node.__dict__['number'])
        return representer.represent_mapping(cls.yaml_tag, node.__dict__)

    @classmethod
    def from_yaml(cls, constructor, node):
        value = ruamel.yaml.constructor.SafeConstructor.construct_mapping(
            constructor, node, deep=True
        )
        instance = cls(
            price=value['price'],
            type_car=value['type_car'],
            producer=value['producer'],
            mileage=value['mileage']
        )
        instance.number = value['number']
        return instance


@yaml_object(yaml)
class Garage:
    yaml_tag = '!garage'
    owner: uuid.UUID

    def __init__(self, town, places: int, cars=[], owner=None):
        self.town = town if town in TOWNS else []
        self.cars = cars
        self.places = places
        self.owner = owner
        assert self.town, f'Select towns from list {TOWNS}'

    def __repr__(self):
        return f'Garage: Town {self.town}, Cars {self.cars},' \
            f'Places {self.places}, Owner {self.owner}'

    def add(self, car):
        car_in_garage = list(
            filter(lambda c: c.number == car.number, self.cars)
        )
        if not car_in_garage and len(self.cars) < self.places:
            print(f'Car {car.producer} is added to garage {self.town}')
            self.cars.append(car)
            return self.cars

        if car_in_garage:
            print(f'The car {car.producer} is already in the garage '
                  f'{self.town}')
            return
        print(f'Sorry garage count is full (places={self.places}, '
              f'count={len(self.cars)})')
        return

    def remove(self, car):
        if self.cars:
            return self.cars.remove(car)

    def hit_hat(self):
        return sum(map(lambda car: car.price, self.cars))

    def __lt__(self, other):
        return self.cars < other.cars

    def __gt__(self, other):
        return self.cars > other.cars

    @classmethod
    def to_yaml(cls, representer, node):
        return representer.represent_mapping(cls.yaml_tag, node.__dict__)

    @classmethod
    def from_yaml(cls, constructor, node):
        value = ruamel.yaml.constructor.SafeConstructor.construct_mapping(
            constructor, node, deep=True
        )
        instance = Garage(
            town=value['town'],
            places=value['places'],
            cars=value['cars'],
            owner=value['owner']
        )
        return instance


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
    def yaml_damp(cls, file_name, data):
        yaml_format = '{}.yaml'.format(file_name)
        with open(yaml_format, "w") as file:
            cls.yaml.indent(mapping=4, sequence=10, offset=8)
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
    def pickle_damp(file_name, data):
        file_pickle = '{}.pickle'.format(file_name)
        with open(file_pickle, "wb") as file:
            pickle.dump(data, file)

    @staticmethod
    def pickle_load(file_name):
        file_pickle = '{}.pickle'.format(file_name)
        with open(file_pickle, "rb") as file:
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
    gara2 = Garage(town='Prague', places=3)
    for car in cars_list:
        gara.add(car)
    gara.add(ford)
    gara2.add(ford)
    gara2.add(bmw)
    cesas = Cesar('Petro', garages_list)
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
    pickle_damp_cesar = PicleConverter.pickle_damp('pickle_damp_cesar', cesas)
    picle_load_cesar = PicleConverter.pickle_load('pickle_damp_cesar')

    pickle_damps_cesar = PicleConverter.pickle_damps(cesas)
    pickle_loads_cesar = PicleConverter.pickle_loads(pickle_damps_cesar)
    print('pickle_loads', pickle_loads_cesar.hit_hat())
    print('pickle_load', picle_load_cesar.hit_hat())
    print(cesas.hit_hat())
