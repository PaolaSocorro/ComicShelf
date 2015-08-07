from model import Book, connect_to_db,db
from server import app
from datetime import datetime
import os
import re

root_dir = raw_input("Enter File Path: ")
# root_dir = "C:\Users\Paola\Desktop\Comic Test"


data_files ={}


for root, dirs, files in os.walk(root_dir):
    print "Root Directory: ",root 
    print "Directories in Root: ",dirs
    for i in files:
        print "A file: ", i

       n = re.compile(r'([a-zA-Z-:_(\s)]+)')
       name = n.search(i)
       y = re.compile(r'(\(\d\d\d\d\))')
       year = y.search(i)
       iss = re.compile(r'(.art\s\d)|(.art\d)|(\d\d\d)|(\d\d)|(\d)')
       issue = iss.search(i)
       e = re.compile(r'(.cb.)')
       ext = e.search(i)

       print "Title: ",name.group(), "Issue: ", issue.group(),"Year: ",year.group(),"FileType: ",ext.group()




    print " "
    print "#################################"
    print " "


print type(data_files)

#MATCHES THE ISSUE NUMBER
# (.art\s\d)|(.art\d)|(\d\d\d)|(\d\d)|(\d)

   # m = re.search('([a-zA-Z-:_(\s)]+)','\(\d\d\d\d\)','\(.*\)','(.cb.)')
