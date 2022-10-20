import os
from PIL import Image
from PIL.ExifTags import TAGS


file = "{File you want to view}"

file_ext = str(file).split(".")[-1] # Get file extension

image = Image.open(file)

if file_ext == "jpg" or file_ext == "jpeg" or file_ext == "JPG":
    print(file)

    exif = {}
    
    for tag, value in image._getexif().items():
        if tag in TAGS:
            exif[TAGS[tag]] = value
        
        try:
            date = exif["DateTimeOriginal"]

            year = date.split(":")[0]

        except KeyError:
            date = exif["DateTime"]

            year = date.split(":")[0]

    print(exif)

    