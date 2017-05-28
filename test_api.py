#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 05:24:38 2017

@author: rhdzmota
"""

# %% 
from other_functions import *

# %% 

a = {'object': 'page', 'entry': [{'id': '1939046243044035', 'time': 1495966105445, 'messaging': [{'sender': {'id': '1747126771972077'}, 'recipient': {'id': '1939046243044035'}, 'timestamp': 1495966105311, 'message': {'mid': 'mid.$cAAbjjUTNXFZif8yG31cToc63MxZj', 'seq': 189831, 'text': 'TestMessage'}}]}]}
event = a["entry"][0]["messaging"][0]# %% 


# %% 
sender = event['sender']['id']
text = event['message'].get('text')
timestamp = event['timestamp']
sendMessage2DB(sender,text,timestamp)
# %% 
print("alright")

# %% 

# %% 

# %% 

# %% 

# %% 

# %% 

# %% 

# %% 

# %% 

# %% 

# %% 

# %% 

# %% 

# %% 