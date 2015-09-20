from model import Tag,Genre,Publisher, connect_to_db, db
from server import app
from datetime import datetime
# import os
# import re


def seed_publishers():
    pub_file = open("seed_data/comic_publishers.txt") # Open file

    for line in pub_file:
        #split into strings
        line = line.rstrip()
        short = line.replace(" ", "").lower()
        publisher = Publisher(name=line,name_short=short)

        db.session.add(publisher)
    db.session.commit()

    print "Publishers seeded "
    pub_file.close()


def seed_genres():
    genre_file = open("seed_data/comic_genres.txt") # Open file

    for line in genre_file:
        #split into strings
        line = line.rstrip()
        genre = Genre(genre=line)

        db.session.add(genre)
    db.session.commit()

    print "Genres seeded "
    genre_file.close()


if __name__ == "__main__":
    connect_to_db(app)
    print "Connected to db"


    db.create_all()
    seed_publishers()
    seed_genres()




#MATCHES THE ISSUE NUMBER
# (.art\s\d)|(.art\d)|(\d\d\d)|(\d\d)|(\d)

   # m = re.search('([a-zA-Z-:_(\s)]+)','\(\d\d\d\d\)','\(.*\)','(.cb.)')
