#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 19:42:14 2017

@author: rhdzmota
"""

# %% Imports 

from PIL import Image
import numpy as np
import requests
import wget
import os

def log(text):
    print(str(text))
    sys.stdout.flush()

# %% Download Image

def downloadImage(img_url):
    image_filename = wget.download(img_url)
    return image_filename
    

# %% Open Image

def openImage(image_filename):
    #im = Image.open(image_filename)
    with open(image_filename, "rb") as imageFile:
        image_file = imageFile.read()
        im = bytearray(image_file)
    return im 

# %% Save Image

def saveImage(im):
    bytes_array = bytearray(im)
    with open("img.jpg", "wb") as new_image_file:
        new_image_file.write(bytes_array)
        
    return True 

# %% Get Image 

def getImage(img_url):
    # returns the image (bytes)
    image_filename = downloadImage(img_url)
    im = openImage(image_filename)
    os.remove(image_filename)
    return im

# %% Image as bytes 

def getNumpyImage(image_filename):
    im = getImage(img_url)
    os.remove(image_filename)
    array = np.array(im)
    return array

# %% User Info 
def getUserInfo(sender):
    pat = 'EAAEY4sHIr4cBACBhvZBLYb03gnnl9bXriwZAfpeVXIfyToNIvXMr8v3zPnSC1OS9tBBe6SNZCOdHZCg1DZA3c3yBJRKhrZBnZBH3thGHW1XQeWdEeOJwZCtDZCp4O4zXbZCAMTW912O5ZCzOl7eyw2oLDiF1Q8fRXnB43AY4vbqvHM4sQZDZD'
    #pat = os.environ["PAT"]
    userprofile_api = 'https://graph.facebook.com/v2.6/{USER_ID}?fields=first_name,last_name,profile_pic,gender&access_token={PAGE_ACCESS_TOKEN}'
    temp = eval(requests.get(userprofile_api.format(USER_ID=sender,PAGE_ACCESS_TOKEN=pat)).text)
    return temp

# %% Image text
def getImageText():
    # add api to image test
    return "" 
# %% Identify INE 

def isThisAnINE(img_url):
    # add request to azure
    identify_url = ""
    _data = {"img_url":img_url}
    r = requests.get(identify_url,data=_data)
    return r.json().get("res")

# %% Send INE 

def sendIne2DB(sender,_url):  
    facebook_data = getUserInfo(sender)
    image_text    = getImageText()    
    post_url = "http://35.162.69.59:8080/api/ine" 
    ine = {"facebookID":str(sender),
           "fName":"",
           "mName":str(facebook_data.get("last_name")),
           "lName":"",
           "Address":"",
           "ineID":"",
           "curp":""}
    try:
        r = requests.post(post_url,data=ine)
        print(r.text)
        log(r.text)
        if not r.ok:
            print("Warning: Something went wrong with sendIne2DB.")
            log("Warning: Something went wrong with sendIne2DB.")
    except:
        print("Warning: Something definitely went wrong with sendIne2DB.")
        
# %% Send Message data 
# sender = 1747126771972077
def sendMessage2DB(sender,text,timestamp):
    facebook_data = getUserInfo(sender)
    message_info = {"name":str(facebook_data.get("first_name")),
                    "gender":str(facebook_data.get("gender")),
                    "facebookID":str(sender),
                    "timestamp":int(timestamp),
                    "messageText":str(text)}
    post_url = "http://35.162.69.59:8080/api/message" 
    try:
        r = requests.post(post_url,data=message_info)
        print(r.text)
        log(r.text)
        if not r.ok:
            print("Warning: Something went wrong with sendMessage2DB.")
    except:
        print("Warning: Something definitely went wrong with sendMessage2DB.")
# %% 



# %% 

# %% 

# %% 

# %% 

# %%  