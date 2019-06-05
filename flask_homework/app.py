from datetime import timedelta

from flask import Flask, render_template, redirect

from main import main
from fruits import fruits
from vegetables import vegetables

app = Flask(__name__)
app.permanent_session_lifetime = timedelta(minutes=10)

app.register_blueprint(main)
app.register_blueprint(fruits)
app.register_blueprint(vegetables)


@app.errorhandler(404)
def error_404(error):
    return render_template("error_404.html", title=error)


@app.route('/re')
def redirect_page():
    return redirect("https://www.youtube.com", code=302)


if __name__ == "__main__":
    app.run(debug=True)
