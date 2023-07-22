#!/usr/bin/env python3
import requests
'''This example shows how a file can be uploaded using the Python Requests module'''
url = "https://httpbin.org/post"
with open('/Users/chris/Sites/test.php', 'rb') as opened:
    r = requests.post(url, files={'file': opened})