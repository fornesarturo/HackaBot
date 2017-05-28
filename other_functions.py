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
    return im

# %% Image as bytes 

def getNumpyImage(image_filename):
    im = getImage(img_url)
    array = np.array(im)
    return array

# %% User Info 
def getUserInfo(sender):
    #pat = 'EAAEY4sHIr4cBACBhvZBLYb03gnnl9bXriwZAfpeVXIfyToNIvXMr8v3zPnSC1OS9tBBe6SNZCOdHZCg1DZA3c3yBJRKhrZBnZBH3thGHW1XQeWdEeOJwZCtDZCp4O4zXbZCAMTW912O5ZCzOl7eyw2oLDiF1Q8fRXnB43AY4vbqvHM4sQZDZD'
    pat = os.environ["PAT"]
    userprofile_api = 'https://graph.facebook.com/v2.6/{USER_ID}?fields=first_name,profile_pic,gender&access_token={PAGE_ACCESS_TOKEN}'
    temp = eval(requests.get(userprofile_api.format(USER_ID=sender,PAGE_ACCESS_TOKEN=pat)).text)
    return temp

# %% Identify INE 

def isThisAnINE():
    # add request to azure
    return True

# %% 
"""
{'object': 'page', 'entry': [{'id': '1939046243044035', 'time': 1495932613136, 'messaging': [{'sender': {'id': '1747126771972077'}, 'recipient': {'id': '1939046243044035'}, 'timestamp': 1495932613057, 'message': {'mid': 'mid.$cAAbjjUTNXFZifc15wVcTIgunFywI', 'seq': 189453, 'attachments': [{'type': 'image', 'payload': {'url': 'https://scontent.xx.fbcdn.net/v/t34.0-12/18816060_10156294022279966_529289128_n.jpg?_nc_ad=z-m&oh=e9df4c8dd5c0f49673977cef12871037&oe=592C9FAD'}}]}}]}]}
event = {
    'sender': {'id': '1747126771972077'}, 
    'recipient': {'id': '1939046243044035'}, 
    'timestamp': 1495932613057, 
    'message': {
            'mid': 'mid.$cAAbjjUTNXFZifc15wVcTIgunFywI', 
            'seq': 189453, 
            'attachments': [{'type': 'image',
                             'payload': {'url': 'https://scontent.xx.fbcdn.net/v/t34.0-12/18816060_10156294022279966_529289128_n.jpg?_nc_ad=z-m&oh=e9df4c8dd5c0f49673977cef12871037&oe=592C9FAD'}}]}}]}



event["message"]["attachments"][0]["payload"]["url"]
"""

 