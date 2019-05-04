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
    garages: List[Garage]

    def __init__(self, name: str, garages=0):
        self.name = name
        self.garages = garages if garages else []
        self.register_id = uuid.uuid4()

    def __str__(self):
        return f'Cesar on {self.name} have {self.garages} and hes register id {self.register_id}'

    def hit_hat(self):
        return sum(map(lambda obj: obj.hit_hat(), self.garages))

    def garages_count(self):
        return len(self.garages)

    def сars_count(self):
        return sum(map(lambda garage: len(garage.cars), self.garages))

    def add_car(self, car, garage=None):

        if garage in self.garages:
            if len(garage.cars) < garage.places:
                print(f'Selected garage {garage.town}')
                return garage.add(car)
            print(f'Sorry garage in {garage.town} is full')
            return

        # count is count cars in garage, free_garage is object garage
        count, free_garage = min([(obj.places - len(obj.cars), obj) for obj in self.garages])
        if count:
            print(f'Sorry all the places are taken')
            return
        return free_garage.add(car)


class Car:

    def __init__(self, price: float, type_car, producer, mileage: float):
        self.price = price
        self.type_car = type_car if type_car in CARS_TYPES else []
        self.producer = producer if producer in CARS_PRODUCER else []
        self.number = uuid.uuid4()
        self.mileage = mileage
        assert self.type_car, f'Bad type car {type_car}. Select type from list {CARS_TYPES}'
        assert self.producer, f'Bad producer {producer}. Select producer from list {CARS_TYPES}'

    def __str__(self):
        return f'Specification for the car next: \n Price {self.price} \n Type {self.type_car} \
        \n Producer {self.producer} \n Number {self.number} \n Mileage {self.mileage}'

    def __repr__(self):
        return f'Car(price={self.price}, type={self.type_car}, producer={self.producer},' \
            f' number={self.number}, mileage={self.mileage})>'

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
    owner: uuid.UUID

    def __init__(self, town, places=3, owner=None):
        self.town = town if town in TOWNS else []
        self.cars = []
        self.places = places
        self.owner = owner
        assert self.town, f'Select towns from list {TOWNS}'
        assert self.places >= len(self.cars), f'Max cars in garage is {self.places}'

    def __str__(self):
        return f'cars list {self.cars}'

    def add(self, car):
        if car not in self.cars and len(self.cars) < self.places:
            print(f'Car {car.producer} is added to garage {self.town}')
            self.cars.append(car)
            return self.cars
        if car in self.cars:
            print(f'The car {car.producer} is already in the garage {self.town}')
            return

    def remove(self, car):
        if self.cars:
            return self.cars.remove(car)

    def hit_hat(self):
        return sum(map(lambda x: x.price, self.cars))

    def __lt__(self, other):
        return self.cars < other.cars


if __name__ == '__main__':

    cars_list = []
    cars_list2 = []
    for _ in range(3):
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

    garages_list = [Garage(town=random.choice(TOWNS), places=random.randint(1, 20)) for _ in range(3)]
    garages_list2 = [Garage(town=random.choice(TOWNS)) for _ in range(3)]

    gara = Garage(town='Amsterdam')
    for car in cars_list:
        gara.add(car)

    print(gara.cars)
    print(gara.hit_hat())

    cesas = Cesar('Petro', garages_list)
    cesas2 = Cesar('Vasia', garages_list2)
    print(cesas.hit_hat())
    print(cesas.garages)
    for _ in range(5):
        for car in cars_list:
            cesas.add_car(car)

    print(len(gara.cars))
    gara.remove(cars_list[0])
    print(len(gara.cars))
    # cesss.add_car(bugatti)
    print(cesas.hit_hat())
    print(cesas.сars_count())
    print(cesas.garages_count())

    bmw = Car(price=35000.145, type_car='Sedan', producer='BMW', mileage=1)
    ford = Car(price=25000.145, type_car='Sedan', producer='Ford', mileage=1)
    # # print(bmw.price, bmw.type_car, bmw.producer, bmw.number)
    # assert bmw.type_car and ford.type_car, f'Select type car {CARS_TYPES}'
    # assert bmw.producer and ford.producer, f'Select producer {CARS_PRODUCER}'
    # print(bmw)
    # print(repr(bmw))
    print(ford > bmw)
    print(ford < bmw)
    print(ford == bmw)
    print(bmw >= ford)
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
