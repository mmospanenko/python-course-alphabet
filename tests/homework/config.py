import os

from tests.homework.serialization.homework import (
    YamlConverter,
    JsonConverter,
    PickleConverter
)


def fixture_dir(base_dir):
    home_path = os.path.dirname(os.path.abspath(__file__))
    damp_dir = os.path.join(home_path, f'fixture/{base_dir}/')

    if not os.path.isdir(damp_dir):
        raise AssertionError(f'{damp_dir} not found')
    return damp_dir


YAML_CARS_OBJ = YamlConverter().yaml_load('cars', fixture_dir('yaml_fixture'))
YAML_CARS = YamlConverter().yaml_load('cars_add', fixture_dir('yaml_fixture'))
YAML_GARAGES = YamlConverter().yaml_load('garages', fixture_dir('yaml_fixture'))
YAML_GARAGE = YamlConverter().yaml_load('garage', fixture_dir('yaml_fixture'))
YAML_CESAR = YamlConverter().yaml_load('cesar', fixture_dir('yaml_fixture'))

JSON_CESAR = JsonConverter().json_load('cesar_damp', fixture_dir('json_fixture'))

PICKLE_CESAR = PickleConverter().pickle_load('pickle_damp_cesar', fixture_dir('pickle_fixture'))
