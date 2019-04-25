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
from typing import Union, List
from constants import CARS_TYPES, CARS_PRODUCER
import uuid
import random


class Cesar:

    def __init__(self, price, type_car, producer):
        self.__price = price
        self.__type = type_car
        self.__producer = producer
        self.number = uuid.uuid4()
        self.mileage = float(f'{random.random() * 100:2f}')

    @property
    def price(self):
        assert isinstance(self.__price, float), 'Price must be float'
        return self.__price

    @property
    def type(self):
        car = self.__type if self.__type in CARS_TYPES else None
        assert car, f'Select car in list {CARS_TYPES}'
        return car

    @property
    def producer(self):
        producer = self.__producer if self.__producer in CARS_PRODUCER else None
        assert producer, f'Select producer in list {CARS_PRODUCER}'
        return producer

    @property
    def new_number(self):
        self.number = uuid.uuid4()
        return self.number

    @property
    def logs(self):
        specification = dict(
            price=self.price,
            type=self.type,
            producer=self.producer,
            number=str(self.number),
            mileage=self.mileage
        )
        return specification

    def __str__(self):
        return self.car()


class Car:
    pass


class Garage:
    pass


if __name__ == '__main__':

    bmw = Cesar(price=35000.00, type_car='Truck', producer='BMW')
    ford = Cesar(price=25000.145, type_car='Sedan', producer='FORD')
    print(bmw.price, bmw.type, bmw.producer, bmw.number)
    print(f'bmw number is {bmw.number}')
    print(f'bmw number has been changed to the {bmw.new_number}')
    print('set of the car')
    print('___________')
    for k, v in bmw.logs.items(): print(f'{k} {v}')
    print('___________')
    print(bmw.price > ford.price)
