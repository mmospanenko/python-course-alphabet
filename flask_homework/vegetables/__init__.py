from flask import Blueprint
from flask_restful import Api
from vegetables.routes import Vegetables, VegetablesDelete

vegetables = Blueprint('vegetables', __name__)
api_vegetables = Api(vegetables)


api_vegetables.add_resource(
    Vegetables,
    "/vegetables",
    endpoint='vegetables',
    methods=['POST', 'GET', 'DELETE']
)

api_vegetables.add_resource(
    VegetablesDelete,
    "/vegetables/d",
    endpoint='vegetables_delete',
    methods=['POST', 'GET']
)
