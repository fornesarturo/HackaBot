#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 12:11:59 2017

@author: rhdzmota
"""

# %% Imports 
from PIL import Image
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


# %% Pipeline 

def test_pipeline(img_url):
    
    image_filename = downloadImage(img_url)
    im = openImage(image_filename)

    return im 

# %% 
test_sender = '1747126771972077'

def getUserInfo(sender):
    #pat = 'EAAEY4sHIr4cBACBhvZBLYb03gnnl9bXriwZAfpeVXIfyToNIvXMr8v3zPnSC1OS9tBBe6SNZCOdHZCg1DZA3c3yBJRKhrZBnZBH3thGHW1XQeWdEeOJwZCtDZCp4O4zXbZCAMTW912O5ZCzOl7eyw2oLDiF1Q8fRXnB43AY4vbqvHM4sQZDZD'
    pat = os.environ["PAT"]
    userprofile_api = 'https://graph.facebook.com/v2.6/{USER_ID}?fields=first_name,profile_pic,gender&access_token={PAGE_ACCESS_TOKEN}'
    temp = eval(requests.get(userprofile_api.format(USER_ID=sender,PAGE_ACCESS_TOKEN=pat)).text)
    return temp
    
    
        
# %% 


# %% 


# %% 


# %% 














# %% 

"""
ARTURO
https://scontent.xx.fbcdn.net/v/t35.0-12/18765237_10209433260368806_1420608047_o.jpg?_nc_ad=z-m&oh=de88f5406cafcc13c484f0f885defc69&oe=592CB01B



https://scontent.xx.fbcdn.net/v/t34.0-12/18762691_10155503045899653_1707103226_n.jpg?_nc_ad=z-m&oh=bb994ed8788a5f36935a83dda7eaf314&oe=592B6B4E
https://scontent.xx.fbcdn.net/v/t34.0-12/18762686_10155503047199653_1881767931_n.jpg?_nc_ad=z-m&oh=8ca2a005a0589f06c7c4326fa24c8ad1&oe=592BB1A7
https://scontent.xx.fbcdn.net/v/t34.0-12/18763356_10155503049864653_881108133_n.jpg?_nc_ad=z-m&oh=0f4ea5d8c41bafd6658ce748f4826a98&oe=592C8780
https://scontent.xx.fbcdn.net/v/t34.0-12/18763348_10155503050119653_110039277_n.jpg?_nc_ad=z-m&oh=f40b1b15b5801534d18b3877a6e1b2b7&oe=592CAED5
https://scontent.xx.fbcdn.net/v/t34.0-12/18762266_10155503050344653_2083753391_n.jpg?_nc_ad=z-m&oh=a780dabec1e5b9a8dabd0831f5e4c8c7&oe=592B8182
https://scontent.xx.fbcdn.net/v/t34.0-12/18741430_10155503050659653_413175088_n.jpg?_nc_ad=z-m&oh=b2dd689019dcd10cc2086a7ad4c785c5&oe=592C96AF  
https://scontent.xx.fbcdn.net/v/t34.0-12/18816068_1214285115349037_477212658_n.jpg?_nc_ad=z-m&oh=31457fca3b9ba7dad750eddb720e1ef2&oe=592B8520
https://scontent.xx.fbcdn.net/v/t34.0-12/18762413_1214285285349020_638239059_n.jpg?_nc_ad=z-m&oh=1bc591a0232dc3b204d1525fb38a0534&oe=592B9EB6
https://scontent.xx.fbcdn.net/v/t34.0-12/18741786_1214285378682344_765968434_n.jpg?_nc_ad=z-m&oh=13f6b970d8859a60c2c7b4066e46ea42&oe=592BA33C
https://scontent.xx.fbcdn.net/v/t35.0-12/18745114_10155503054904653_1269234010_o.jpg?_nc_ad=z-m&oh=b651003c5ef3b3e5fcaeb697b43f9968&oe=592BB87A
https://scontent.xx.fbcdn.net/v/t34.0-12/18741502_10155503056184653_864250370_n.jpg?_nc_ad=z-m&oh=37be13336b64dd4d5708c0be657171cc&oe=592CA8DC


"""
# %% 

if __name__ == "__main__":
    
    img_url = "https://scontent.xx.fbcdn.net/v/t34.0-12/18762691_10155503045899653_1707103226_n.jpg?_nc_ad=z-m&oh=bb994ed8788a5f36935a83dda7eaf314&oe=592B6B4E"
    im = test_pipeline(img_url)
    
    
    
    
# %% 
newFileByteArray = bytearray(im)
newFile = open("img.jpg", "wb")
newFile.write(newFileByteArray)
newFile.close()
# %% 


# %% 


# %% 