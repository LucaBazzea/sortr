import os
from datetime import datetime
import shutil
from PIL import Image
from PIL.ExifTags import TAGS
from PIL import UnidentifiedImageError

os.chdir("C:/Users/Luca/Desktop/sort")

def get_mtime(file):
    unix_time = os.path.getmtime(file) # Get timestamp
    date_time = datetime.fromtimestamp(unix_time) # Convert unix time to something human readable

    date = str(date_time).split()[0] # Get date
    year = str(date).split("-")[0] # Get year

    return year


def get_exif(file):
    try:
        image = Image.open(file)

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

        # except OSError:
        #     year = get_mtime(file)

    except:
        year = get_mtime(file)

    return year


for file in os.listdir():
    file_ext = str(file).split(".")[-1] # Get file extension

    if file_ext == "jpg" or file_ext == "jpeg" or file_ext == "JPG": # If file is not a .jpg then sorting will be done based on date modified
        year = get_exif(file)
    else:
        year = get_mtime(file)

    print(f"\t\t{file}:\t{year}")

    try:
        os.mkdir(year)
    except FileExistsError:
        pass
    except FileNotFoundError:
        pass

    try:
        if file_ext == "jpg" or file_ext == "jpeg" or file_ext == "JPG" or file_ext == "png" or file_ext == "gif" or file_ext == "webp" or file_ext == "mkv" or file_ext == "mp4": # I'll find a more elegant solution later - why are there so many names for .jpg
            shutil.move(file, year)
    except:
        print(f"\t\tError - Duplicate name: {file}")
