"""
Вам небхідно написати 3 класи. Колекціонери Гаражі та Автомобілі.
Звязкок наступний один колекціонер може мати багато гаражів.
В одному гаражі може знаходитися багато автомобілів.

Автомобіль має наступні характеристики:
    price - значення типу float. Всі ціни за дефолтом в одній валюті.
    type - одне з перечисленних значеннь з CARS_TYPES в docs.
    producer - одне з перечисленних значеннь в CARS_PRODUCER.
    number - значення типу UUID. Присвоюється автоматично при створенні автомобілю.
    mileage - значення типу float. Пробіг автомобіля в кілометрах.


    Автомобілі можна перівнювати між собою за ціною.
    При виводі(logs, print) автомобілю повинні зазначатися всі його атрибути.

    Автомобіль має метод заміни номеру.
    номер повинен відповідати UUID

Гараж має наступні характеристики:

    town - одне з перечислениз значеннь в TOWNS
    cars - список з усіх автомобілів які знаходяться в гаражі
    places - значення типу int. Максимально допустима кількість автомобілів в гаражі
    owner - значення типу UUID. За дефолтом None.


    Повинен мати реалізованими наступні методи

    add(car) -> Добавляє машину в гараж, якщо є вільні місця
    remove(cat) -> Забирає машину з гаражу.
    hit_hat() -> Вертає сумарну вартість всіх машин в гаражі


Колекціонер має наступні характеристики
    name - значення типу str. Його ім'я
    garages - список з усіх гаражів які належать цьому Колекціонеру. Кількість гаражів за замовчуванням - 0
    register_id - UUID; Унікальна айдішка Колекціонера.

    Повинні бути реалізовані наступні методи:
    hit_hat() - повертає ціну всіх його автомобілів.
    garages_count() - вертає кількість гаріжів.
    сars_count() - вертає кількість машиню
    add_car() - додає машину у вибраний гараж. Якщо гараж не вказаний, то додає в гараж, де найбільше вільних місць.
    Якщо вільних місць немає повинне вивести повідомлення про це.

    Колекціонерів можна порівнювати за ціною всіх їх автомобілів.
"""
from __future__ import annotations
from typing import Union, List
from constants import CARS_TYPES, CARS_PRODUCER, TOWNS
import uuid
import random
CT = Union[float, str, str, type(uuid.uuid4), float]


class Cesar:

    def __init__(self, name: str, garages=0):
        self.name = name
        self.garages = garages
        self.register_id = uuid.uuid4()

    def __str__(self):
        return f'Cesar on {self.name} have {self.garages} and hes register id {self.register_id}'

    def hit_hat(self):
        pass

    def garages_count(self):
        pass

    def сars_count(self):
        pass

    def add_car(self):
        pass


class Car:

    def __init__(self, price: float, type_car, producer, mileage: float):
        self.price = price
        self.type_car = type_car
        self.producer = producer
        self.number = uuid.uuid4()
        self.mileage = mileage

    def __str__(self):
        return f'Specification for the car next: \n Price {self.price} \n Type {self.type_car} \
        \n Producer {self.producer} \n Number {self.number} \n Mileage {self.mileage}'

    def __repr__(self):
        return f'Car(price={self.price}, type={self.type_car}, producer={self.producer}, number={self.number}, mileage={self.mileage})>'

    def __float__(self):
        return float(self.mileage), float(self.price)

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


class Garage:

    def __init__(self, town, places=10, owner=None):
        self.town = town if town in TOWNS else []
        self.cars = []
        self.places = places
        self.owner = owner

    def __str__(self):
        return f'cars list {self.cars}'

    def add(self, car):
        if car not in self.cars and len(self.cars) < 10:
            self.cars.append(car)
            return self.cars

    def remove(self, car):
        return self.cars.remove(car)

    def hit_hat(self):
        return sum(map(lambda x: x.price, self.cars))


if __name__ == '__main__':

    # ces = Cesar(name='Pety', garages=2)
    # print(ces)

    bmw = Car(price=35000.00, type_car='Truck', producer='BMW', mileage=0.0)
    ford = Car(price=25000.145, type_car='Sedan', producer='Ford', mileage=1)
    gara = Garage(town='Amsterdam')
    gara.add(bmw)
    gara.add(ford)
    gara.add(bmw)
    print(gara.cars)
    print(gara.hit_hat())
    # gara.remove(bmw)
    # print(gara.cars)

    # ford = Car(price=25000.145, type_car='Sedan', producer='Ford', mileage=1)
    # # print(bmw.price, bmw.type_car, bmw.producer, bmw.number)
    # assert bmw.type_car and ford.type_car, f'Select type car {CARS_TYPES}'
    # assert bmw.producer and ford.producer, f'Select producer {CARS_PRODUCER}'
    # print(bmw)
    # print(repr(bmw))
    # print(ford > bmw)
    # print(ford < bmw)
    # print(ford == bmw)
    # print(bmw >= ford)
    # print(f'bmw number is {bmw.number}')
    # print(f'bmw number has been changed to the {bmw.new_number}')
    # print(bmw)
    # print(type(uuid))
    # print('___________')
    # for k, v in bmw.logs.items(): print(f'{k} {v}')
    # print('___________')
    # print(bmw.price + ford.price)
    # # print(bmw.mileage + ford.mileage)
    # print(type(bmw.mileage))
