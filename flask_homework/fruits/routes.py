from flask_restful import Resource, reqparse
from flask import render_template, make_response, request


parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('id', type=int, help="wrong page expecting int")

values = [
    'Alfalfa',
    'Sprouts',
    'Apple',
    'Apricot',
    'Artichoke',
    'Asian',
    'Pear',
    'Asparagus',
    'Atemoya',
    'Avocado',
    'Bamboo'
]
response = {key: val for key, val in enumerate(values, 1)}


class Fruits(Resource):

    def render(self):
        return make_response(render_template(
            'fruits/fruits.html',
            values=response,
            title='fruits'
            )
        )

    def get(self):
        parser.parse_args()
        return self.render()

    def post(self):
        if request.form.get('id'):
            max_values = max(response)
            response[max_values + 1] = request.form.get('id')
            return self.render()
        return self.render()


class FruitsDelete(Resource):

    def render(self):
        return make_response(render_template(
            'fruits/fruits.html',
            values=response,
            title='fruits'
            )
        )

    def post(self):
        parser.parse_args()
        ids = parser.parse_args()
        for key in response:
            if key == ids['id']:
                del response[ids['id']]
                break
        return self.render()
