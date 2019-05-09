import json
from uuid import UUID
from objects_and_classes.homework.homework import Cesar, Car, Garage
import inspect


class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return [obj.real, obj.imag]
        if isinstance(obj, set):
            return list(obj)
        if isinstance(obj, UUID):
            return obj.hex
        if hasattr(obj, '__dict__'):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


def object_comparison(obj, class_obj):
    assert isinstance(obj, dict), 'Obj mast be dict'
    keys_obj = list(filter(lambda key: key, obj.keys()))
    key_class = list(
        filter(lambda key: key, inspect.signature(class_obj).parameters.keys())
    )
    inspect_arg = list(map(lambda cl_key: cl_key in keys_obj, key_class))
    return inspect_arg


def json_hook(obj):
    if 'set' in obj:
        return set(obj)
    car_args = object_comparison(obj, Car)
    cesar_args = object_comparison(obj, Cesar)
    garage_args = object_comparison(obj, Garage)
    if all(car_args):
        create_car = Car(
            price=obj['price'],
            type_car=obj['type_car'],
            producer=obj['producer'],
            mileage=obj['mileage']
        )
        create_car.number = obj['number']
        return create_car
    if all(garage_args):
        create_garage = Garage(
            town=obj['town'],
            places=obj['places'],
            cars=obj['cars'],
            owner=obj['owner']
        )
        return create_garage
    if all(cesar_args):
        create_cesar = Cesar(name=obj['name'], garages=obj['garages'])
        create_cesar.register_id = obj['register_id']
        return create_cesar

    return obj
