from flask_restful import Resource, reqparse
from flask import render_template, make_response, request


parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('id', type=int, help="wrong page expecting int")

values = [
    'Помидорка',
    'Картошечка',
    'Баклажанчик',
    'Артишок',
    'Кукурузка',
    'Бурячок',
]
response = {key: val for key, val in enumerate(values, 1)}


def render():
    return make_response(render_template(
        'vegetables/vegetables.html',
        values=response,
        title='Vegetables'
        )
    )


class Vegetables(Resource):

    def get(self):
        parser.parse_args()
        return render()

    def post(self):
        if request.form.get('id'):
            max_values = max(response)
            response[max_values + 1] = request.form.get('id')
            return render()
        return render()


class VegetablesDelete(Resource):

    def post(self):
        parser.parse_args()
        ids = parser.parse_args()
        for key in response:
            if key == ids['id']:
                del response[ids['id']]
                break
        return render()
