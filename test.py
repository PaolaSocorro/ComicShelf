import os

# root_dir = raw_input("Enter File Path: ")
root_dir = "C:\Users\Paola\Desktop\Comic Test"

# data_files = (x[0], x[2]) for x in os.walk(root_dir)]
data_files =[]


for root, dirs, files in os.walk(root_dir):
    print "Root Directory: ",root 
    print "Directories in Root: ",dirs
    for i in files:
        print "A file: ",i
    print " "
    print "#################################"
    print " "

print type(data_files)

