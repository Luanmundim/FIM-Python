#!/usr/bin/env python
# coding: utf-8

# In[1]:


import hashlib
import sys
import os.path
from pathlib import Path
from os import listdir
from os.path import isfile, join


# In[2]:


#getting all the files names at the folder
def nameOfFiles():
    filesNames = [f for f in listdir("FIM/Files") if isfile(join("FIM/Files", f))]
    return(filesNames)
nameOfFiles()


# In[3]:


# the main function that open all the files at the folder, 
#calculate the digest of each file and append to a final file
#that will later save to a txt
def main():
    filesHash = ''
    bufSize = 5000000
    sha512 = hashlib.sha512()
    for i in filesNames:
        with open("FIM/files/"+ i, "rb") as f:
            while True:
                data = f.read(bufSize)
                if not data:
                    break
                sha512.update(data)
                filesHash+=(sha512.hexdigest())
    return(filesHash)


# In[4]:


def createControlFile():
    with open('fileControlData.txt','w',encoding = 'utf-8') as f:
        for i in fileControl: f.write(i)
    print("File generated, Everything is OK my brother!")


# In[5]:


filesNames = nameOfFiles()
fileControl = main()
if os.path.exists("fileControlData.txt") is True:
    with open('fileControlData.txt','r',encoding = 'utf-8') as file:
        file = file.read()
        if file == fileControl:    
            print("The files are intact!")
        else:
            if len(fileControl)> len(file):
                answer = input("A file was added, do you wanna to recreate the control File?(y/n)").lower()
                if answer == "y":createControlFile()
            else: 
                answer = input("A file was removed, do you wanna to recreate the control File?(y/n)").lower()
                if answer == "y":createControlFile()
else:
    createControlFile()


# In[ ]:




