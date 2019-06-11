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
        self.cesar_yaml = Cesar('Pit', YAML_GARAGES)
        self.cesar_json = JSON_CESAR
        self.cesar_pickle = PICKLE_CESAR
        self.garage = Garage(town='Amsterdam', places=3)


class TestCar(Base):

    def test_matching_cars(self):
        for car in YAML_CARS_OBJ:
            if car.get('eg'):
                self.assertEqual(car['eg'], self.car)
            if car.get('gt'):
                self.assertGreater(car['gt'], self.car)
                self.assertGreaterEqual(car['gt'], self.car)
            if car.get('lt'):
                self.assertLess(car['lt'], self.car)
                self.assertLessEqual(car['lt'], self.car)

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

        for index in range(len(self.garage.cars)):
            self.assertEqual(
                self.garage.cars[index].number, YAML_CARS[index].number)

    def test_validation_add_cars(self):
        for car in YAML_CARS:
            self.garage.add(car)
        message = 'Sorry garage count is full (places=3, count=3)'
        self.assertTrue(self.garage.add(self.car) == message)

    def test_remove_car(self):
        self.add_car()
        get_car = YAML_CARS[0]
        self.assertEqual(len(self.garage.cars), self.garage.places)
        self.garage.remove(get_car)
        self.assertEqual(len(self.garage.cars), 2)
        for car in self.garage.cars:
            self.assertIsNot(car.number, get_car.number)

    def test_hit_hat(self):
        self.add_car()
        self.assertEqual(self.garage.hit_hat(), 216482.94499999998)


class TestCesar(Base):

    def add_car(self):
        for car in YAML_CARS:
            self.cesar_yaml.add_car(car)
        return self.garage

    def test_add_car(self):
        self.assertEqual(self.cesar_yaml.garages[2].cars, [])
        self.cesar_yaml.add_car(self.car)
        self.assertEqual(len(self.cesar_yaml.garages[2].cars), 1)
        self.assertEqual(
            self.car.number, self.cesar_yaml.garages[2].cars[0].number)

    def test_hit_hat(self):
        self.cesar_yaml.add_car(self.car)
        self.add_car()
        self.assertEqual(self.cesar_yaml.hit_hat(), 240482.945)

    def test_garages_count(self):
        assert len(self.cesar_yaml.garages) == self.cesar_yaml.garages_count()

    def test_cars_count(self):
        yaml_cars_count = [len(car.cars) for car in self.cesar_yaml.garages]
        assert sum(yaml_cars_count) == self.cesar_yaml.cars_count()

        json_cars_count = [len(car.cars) for car in self.cesar_json.garages]
        assert sum(json_cars_count) == self.cesar_json.cars_count()

        pickle_cars_count = [len(car.cars) for car in self.cesar_pickle.garages]
        assert sum(pickle_cars_count) == self.cesar_pickle.cars_count()

    def test_validation_add_cars(self):
        self.cesar_yaml.add_car(self.car, garage=self.cesar_yaml.garages[0])
        m = 'Sorry garage count is full (places=3, count=3)'
        assert self.cesar_yaml.add_car(
            YAML_CARS[0], garage=self.cesar_yaml.garages[0]) == m

    def test_gt_cesar(self):
        new_cesar = Cesar('Anton', YAML_GARAGE)
        new_cesar.add_car(self.car)
        new_cesar.add_car(YAML_CARS[0])
        assert new_cesar.hit_hat() > self.cesar_yaml.hit_hat()

    def test_json_cesar(self):
        print(self.cesar_json.hit_hat())


if __name__ == "__main__":
    unittest.main()
