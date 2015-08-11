import os
import re
import json

# root_dir = raw_input("Enter File Path: ")
root_dir = "C:\Users\Paola\Desktop\Comic Test\Forever Evil"


data_files ={}
name=""
year=""
issue=""
ext=""
end = ('.db','.jpg','.png') #EXTENSIONS TO IGNORE


for root, dirs, files in os.walk(root_dir):
    print "Root Directory: ",root 
    print "Directories in Root: ",dirs
    data_files['root']=root
    # data_files[key]=files
    for counter, i in enumerate(files):
        print "A file: ",counter, i
        n = re.compile(r'([a-zA-Z-:_(\s)]+)')
        y = re.compile(r'(\(\d\d\d\d\))')
        iss = re.compile(r'(.art\s\d)|(.art\d)|(.art_\d)|(\d\d\d)|(\d\d)|(\d)')
        e = re.compile(r'(.cb.)')
        if i.endswith(end):
            print "not a comic file"
            name=""
            year=""
            issue=""
            ext=""
        else:
            try:
                name = n.search(i).group()
                year = y.search(i).group()
                issue = iss.search(i).group()
                ext = e.search(i).group()
                data_files[counter]={
                        'id':counter
                        'name':name,
                        'issue_number':issue,
                        'year':year,
                        'extension':ext,
                        'file':i}
                # import pdb; pdb.set_trace()
            except AttributeError:
               print "not enough data"

        print " "
        print "Title: ",name, "Issue: ",issue,"Year: ",year,"FileType: ",ext
        print " "

jdata = json.dumps((data_files),sort_keys=True,indent=4, separators=(',',':'))
print jdata
print type(jdata)



