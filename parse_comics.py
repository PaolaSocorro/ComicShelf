import os, sys
import zipfile
import rarfile 
import tarfile
# root = "C:\cygwin64\home\Paola\src\hbproject\static\comic_test"

# class Unpacker(object):

#     def __init__(self, filetype):
#         self.filetype = os.path.splitext(filetype)[-1].lower()






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
            folder_path = issue_path
            # zip_file.printdir()
            #MAKES PATH TO FIRST IMAGE IN THE ISSUE
            issue_path = os.path.join(root, issue_path)
            icover_path = os.listdir(issue_path)[0]
            # icover_path = os.path.join(issue_path, icover_path)
            # print "parse_comics issue_path: ", issue_path
            # print "parse_comics icover_path: ", icover_path

    return [issue_path,icover_path,folder_path]


def find_images(folder,img_type):
    """
    Traverse folder directory and find images

    """
    pass


def unpack_rars(root):
    """
    Extracts rars from rarfile.
    Makes folder for all images.
    RETURNS: PATH to folder, and cover image in folder.
    """

    # import pdb; pdb.set_trace()
    ALLOWED_EXTENSIONS = set(['.cbr','.cbz','.cbt'])


    for f in os.listdir(root):
        my_file = ""
        issue_path = ""
        icover_path = ""
        filetype = ''
        opened_file = ""
        print "Start: ","@"*40
        print "ThiS IS F", f

        filetype = os.path.splitext(f)[1].lower()
        print "my filetype is : ",filetype
        print "ROOT: ", root
        folder_path = os.path.splitext(f)[0]
        print "folder [0]: ", folder_path

        my_file = os.path.join(root, f)
        print my_file


        if os.path.isdir(my_file) == False and filetype in ALLOWED_EXTENSIONS:
            save_to = os.path.join(root, folder_path)
            print "SAVE TO: ", save_to


            if filetype == ".cbr":
                opened_file = rarfile.RarFile(my_file, 'r')
                print "Its a ", filetype

            elif filetype == ".cbz":
                opened_file = zipfile.ZipFile(my_file, 'r')
                print "Its a ", filetype

            elif filetype == ".cbt":
                opened_file = tarfile.TarFile(my_file, 'r')
                print "Its a ", filetype

            opened_file.extractall(save_to)

            #REMOVES THE EXTENSION FROM ZIP FILE PATH
            issue_path = sorted(opened_file.namelist())[0]

            print folder_path
            print "issue path: " ,issue_path
            #MAKES PATH TO FIRST IMAGE IN THE ISSUE
            print "BEFORE JOIN: ", issue_path

            issue_path = save_to
            print "AFTER JOIN: ", issue_path


            print "*"*10  
            new_folder = os.listdir(issue_path)[0]
            check = os.path.join(issue_path,new_folder)
            print "WTFMATE?!",new_folder
            print "is this directory: ",os.path.isdir(check) 


            if os.path.isdir(check)==False:
                icover_path = new_folder
                print "no reason a folder should be in here"
            else:
                print folder_path
                print new_folder
                issue_path = os.path.join(issue_path, new_folder)
                icover_path = os.listdir(issue_path)[0]  
                folder_path = os.path.join(folder_path,new_folder)

            print "folder_path: ",folder_path
            print "issue_path: ",issue_path
            print "cover path: ", icover_path

        # else: 
        #     print "###WHAT IS THIS###"
        #     print os.listdir(folder_path)


    return [issue_path,icover_path,folder_path]


