import os
import re

root_dir = raw_input("Enter File Path: ")
# root_dir = "C:\Users\Paola\Desktop\Comic Test"


data_files ={}
num=1
key = "dirs"+ str(num)
name=""
year=""
issue=""
ext=""
end = ('.db','.jpg','.png') #EXTENSIONS TO IGNORE


for root, dirs, files in os.walk(root_dir):
    print "Root Directory: ",root 
    print "Directories in Root: ",dirs
    data_files['root']=root
    data_files[key]=files
    for i in files:
        print "A file: ", i
        n = re.compile(r'([a-zA-Z-:_(\s)]+)')
        # name = n.search(i).group()
        # name = name.group()
        y = re.compile(r'(\(\d\d\d\d\))')
        # year = y.search(i).group()
        # year = year.group()
        iss = re.compile(r'(.art\s\d)|(.art\d)|(.art_\d)|(\d\d\d)|(\d\d)|(\d)')
        # issue = iss.search(i).group()
        # issue = issue.group()
        e = re.compile(r'(.cb.)')
        # ext = e.search(i).group() 
        # import pdb; pdb.set_trace()
        if i.endswith(end):
            print "not a comic file"
        else:
            try:
                name = n.search(i).group()
                year = y.search(i).group()
                issue = iss.search(i).group()
                ext = e.search(i).group()
            except AttributeError:
               print "not enough data"


        # ext = ext.group()
        print " "
        print "Title: ",name, "Issue: ",issue,"Year: ",year,"FileType: ",ext
        print " "



       # m = re.search('\w+','\(\d\d\d\d\)','\(.*\)','.cbr')
    print " "
    print "#################################"
    print " "


print type(data_files)

# \d\d\d

# \(\d\d\d\d\)

# \(.*\)


