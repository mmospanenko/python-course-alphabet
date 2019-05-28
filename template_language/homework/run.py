import json
import os

from flask import Flask, render_template

PRJ_DIR = os.path.dirname(os.path.abspath(__file__))
DUMP = os.path.join(PRJ_DIR, 'movies.json')

app = Flask(__name__)
initial_year = 2010


with open(DUMP) as f:
    MOVIES = json.load(f)


@app.route('/')
def home_page():
    return render_template('home.html', title='Home', author='Alex Smith')


@app.route('/movies')
def movies_page():
    return render_template(
        'movies.html',
        title='Movies list',
        movies=MOVIES,
        initial_year=initial_year
    )


@app.route('/<title>')
def movie_page(title):
    for i, movie in enumerate(MOVIES):
        if MOVIES[i].get('title') == title:
            return render_template('movie.html', title=title, movie=MOVIES[i])
    return render_template(
        'movies.html',
        title='Movies list',
        movies=MOVIES,
        initial_year=initial_year
    )


if __name__ == '__main__':
    app.run(debug=True)
