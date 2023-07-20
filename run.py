#!/usr/bin/env python3
import os
import json
import requests
import ChangeImage
from supplier_image_upload import img_upload

def create_dd():# Iterate over the files in the feedback directory
  ddl = []
  for filename in osld:
    filepath = os.path.join(fd, filename)
    if not filename.startswith('.'):
      with open(filepath, "r") as f:
      # Extract the title, name, date, and feedback 
        fruit = f.readline().strip()
        weight = int(f.readline().strip().replace('lbs', ''))
        description = f.read().strip()
        img = os.path.splitext(filename)[0] + 'jpeg'
        dd = {"name": fruit, "weight (in lbs)": weight, "description": description,"image": img}
        ddl.append(dd)
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

def main():
  ChangeImage()
  img_upload()
  fd = os.path.join(os.getcwd(),'supplier-data', 'descriptions')
  osld = os.listdir(fd)
  url = "https://httpbin.org/post"
  ddl = create_dd()
  ddj = convert_to_json(ddl)
  upload_json(ddj)



if __name__ == '__main__':
  main()