#!/usr/bin/env python3
import os
import requests

def file_upload():
  # This example shows how a file can be uploaded using
  # The Python Requests module
  fd = os.getcwd() + '/supplier-data/images'
  osld = os.listdir(fd)
  for i in osld:
    if i.endswith('.jpeg'):
      filepath = os.path.join(fd, i)
      url = "http://localhost:80/upload"
      try:
        with open(filepath, 'rb') as img:
          files = {'file': img}
          response = requests.post(url, files=files)
          response.raise_for_status()  # Raise an exception if the request fails
          print(f"Image {i} uploaded successfully.")
      except requests.exceptions.RequestException as e:
        print(f"Error uploading {i}: {e}")

def main():
  file_upload()

__name__ == '__main__'
main()

