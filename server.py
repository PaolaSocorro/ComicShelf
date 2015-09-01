from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request,url_for, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from werkzeug import secure_filename
from model import Book,Genre,User, Publisher, connect_to_db, db
from pyunpack import Archive
import extract_comics, process_filenames,parse_comics, json
import os, sys


USER_ROOT = r'C:/cygwin64/home/Paola/src/hbproject/'
UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = set(['cbr','cbz','cbt','cba','cb7'])
# ALLOWED_EXTENSIONS = set(['cbr','cbz','pdf', 'png', 'jpg', 'jpeg', 'gif','bmp','tiff'])


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
    mix_publishers = set([])
    mix_titles = set([])
    publishers = Publisher.query.all()
    
    genres = Genre.query.all()
    books = Book.query.all()
    # print "Book TYPE", type(books)
    # loggedin_user = session['login_id'][2]
    # print "USER LOGGED IN",loggedin_user

    up_books = db.session.query(Book,Publisher).join(Publisher).all()


    for book,pub in up_books:
        pubs = (str(pub.name_short),pub.name)
        titles = (str(book.title_short),book.title)
        mix_publishers.add(pubs)
        mix_titles.add(titles)

    # print "UP_BOOK TYPE", type(up_books)
    # print mix_publishers
    # print mix_titles
    # print up_books
    # for book in mix_controls:
    #     print book
    # import pdb; pdb.set_trace()


    return render_template("homepage.html",publishers=publishers,genres=genres,books=books,up_books=up_books, mix_titles=mix_titles, mix_publishers=mix_publishers)







"""
###################################
    WORK ROUTES
###################################

"""

@app.route('/open_book',methods=['GET','POST'])
def open_books():
    """
    Open Comic book 
    """

    if request.method == 'POST':
        path = request.form['random']

        pages = extract_comics.get_pages(path)
        print "MY PATH: ", path
        print pages
        print "******"
        print jsonify(pages)
        return jsonify(pages)

    return render_template('profile.html')



@app.route('/upload', methods=['POST'])
def upload():
    """
    upload files 
    """

    uploaded_files = request.files.getlist("file[]")
    filenames = []

    for file in uploaded_files:
        path = ""
        issue_path = ""
        icover_path = ""

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            info = process_filenames.walk_files(filename)
            #process filename, extract name and issue number
            #to use for path
            folder_name= info['comics'][0]['name']
            print 'FOLDER NAME ONLY', folder_name
 
            # path = NAME OF THE FOLDER WHERE ALL ISSUES ARE SAVED
            path = UPLOAD_FOLDER + folder_name
            folder_path = path
            print "PATH BEFORE JOIN", path
            # import pdb; pdb.set_trace()
            path = os.path.join(USER_ROOT,path)
            print "STRING PATH: ", path
            #CHECK IF PATH IS A DIR. IF NOT MAKE ONE.
            if os.path.isdir(path) == False:
                new_dir = os.makedirs(path)

            file.save(os.path.join(path,filename))

            filenames.append(filename)

            #GET FORM DATA#######
            form_pub = request.form.get("publishers")
            form_gen = request.form.get("genres")
            # form_gen = request.form.get("tags")
            lang = 'English'

            #GET PUBLISHERID AND GENREID FROM DB
            pub_id = Publisher.query.filter_by(name=form_pub).first()
            gen_id = Genre.query.filter_by(genre=form_gen).first()

            #FROM INFO DICTIONARY
            year = int(info['comics'][0]['year'])
            issue_number = int(info['comics'][0]['issue_number'])
            file_name = info['comics'][0]['file']

            #UNPACK COMICS GET ISSUE PATH AND COVER ISSUE PATH in that order
            ci_paths = parse_comics.unpack_rars(path)


            print "ALL PATHS RETURNED: ", ci_paths
            issue_path = os.path.join(folder_path,ci_paths[2])
            print "STR ISSUE PATH:", issue_path
            icover_path = os.path.join(issue_path,ci_paths[1])
            print "STR COVER PATH: ", icover_path

            #COMMIT
            short_title = folder_name.replace(" ", "").lower()
            user = session['login_id'][2]
            book = Book(publisher_id=pub_id.publisher_id,user_id=user,title=folder_name,title_short=short_title,year=year,issue_number=issue_number,language=lang,file_name=file_name,comicfolder_path=issue_path,coverimage_path=icover_path)
            # genre = BookGenre()
            db.session.add(book)
            print 'ADDED TO SESSION'
    # comic_info = process_filenames.walk_files(filenames)
    db.session.commit()
    print 'ADDED TO DATABASE'
    return redirect ('/')
    # return render_template('upload.html',filenames=filenames)


# @app.route('/upload/<filename>')
# def uploaded_file(filename):



#     return send_from_directory(app.config['UPLOAD_FOLDER'],filename)





"""
###################################
    PROFILE
###################################

"""



@app.route('/users/<int:id>')
def user_profile(id):
    """Show user profile
   
    """
    this_user = User.query.filter_by(user_id=id).one()
    publishers = Publisher.query.all()
    genres = Genre.query.all()



    return render_template("profile.html", publishers=publishers, genres=genres, this_user=this_user )



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
        u_id = ""


        dbemails = db.session.query(User.email).all()

        print email, type(email)
        print "Query Ran"
        # print type(dbemails)

        user = User.query.filter_by(email=email).first()
        u_id = user.user_id
        name = user.name

        credentials = (email, password, u_id, name)

        print user.user_id, user.name
        # print user

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
            print session['login_id'][2]
            # flash('You were successfully logged in')
            return redirect("/")
            # return redirect("/users/%s" % user.user_id) # REDIRECT TO PROFILE PAGE.FIX
            # return redirect ("/")


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


        user = User.query.filter_by(email=email).first()
        c_name = user.name
        c_email = user.email

        # if

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
    # DebugToolbarExtension(app)

    app.run()
