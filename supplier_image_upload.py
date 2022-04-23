#!/usr/bin/env python3
import os
import requests

url = "http://localhost/upload/"

src_dir = "supplier-data/images/"

imgfiles = [x for x in os.listdir(src_dir) if x.endswith(".jpeg")]

for img in imgfiles:
    with open(src_dir + img, 'rb') as jpegfiles:
        r = requests.post(url, files={'file': jpegfiles})
