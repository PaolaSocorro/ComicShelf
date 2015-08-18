from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request,url_for, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from werkzeug import secure_filename
from model import User, Publisher, connect_to_db, db
from pyunpack import Archive
import extract_comics, process_filenames,parse_comics, json
import os, sys


USER_ROOT = r'C:/cygwin64/home/Paola/src/hbproject/'
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(['cbr','cbz','pdf', 'png', 'jpg', 'jpeg', 'gif','bmp','tiff'])
 # set(['cbr','cbz','cbt','cba','cb7'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
app.config['USER_ROOT']=USER_ROOT
# print app

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


"""
###################################
    render_template ROUTES
###################################

"""

@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")


@app.route('/addcomics')
def inputform():

    return render_template("input_form.html")




"""
###################################
    WORK ROUTES
###################################

"""


@app.route('/comictable', methods=['GET','POST'])
def make_table():
    """input form test"""
    # file_loc = "C:\Users\Paola\Desktop\Comic Test\Forever Evil"
    file_loc = "C:\Users\Paola\Desktop\Comic Test\Batman Eternal"

    comics = extract_comics.walk_files(file_loc)
    # comics = process_filenames.walk_files(files)

    print 'Making Comic Table'


    return jsonify(comics)


@app.route('/upload', methods=['POST'])
def upload():

    uploaded_files = request.files.getlist("file[]")
    filenames = []
    path = ""
    issue_path = ""
    icover_path = ""

    for file in uploaded_files:

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            info = process_filenames.walk_files(filename)
            #process filename, extract name and issue number
            #to use for path
            folder_name= info['comics'][0]['name']
            issue_path= info['comics'][0]['issue_number']
            # print "OUR PATHS" ,folder_name , issue_path
            # path = NAME OF THE FOLDER WHERE ALL ISSUES ARE SAVED
            path = UPLOAD_FOLDER + folder_name
            path = os.path.join(USER_ROOT,path)
            print "STRING PATH: ", path

            if os.path.isdir(path) == False:
                new_dir = os.makedirs(path)


            file.save(os.path.join(path,filename))

            filenames.append(filename)

        #UNPACK COMICS GET ISSUE PATH AND COVER ISSUE PATH in that order


    ci_paths = parse_comics.unpack_zips(path)
    issue_path = ci_paths[0]
    print "STR ISSUE PATH:", issue_path
    icover_path = ci_paths[1]
    print "STR COVER PATH: ", icover_path

    comic_info = process_filenames.walk_files(filenames)

    return render_template('upload.html',filenames=filenames)


@app.route('/upload/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)


"""
###################################
    LOGIN, SIGNUP, LOUGOUT
###################################

"""


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
