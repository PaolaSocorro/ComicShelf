import os, sys
from pyunpack import Archive
import patoolib

import zipfile
import shutil

import rarfile 

# root = "C:\cygwin64\home\Paola\src\hbproject\static\comic_test"

def unpack_zips(root):
    """ 
    Extracts zips from zipfile. 
    Makes folder for all images. 
    RETURNS: PATH to folder, and cover image in folder.
    """
    # import pdb; pdb.set_trace()
    for f in os.listdir(root):
        my_zip = ""
        issue_path=""
        icover_path=""

        root_path = root
        my_zip = os.path.join(root, f)

        if os.path.isdir(my_zip) == False:
            zip_file = zipfile.ZipFile(my_zip, 'r')
            zip_file.extractall(root)
            # print dir(zip_file)
            #REMOVES THE EXTENSION FROM ZIP FILE PATH
            issue_path = zip_file.namelist()[0]
            # zip_file.printdir()
            #MAKES PATH TO FIRST IMAGE IN THE ISSUE
            issue_path = os.path.join(root, issue_path)
            icover_path = os.listdir(issue_path)[0]
            icover_path = os.path.join(issue_path, icover_path)
            # print "parse_comics issue_path: ", issue_path
            # print "parse_comics icover_path: ", icover_path

    return [issue_path,icover_path]

def unpack_rars(root):
    """
    Extracts rars from rarfile.
    Makes folder for all images.
    RETURNS: PATH to folder, and cover image in folder.
    """
    my_rar = ""
    issue_path = ""
    icover_path = ""
    pass





# patoolib.extract_archive(f, outdir=root)



# pwd = None
# rar = rarfile.RarFile(f)
# rar.extractall(root,None,pwd)

# print f, type(f)