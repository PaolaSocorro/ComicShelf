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
    my_zip = ""
    issue_path=""
    icover_path=""

    for f in os.listdir(root):
        
        my_zip = os.path.join(root, f)
        # print my_zip
        if os.path.isdir(my_zip) == False:
            zip_file = zipfile.ZipFile(my_zip, 'r')
            zip_file.extractall(root)

            #REMOVES THE EXTENSION FROM ZIP FILE PATH
            issue_path = os.path.splitext(my_zip)[0]
            print "parse_comics issue_path: ", issue_path
            #MAKES PATH TO FIRST IMAGE IN THE ISSUE
            for root,dirs,files in os.walk(root):
                # print "the files: ", files

                icover_path = files
                print "cover file: ", icover_path
# 
           
            icover_path = os.path.join(issue_path, icover_path[0])
            # print "parse_comics icover_path after join: ", icover_path

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