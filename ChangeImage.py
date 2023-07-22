#!/usr/bin/env python3
from PIL import Image
import os, sys
cwd = os.getcwd()
fd = cwd + "/supplier-data/images/"
osld = os.listdir(fd)
  
for img in osld:
  if img.endswith('.tiff'):
    fn = os.path.splitext(img)[0]
    of = fd + fn + ".jpeg"
    try:
      Image.open(fd + img).resize((600, 400)).convert('RGB').save(of, 'JPEG')
    except IOError:
      print("Conversion denied", img)