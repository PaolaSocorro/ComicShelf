from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from model import User, connect_to_db, db
import seed_comics, json




app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")

@app.route('/addcomics')
def inputform():


    return render_template("input_form.html")

@app.route('/comictable')
def make_table():
    """input form test"""
    file_loc = "C:\Users\Paola\Desktop\Comic Test\Forever Evil"

    comics = seed_comics.walk_files(file_loc)
    print 'here on comic table'
    # comics = json.loads(comics)
    print comics

    return jsonify(comics)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()