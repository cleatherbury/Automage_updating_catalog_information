#!/usr/bin/env python3
from PIL import Image
import os

def change_image():
  directory = os.getcwd() + '/supplier-data/images'
  dir_list = os.listdir(directory)
  print(directory)
  for filename in dir_list:
    if 'LICENSE' not in filename and 'README' not in filename:
      path=os.path.join(directory, filename)
      new_path = os.path.join(directory, filename)
      new_path = os.path.splitext(new_path)[0] + '.jpg'
    with Image.open(path) as image:
      image.resize((600,400), Image.BICUBIC).convert('RGB').save(new_path, 'JPEG')

