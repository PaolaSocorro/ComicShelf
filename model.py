"""Models and database functions for Comics organization project."""

from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

###########REMEMBER TO RUN POSTGRESQL ON CONSOLE FOR NOW #########

#psql -h localhost -U postgres
################
#TO DROP ALL TABLES USE:
#psql -h localhost -U postgres < droptable.script

##############################################################################
# Model definitions

class User(db.Model):
    """User of ratings website.
    TEST: add a user
    """

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.String(20), nullable=True)


    # def __repr__(self):
    #     """Provide helpful representation when printed."""

    #     return "<User user_id=%s name=% age=%s email=%s password=%s gender=%s>" % (self.user_id, self.name, self.age, self.email, self.password, self.gender)

class Book(db.Model):
    """Book, or comic of organization app.
    TEST: Add a book

    """

    __tablename__ = "books"

    book_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publishers.publisher_id'))  # FK to publishers table
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))  # FK to users table
    title = db.Column(db.String(200), nullable=False)
    title_short = db.Column(db.String(200),nullable=False)
    release_date = db.Column(db.Date, nullable=True)
    year = db.Column(db.Integer, nullable=True)
    issue_number = db.Column(db.Integer, nullable=False)
    language = db.Column(db.String, nullable=True)
    publisher = db.Column(db.String, nullable=True)
    file_name = db.Column(db.String, nullable=False)
    comicfolder_path = db.Column(db.String, nullable=False)
    coverimage_path = db.Column(db.String, nullable=False)

    #DEFINE relationship to publisher

    publisher = db.relationship("Publisher",
                backref=db.backref("books", order_by=book_id))

    user = db.relationship("User",
            backref=db.backref("books", order_by=book_id))



class Comment(db.Model):
    """book comments in app
    TEST: ADD a comment to a book
    """

    __tablename__ = "comments"

    comment_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))  # FK TO USER TABLE
    book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'))  # FK TO BOOK TABLE
    comment = db.Column(db.String(1000), nullable=True)

    user = db.relationship("User",
                backref=db.backref("comments", order_by=comment_id))

    book = db.relationship("Book",
                backref=db.backref("comments", order_by=comment_id))




class Bookmark(db.Model):
    """Bookmarks for books. per user.
    TEST: add a bookmark to a book.
    """

    __tablename__ = "bookmarks"

    bookmark_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))  # FK TO USER TABLE
    book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'))  # FK TO BOOK TABLE
    page_number = db.Column(db.Integer, nullable=False)

    user = db.relationship("User",
                backref=db.backref("bookmarks", order_by=bookmark_id))

    book = db.relationship("Book",
                backref=db.backref("bookmarks", order_by=bookmark_id))

class Rating(db.Model):
    """Ratings table
    TEST: rate a book
    """
    __tablename__ = "ratings"


    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'))  # FK TO BOOK TABLE
    book_rating = db.Column(db.Integer, nullable=True)

    book = db.relationship("Book",
                backref=db.backref("ratings", order_by=rating_id))


class Publisher(db.Model):
    """book Publishers

    TEST: add a publisher. ex. Marvel, marvel. (check for upper, lowercase)
    """

    __tablename__ = "publishers"

    publisher_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    name_short = db.Column(db.String(100), nullable=True)



class Artist(db.Model):
    """
    Comic book artists
    """
    __tablename__ = "artists"


    artist_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'))  # FK TO BOOK TABLE
    artist_name = db.Column(db.String(100), nullable=False)
    job = db.Column(db.String(50))  # (pencils,inks colors)


    book = db.relationship("Book",
                backref=db.backref("artists", order_by=artist_id))


class Author(db.Model):
    """
    book authors
    """

    __tablename__ = "authors"

    author_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'))  # FK TO BOOK TABLE
    author_name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(20), nullable=True)

    book = db.relationship("Book",
                backref=db.backref("authors", order_by=author_id))

class Character(db.Model):
    """
    book characters, comics

    """
    __tablename__ = "characters"


    character_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'))  # FK TO BOOK TABLE
    hero_name = db.Column(db.String(100), nullable=False)
    real_name = db.Column(db.String(100), nullable=True)
    universe = db.Column(db.String(100), nullable=True)
    aliases = db.Column(db.String(500), nullable=True)

    book = db.relationship("Book",
                backref=db.backref("characters", order_by=character_id))


############


class Tag(db.Model):
    """Creates tag for a book.

    TEST: creat a few tags"""

    __tablename__ = "tags"

    tag_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    tag = db.Column(db.String(100), nullable=True)


class Genre(db.Model):
    """Creates genre for several books.

    TEST: creat an genre"""

    __tablename__ = "genres"

    genre_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    genre = db.Column(db.String(100), nullable=True)



###########
########## JOIN TABLES ##############
###########

class BookGenre(db.Model):
    """
    Join table to find the genre of a book
    """

    __tablename__ = "bookgenres"

    bookgenre_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'))  # FK TO BOOK TABLE
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'))  # FK TO GENRE TABLE


    book = db.relationship("Book",
            backref=db.backref("bookgenres", order_by=bookgenre_id))

    genre = db.relationship("Genre",
            backref=db.backref("bookgenres", order_by=bookgenre_id))



class BookTag(db.Model):
    """
    Join table to find the tag of a book
    """

    __tablename__ = "booktags"

    booktag_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.book_id')) #FK TO BOOK TABLE
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.tag_id')) #FK TO TAG TABLE



    book = db.relationship("Book",
            backref=db.backref("booktags", order_by=booktag_id))

    tag = db.relationship("Tag",
            backref=db.backref("booktags", order_by=booktag_id))




##########
##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:wildm3101@localhost:5432/comicsdb'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://paola:hackbright@localhost:5432/comics'

    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."
