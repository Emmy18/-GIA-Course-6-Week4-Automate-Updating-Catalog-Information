#! /usr/bin/env python3

import os
import requests

value = os.getcwd()
fruit_dir = value + "/supplier-data/descriptions/"
fruit_dir_list = os.listdir(fruit_dir)
site = "http://localhost/fruits/"
fruits = {}

def fruit_catalog():
    for item in fruit_dir_list:
        file = fruit_dir + item
        with open(file) as desc_file:
            line = desc_file.readlines()
            fruits["name"] = line[0].strip("\n")
            fruits["weight"] = int(line[1].strip("\n").strip("lbs"))
            fruits["description"] = line[2]
            name, ext = os.path.splitext(item)
            fruits["image_name"] = name + ".jpeg"
        print(fruits)
        post = requests.post(site, json=fruits)

fruit_catalog()
