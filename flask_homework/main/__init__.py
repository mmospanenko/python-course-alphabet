from flask import Blueprint, render_template
from flask_restful import Api
from main.routes import Main

main = Blueprint('main', __name__)
api_main = Api(main)

api_main.add_resource(Main, "/", endpoint='main_page')


# @main.route('/')
# def home():
#     return render_template('home.html', response='aaa')
