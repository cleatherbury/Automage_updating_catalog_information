#!/usr/bin/env python3
import os, time
import requests

cwd = os.getcwd()
fd = cwd + '/supplier-data/images/'
osld = os.listdir(fd)
url = "http://34.29.193.76/upload/"
f
for i in osld:
  fp = (fd + i)
  if i.endswith('.jpeg'):
      with open(fd + i, 'rb') as img:
        r = requests.post(url, files={'file' : img})
        r.raise_for_status()  # Raise an exception if the request fails          
        print(f"Image {i} uploaded successfully.")