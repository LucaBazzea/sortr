from genericpath import isdir
from msilib.schema import Directory
import os
from datetime import datetime
import shutil


for file in os.listdir():
    unix_time = os.path.getmtime(file) # Get timestamp
    date_time = datetime.fromtimestamp(unix_time) # Convert unix time to something human readable

    date = str(date_time).split()[0] # Get date
    year = str(date).split("-")[0] # Get year
    file_ext = str(file).split(".")[-1] # Get file extension

    print(f"{file}: {year}")

    try:
        os.mkdir(year)
    except FileExistsError:
        pass

    try:
        if file_ext == "jpg" or file_ext == "jpeg" or file_ext == "JPG" or file_ext == "png" or file_ext == "gif" or file_ext == "webp" or file_ext == "mkv" or file_ext == "mp4": # I'll find a more elegant solution later - why are there so many names for .jpg
            shutil.move(file, year)
    except:
        print(f"Error - Duplicate name: {file}")
