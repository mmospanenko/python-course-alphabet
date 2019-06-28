import unittest
import random
import uuid

from tests.homework.config import (
    YAML_CARS_OBJ,
    YAML_CARS,
    YAML_GARAGES,
    YAML_GARAGE,
    JSON_CESAR,
    PICKLE_CESAR
)
from tests.homework.objects_and_classes.homework.homework import (
    Car,
    Cesar,
    Garage
)
from tests.homework.objects_and_classes.homework.constants import (
    CARS_TYPES,
    CARS_PRODUCER
)


class Base(unittest.TestCase):

    def setUp(self):
        self.car = Car(
            price=10000 * 1.2,
            type_car=random.choice(CARS_TYPES),
            producer=random.choice(CARS_PRODUCER),
            mileage=random.randint(10, 1000) * 1.2
        )
        self.first_car, self.second_car, self.third_car = YAML_CARS
        self.cesar_yaml = Cesar('Pit', YAML_GARAGES)
        self.cesar_json = JSON_CESAR
        self.cesar_pickle = PICKLE_CESAR
        self.garage = Garage(town='Amsterdam', places=3)
        self.cesar = Cesar('Denchick', [self.garage])
        self.first_garage, self.second_garage, self.third_garage = YAML_GARAGES


class TestCar(Base):

    def test_eq_car(self):
        for car in YAML_CARS_OBJ:
            if car.get('eg'):
                self.assertEqual(car['eg'], self.car)

    def test_gt_car(self):
        self.car.price = 13000.0
        for car in YAML_CARS_OBJ:
            if car.get('gt'):
                self.assertEqual(car['gt'], self.car)

    def test_lt_car(self):
        self.car.price = 11000.0
        for car in YAML_CARS_OBJ:
            if car.get('lt'):
                self.assertEqual(car['lt'], self.car)

    def test_new_number(self):
        self.assertNotEqual(self.car.number, self.car.new_number)

    def test_type_uuid(self):
        assert isinstance(self.car.number, uuid.UUID)


class TestGarage(Base):

    def add_car(self):
        for car in YAML_CARS:
            self.garage.add(car)
        return self.garage

    def test_add_cars(self):
        for car in YAML_CARS:
            self.garage.add(car)

        for index, car in enumerate(self.garage.cars):
            self.assertEqual(car.number, YAML_CARS[index].number)

    def test_validation_add_cars(self):
        for car in YAML_CARS:
            self.garage.add(car)
        message = 'Sorry garage count is full (places=3, count=3)'
        self.assertTrue(self.garage.add(self.car) == message)

    def test_remove_car(self):
        self.add_car()
        self.assertEqual(len(self.garage.cars), self.garage.places)
        self.garage.remove(self.first_car)
        self.assertEqual(len(self.garage.cars), 2)
        for car in self.garage.cars:
            self.assertIsNot(car.number, self.first_car.number)

    def test_hit_hat(self):
        self.add_car()
        self.assertEqual(self.garage.hit_hat(), 216482.94499999998)


class TestCesar(Base):

    def add_car(self):
        for car in YAML_CARS:
            self.garage.add(car)
        return self.garage

    def test_add_car(self):
        self.assertEqual(self.third_garage.cars, [])
        self.cesar_yaml.add_car(self.car)
        self.assertEqual(len(self.third_garage.cars), 1)
        self.assertEqual(self.car.number, self.third_garage.cars[0].number)

    def test_hit_hat(self):
        self.add_car()
        self.assertEqual(self.cesar.hit_hat(), 216482.94499999998)

    def test_yaml_hit_hat(self):
        self.cesar_yaml.add_car(self.first_car)
        self.car.price = 225609.6
        self.cesar.add_car(self.car)
        self.assertEqual(self.cesar_yaml, self.cesar)

    def test_garages_count(self):
        assert len(self.cesar_yaml.garages) == self.cesar_yaml.garages_count()

    def test_cars_count_from_yaml(self):
        cars_count = [len(car.cars) for car in self.cesar_yaml.garages]
        assert sum(cars_count) == self.cesar_yaml.cars_count()

    def test_cars_count_from_json(self):
        cars_count = [len(car.cars) for car in self.cesar_json.garages]
        assert sum(cars_count) == self.cesar_json.cars_count()

    def test_cars_count_from_pickle(self):
        cars_count = [len(car.cars) for car in self.cesar_pickle.garages]
        assert sum(cars_count) == self.cesar_pickle.cars_count()

    def test_validation_add_cars(self):
        self.cesar_yaml.add_car(self.car, garage=self.second_garage)
        self.cesar_yaml.add_car(
            self.first_car, garage=self.second_garage
        )
        message = 'Sorry garage count is full (places=2, count=2)'
        assert self.cesar_yaml.add_car(
           self.second_car, garage=self.second_garage) == message

    def test_gt_cesar_from_yaml(self):
        new_cesar = Cesar('Anton', YAML_GARAGE)
        new_cesar.add_car(self.car)
        new_cesar.add_car(self.first_car)
        assert new_cesar > self.cesar_yaml

    def test_json_eq_cesar(self):
        self.car.price = 134673.235
        self.cesar.add_car(self.car)
        self.assertEqual(self.cesar, self.cesar_json)


if __name__ == "__main__":
    unittest.main()
