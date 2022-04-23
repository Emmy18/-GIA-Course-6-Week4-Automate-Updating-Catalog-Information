#!/usr/bin/env python3

import os
from PIL import Image

value = os.getcwd()
src_dir = value + "/supplier-data/images/"
new_ext = ".jpg"
imgfiles = [x for x in os.listdir(src_dir) if x.endswith(".tiff")]
size = (600, 400)

for file in imgfiles:
    with Image.open(src_dir + file) as img:
        new_file, ext = os.path.splitext(src_dir + file)
        new_file = new_file + ".jpeg"
        img_resz = img.resize(size)
        img_conv = img_resz.convert("RGB")
        img_sav = img_conv.save(new_file, "JPEG")
