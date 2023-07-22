#!/usr/bin/env python3
import os, sys, time
import json, requests

fd = 'supplier-data/descriptions/'
osld = os.listdir(fd)
#url = "http://34.136.136.56/fruits/"
url = "https://httpbin.org/anything"
for fi in osld:
  if fi.endswith('.txt'):
    with open(fd + fi, "r") as f:
      lines = f.readlines()
      fruit = lines[0].strip()
      weight = int(lines[1].strip().replace('lbs', ''))
      description = lines[2].strip()
      fdict = {"name": fruit, "weight": weight, "description": description, "image_name": fruit + '.jpeg"'}
      print(fdict)
      try:
        r = requests.post(url, json=fd)
        r.raise_for_status()
        print(f"Data uploaded successfully")
      except requests.exceptions.RequestException as e:
        print(f"Error uploading data: {e}")+ '.jpeg'