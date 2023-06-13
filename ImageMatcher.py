import cv2
import os, glob
import numpy as np
from shutil import copy2
import shutil, sys
import csv

#If you want, create a csv that you want it to print the matched filenames to.  The path goes at the bottom of the code.  It doesn't create #it automatically, but I'll fix that in a couple of days, I'm practicing how these repositories work.

folder="Path to folder you want to search" #At least one folder to sort the images of.
folder3="Path to folder you want to search" #The rest are optional but you can also add more.
folder4="Path to folder you want to search" #You only really need "folder" and "folder2".
folder5="Path to folder you want to search" 
folder2="./ImageConsolidation/Duplicates/" #Folder 2 is wherever you want the duplicate images to go.  Make a new folder for this, any path #is fine.

initialfolders=[folder, folder3, folder4, folder5] #Put the folder variables that you want to iterate over here.  One is fine.
imagelist=[]
errors=[]
folders=[] #this index is to get the right folder path for each image.
filetypes=["*.jpg", "*.jpeg", "*.png", "*.webp"] #Next version might have a preference for saving "anything but webp when there's an option"


for folder in initialfolders:
    for filetype in filetypes:
        for filename in glob.glob(os.path.join(folder, filetype)):

            imagelist.append(filename)
            folders.append(folder)

x=(len(imagelist)-1)
y=0
matches=[]


def shortener(string):
    index=string.rfind('/')+1
    string=string[index:]
    return string 

def iter(imglistlen):
    global imagelist
    global x
    global y
    while x>0: #All matches with first image in the list.
        if open(imagelist[y],"rb").read() == open(imagelist[x],"rb").read():
            matchstring="{} and {} are the same.".format(imagelist[y], imagelist[x])
            matches.append(matchstring+",")
                
            shortname=shortener(imagelist[x])#Define a method to get just the filename.
            foldersrc=folders[x]
        
            src="{}{}".format(foldersrc, shortname)
            dest="{}{}".format(folder2, shortname)
            try:
                shutil.move(src, dest, copy_function=copy2)
                imagelist.remove(imagelist[x])
                folders.remove(folders[x])
               #This just removes each match as it goes but keeps the first image.
                print("Moved One!!")
            except:
                ("Error!")
                errors.append(src)

        else:
            pass

        print(x)
        
        x=x-1#All matches with first image in the list.
    imagelist.remove(imagelist[y])   
    folders.remove(folders[y]) 
    return imagelist, folders  

while len(imagelist)>0:
    iter(len(imagelist))
    x=(len(imagelist))-1
    
with open('./MatchedImages.csv', 'w') as f:  #Put the path to the CSV you made here.
    writer = csv.writer(f)
    writer.writerows(matches)
print(matches)
print("Errors: {}".format(errors))








