from model import Publisher, connect_to_db, db
from server import app
from datetime import datetime
# import os
# import re


def seed_publishers():
    pub_file = open("seed_data/comic_publishers.txt") # Open file

    for line in pub_file:
        #split into strings
        line = line.rstrip()
        publisher = Publisher(name=line)

        db.session.add(publisher)
    db.session.commit()

    print "Publishers seeded "
    pub_file.close()


if __name__ == "__main__":
    connect_to_db(app)
    print "Connected to db"



    seed_publishers()




#MATCHES THE ISSUE NUMBER
# (.art\s\d)|(.art\d)|(\d\d\d)|(\d\d)|(\d)

   # m = re.search('([a-zA-Z-:_(\s)]+)','\(\d\d\d\d\)','\(.*\)','(.cb.)')
