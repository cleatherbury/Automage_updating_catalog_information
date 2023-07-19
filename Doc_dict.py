#!/usr/bin/env python3

import os

import json

import requests

feed_dir = "~/supplier_data/documentation"
file_list = os.listdir(feed_dir)
url = "http://104.198.165.104/feedback"
# Iterate over the files in the feedback directory
for filename in file_list:
  filename = feed_dir + "/" + filename
  if not filename.startswith('.'):
    with open(filename, "r") as file:
      # Extract the title, name, date, and feedback 
      fruit = file.readline().strip()
      weight = int(file.readline().strip().rstrip(' lbs'))
      description = file.read().strip()
      feedback_data = {"fruit": fruit, "weight": weight, "description": description}
    
      response = requests.post(url, data=feedback_data)
    if response.status_code == 200:
      print('Data sent accepted')
    else:
      print('Data sent rejected')