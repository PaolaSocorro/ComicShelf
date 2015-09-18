import os
import re

# root_dir = raw_input("Enter File Path: ")
# root_dir = "C:\Users\Paola\Desktop\Comic Test"
root_dir=""

# import pdb; pdb.set_trace()

def get_pages(path):
    # root_path = {'path':"static/uploads/Batman Eternal/Batman_Eternal_001_2014_Digital_Nahga-Empire/Batman Eternal 001 (2014) (Digital) (Nahga-Empire)"}
    # path = root_path.values()[0]
    in_path = os.listdir(path)
    pages = dict(enumerate(in_path))
    # print in_path
    return pages



