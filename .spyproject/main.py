# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 11:13:21 2021

@author: Pooja Gupta
"""
26/08/2021

# file A named location in the memory that can store data 
# persistance 

account = {"balance":10000,"pin":1234}

def withdraw(amount):
    if amount <= account["balance"]:
        account["balance"] -= amount
        
def check_balance(pin):
    if pin == account["pin"]:
        print(account["balance"])
    else:
        print("Incorrect pin")

       
        
check_balance(1234)        

withdraw(5000)

check_balance(1234)


# read

file = open("F://file_demo/demo.txt")

data = file.read()

print(data)


27/08/2021

file.seek(0)

print(file.read(5))

print(file.read())


file.close()

print(file.read())

print(file.readline())

print(file.readlines())


# write 

file = open("index.txt","w")

file.write("This is written by python")

file.flush()

file.close()


# write line

file = open("index.txt","w")

data_list = ["Hello\n","This is line2\n","Bye\n"]

file.writelines(data_list)

file.flush()

file.close()

# append

file = open("index.txt","a")

data_list = ["This is new line\n","appending data\n"]

file.writelines(data_list)

file.flush()

file.close()


# create

file = open("story.txt","x")

file.write("hello world")

file.flush()

file.close()

# Error
file = open("story.txt","x")



# Delete, Rename File
# Create, Rename, Delete Folders

import os

# get current working directory
os.getcwd()

# rename file
os.rename("story.txt","mystory.txt")

# delete file
os.remove("mystory.txt")


# create folder

os.mkdir("myfolder")

os.rename("myfolder","newfolder")

# change directory

os.chdir("F://file_demo/demo.txt"/newfolder")

file = open("new.txt","x")

file.close()

os.chdir("F://file_demo/demo.txt")

# use this when directory is empty
# os.rmdir("newfolder")

# when directory is not empty
import shutil

shutil.rmtree("newfolder")




# Binary File - image, music, video

# read binary

file = open("swiss.jpg","rb")

image_data = file.read()

file.close()

# write binary
file = open("swiss_copy.jpg", "wb")

file.write(image_data)

file.flush()
file.close()



#secret message 

file = oprn("new.jpg","w")

file.write("Hidden message")

file.flush()

file.close()


file = open("new.jpg")

file.read()

file.close()



# Serialization

import pickle

account = {"balance":10000,"pin":1234}


file = open("account.ser","wb")

pickle.dump(account,file)

file.close()


# Deserialization

file = open("account.ser","rb")

account = pickle.load(file)

print(account)





