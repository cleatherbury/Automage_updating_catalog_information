#!/usr/bin/env python3

import os

import json

import requests

fd = os.path.join(os.getcwd(),'supplier-data', 'descriptions')
osld = os.listdir(fd)
url = "http://localhost/fruits"

def create_dd():# Iterate over the files in the feedback directory
  ddl = []
  for filename in osld:
    filepath = os.join(fd, filename)
    if not filename.startswith('.'):
      with open(filepath, "r") as f:
      # Extract the title, name, date, and feedback 
        fruit = f.readline().strip()
        weight = int(f.readline().rstrip(' lbs'))
        description = f.read().strip()
        img = filename.split('.')[0] + 'jpeg'
        dd = {"fruit": fruit, "weight": weight, "description": description,"image": img}
        ddl.append(dd)
      print(ddl)

  return ddl

def convert_to_json(ddl):
  ddj = json.dumps(ddl)
  return ddj
      

def upload_json(ddj):     
    response = requests.post(url, data=ddj)
    if response.status_code == 200:
      print('Data sent accepted')
    else:
      print('Data sent rejected')