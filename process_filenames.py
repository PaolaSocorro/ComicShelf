import re
import os

root = "C:\Users\Paola\Desktop\Comic Test\Batman Eternal"
# import pdb; pdb.set_trace()
def make_files(root_dir):
    file_names = {}

    for root, dirs, files in os.walk(root_dir):
        print "Root Directory: ",root 
        print "Directories in Root: ",dirs
        for counter, i in enumerate(files):
            file_names[counter]=i
    # for i in file_names:
    #     print i, file_names[i]

    return file_names


       


def walk_files(files):
    """walk the specified directory and get the file names within that directory"""

    data_files ={}
    data_files['comics'] = []

    name=""
    year=""
    issue=""
    ext=""
    end = ('.db','.jpg','.png') #EXTENSIONS TO IGNORE

    for key, value in files.iteritems():
        """
        # USE REGEX TO GET name, year, issue, file extension from file name.
        FIX ME:: Don't include parens in year

        FIX ME: REMOVE _ and - from name etc.
        """
        # import pdb; pdb.set_trace()

        print "A file: ",key, value
        n = re.compile(r'([a-zA-Z-:_(\s)]+)')
        y = re.compile(r'(\(\d\d\d\d\))')
        iss = re.compile(r'(.art\s\d)|(.art\d)|(.art_\d)|(\d\d\d)|(\d\d)|(\d)')
        e = re.compile(r'(.cb.)')
        #CHECK FOR non-comic file formats and ignore
        """
        #TRY TO RETRIEVE THE group from regex
        #ELSE  print not enough data. 
        FIX ME:: Retrieve what data can be found, give empty strings for the rest
        """
        try:
            name = n.search(value).group()
            year = y.search(value).group()
            issue = iss.search(value).group()
            ext = e.search(value).group()
            data_files['comics'].append({
                    'name':name,
                    'issue_number':issue,
                    'year':year,
                    'extension':ext,
                    'file':value})
            # import pdb; pdb.set_trace()
        except AttributeError:
           print "not enough data"

        print " "
        print "Title: ",name, "Issue: ",issue,"Year: ",year,"FileType: ",ext
        print " "

    for i in data_files:
        print i, data_files[i]

    return data_files

if __name__ == "__main__":

    comics = make_files(root)
    walk_files(comics)
