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
from constants import CARS_TYPES, CARS_PRODUCER
import uuid
import random
CT = Union[float, str, str, type(uuid.uuid4), float]


class Cesar:
    pass


class Car:

    def __init__(self, price: float, type, producer, mileage: float):
        self.price = price
        self.type = type
        self.producer = producer
        self.number = uuid.uuid4()
        self.mileage = mileage

    def __str__(self):
        return f'Specification for the car next: \n Price {self.price} \n Type {self.type} \
        \n Producer {self.producer} \n Number {self.number} \n Mileage {self.mileage}'

    def __repr__(self):
        return f'Car(price={self.price}, type={self.type}, producer={self.producer}, number={self.number}, mileage={self.mileage})>'

    def __float__(self):
        return float(self.mileage), float(self.price)

    def __lt__(self, other: Car):
        return other.price < self.price

    def __gt__(self, other):
        return other.price > self.price

    def __eq__(self, other):
        return other.price == self.price

    def __le__(self, other):
        return other.price <= self.price

    def __ge__(self, other):
        return other.price >= self.price

    @property
    def new_number(self):
        self.number = uuid.uuid4()
        return self.number


class Garage:
    pass


if __name__ == '__main__':

    bmw = Car(price=35000.00, type='Truck', producer='BMW', mileage=0.0)
    # ford = Car(price=25000.145, type_car='Sedan', producer='FORD')
    # print(bmw.price, bmw.type, bmw.producer, bmw.number)
    print(bmw)
    print(repr(bmw))
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
