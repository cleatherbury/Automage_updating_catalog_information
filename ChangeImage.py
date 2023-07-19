#!/usr/bin/env python3
from PIL import Image
import os

def change_image():
  directory = os.getcwd() + '/supplier-data/images'
  osld = os.listdir(directory)
  print(directory)
  for img in osld:
    if 'tiff' in img:
      path = os.path.join(directory, img)
      new_path = os.path.join(directory, img)
      new_path = os.path.splitext(new_path)[0] + '.jpg'
      with Image.open(path) as t:
        t.resize((600,400), Image.BICUBIC).convert('RGB').save(new_path, 'JPEG')

def main():
  change_image()

__name__ == '__main__'
main()