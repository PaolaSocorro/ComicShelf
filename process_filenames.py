import re
import os

root = "C:\Users\Paola\Desktop\Comic Test\Batman Eternal"
# import pdb; pdb.set_trace()
def make_files(root_dir):
    file_names = []

    for root, dirs, files in os.walk(root_dir):
        print "Root Directory: ",root 
        print "Directories in Root: ",dirs
        for i in files:
            # print type(i), i
            file_names.append(i)
            # file_names.append[i]
    # for i in file_names:
    #     print i, file_names[i]
    # print file_names
    return file_names



def walk_files(files):
    """walk the specified directory and get the file names within that directory"""

    """ if files is a single string, make list with one string """
    if type(files) == type('string'):
        f = files
        files=[]
        files.append(f)

    data_files ={}
    data_files['comics'] = []

    name=""
    year=""
    issue=""
    ext=""
    end = ('.db','.jpg','.png') #EXTENSIONS TO IGNORE

    for comic in files:

        """
        # USE REGEX TO GET name, year, issue, file extension from file name.
        FIX ME:: Don't include parens in year

        FIX ME: REMOVE _ and - from name etc.
        """

        # print type(comic)
        # print "A file: ", comic
        n = re.compile(r'([a-zA-Z-:_(\s)]+)')
        y = re.compile(r'(\d\d\d\d)')
        iss = re.compile(r'(.art\s\d)|(.art\d)|(.art_\d)|(\d\d\d)|(\d\d)|(\d)')
        iss = re.compile(r'(\d\d\d)|(\d\d)|(\d)')
        print 'ISSUE NUMBER!!!!', iss
        e = re.compile(r'(.cb.)')
        #CHECK FOR non-comic file formats and ignore
        """
        #TRY TO RETRIEVE THE group from regex
        #ELSE  print not enough data. 
        FIX ME:: Retrieve what data can be found, give empty strings for the rest
        """
        # import pdb; pdb.set_trace()
        try:
            name = n.search(comic).group()
            name=name.replace("_"," ").rstrip()
            # print comic
            year = y.search(comic).group()
            # print comic
            year = year.replace("(","").replace(")","")

            issue = iss.search(comic).group()
            ext = e.search(comic).group()
            data_files['comics'].append({
                    'name':name,
                    'issue_number':issue,
                    'year':year,
                    'extension':ext,
                    'file':comic})
            # import pdb; pdb.set_trace()
        except AttributeError:
           print "not enough data"

        # print " "
        # print "Title: ",name, "Issue: ",issue,"Year: ",year,"FileType: ",ext
        # print " "

    for i in data_files:
        print i, data_files[i]

    return data_files

if __name__ == "__main__":

    # comics = make_files(root)
    new_list = 'Batman_Eternal_001_2014_Digital_Nahga-Empire.cbr'

    walk_files(new_list)
