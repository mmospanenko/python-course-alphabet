from flask import Blueprint
from flask_restful import Api
from fruits.routes import Fruits, FruitsDelete

fruits = Blueprint('fruits', __name__)
api_fruits = Api(fruits)

api_fruits.add_resource(
    Fruits,
    "/fruits",
    endpoint='fruits',
    methods=['POST', 'GET', 'DELETE']
)

api_fruits.add_resource(
    FruitsDelete,
    "/fruits/d",
    endpoint='fruits_delete',
    methods=['POST', 'GET'],
)
