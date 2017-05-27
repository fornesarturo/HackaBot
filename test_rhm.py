#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 12:11:59 2017

@author: rhdzmota
"""

# %% Imports 
from PIL import Image
import wget

# %% Download Image

def downloadImage(image_url):
    image_filename = wget.download(image_url)
    return image_filename
    

# %% Open Image

def openImage(image_filename):
    im = Image.open(image_filename)
    return im 

# %% Pipeline 

def test_pipeline(image_url):
    
    image_filename = downloadImage(image_url)
    im = openImage(image_filename)

    return True 

# %% 


# %% 


# %% 

# %% 


# %% 


# %% 