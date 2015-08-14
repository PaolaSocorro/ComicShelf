from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from model import User, Publisher, connect_to_db, db
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


@app.route('/comictable', methods=['GET','POST'])
def make_table():
    """input form test"""
    # file_loc = "C:\Users\Paola\Desktop\Comic Test\Forever Evil"
    file_loc = "C:\Users\Paola\Desktop\Comic Test\Batman Eternal"

    comics = seed_comics.walk_files(file_loc)
    print 'Making Comic Table'
    # comics = json.loads(comics)
    # print comics

    return jsonify(comics)


@app.route('/upload', methods=['POST'])
def upload():
    # print (request.json)
    print "Geting FileList from Client"
    if request.method == 'POST':
        comics = request.files['files']
    # if request.method == 'POST':
        print comics
    return comics


@app.route('/login', methods=['GET', 'POST'])
def login_form():
    """ Login  
     take email, password from user form
     check if credentials exist in database, by checking if 
     email is in user table.
     if email in table, redirect to their profile
     if not redirect to sign up page.
    """
    # import pdb; pdb.set_trace()
    if request.method == 'POST': #Process form if route gets a POST request
        email = request.form.get("email") # ""
        password = request.form.get("password") # ""

        credentials = (email, password)
        dbemails = db.session.query(User.email).all()

        print email, type(email)
        print "Query Ran"
        print type(dbemails)

        user = User.query.filter_by(email=email).first()

        if not user:
            flash('PLEASE SIGN UP!')
            return redirect("/signup")
        else:
            if user.password != password:
                print password
                flash('Incorrect password')
                return redirect("/login")

            session["login_id"] = credentials 
            print "SESSION: ", session
            flash('You were successfully logged in')
            # return redirect("/users/%s" % user.user_id) # REDIRECT TO PROFILE PAGE.FIX
            return redirect ("/")


    else: #TAKE user to login page if route process a  GET request
        return render_template("login_form.html")



@app.route('/signup', methods=['GET', 'POST'])
def signup_form():
    """ Sign Up
        Add email, password,age,zipcode then commit new person to database.
        Find new user, and redirect to their profile page. 
    """

    if request.method == 'POST':
        name = request.form.get("name")
        print name
        email = request.form.get("email")
        print email
        password = request.form.get("password")
        print password
        age = request.form.get("age")
        gender = request.form.get("gender")

        person = User(name=name, email=email, password=password, age=age, gender=gender)

        db.session.add(person)
        db.session.commit()
        # new_userid = db.session.query.get(User.user_id.desc()).first()

        print person

    else:
        return render_template("signup.html")

    return redirect("/")




@app.route('/logout')
def log_out():
    """Log out
    redirect to homepage when logged out
    """
    credentials = session["login_id"]
    print credentials
    # If enough time: hide login/logout button depending if login/logout
    if "login_id" in session:
        del session["login_id"]
        flash('Logged out')
        print "Logged out:", session

        return redirect("/")


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()
