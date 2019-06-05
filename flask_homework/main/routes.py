from flask_restful import Resource, reqparse
from flask import render_template, make_response


parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('page', type=int, help="wrong page expecting int")

value = []


class Main(Resource):

    def get(self):
        return make_response(render_template('home.html', response=value))

    def post(self, value):
        # value_list.append(value)
        return "Successful"
