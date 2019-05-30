import json
import os

from flask import Flask, render_template

PRJ_DIR = os.path.dirname(os.path.abspath(__file__))
DUMP = os.path.join(PRJ_DIR, 'movies.json')

app = Flask(__name__)
initial_year = 2010
author = 'Alex Smith'


with open(DUMP) as f:
    MOVIES = json.load(f)


@app.route('/')
def home_page():
    return render_template('home.html', title='Home', author=author)


@app.route('/movies')
def movies_page():
    return render_template(
        'movies.html',
        title='Movies list',
        movies=MOVIES,
        initial_year=initial_year
    )


@app.route('/movie/<ids>')
def movie_page(ids):
    for i, movie in enumerate(MOVIES):
        if MOVIES[i].get('id') == ids:
            title = MOVIES[i].get('title')
            return render_template('movie.html', title=title, movie=MOVIES[i])
    return render_template(
        'movies.html',
        title='Movies list',
        movies=MOVIES,
        initial_year=initial_year
    )


if __name__ == '__main__':
    app.run(debug=True)
