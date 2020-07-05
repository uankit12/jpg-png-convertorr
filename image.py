# import libraries

import sys
import os
from PIL import Image

# grab first and second argument from the command line

folder = sys.argv[1]  # Folder where user contains images
new_folder = sys.argv[2]  # Modififed Images stored in this folder

# check if new folder exists , if not create

if not os.path.exists(new_folder):
    os.makedirs(new_folder)  # creates new path if does not exist
    print(f'{new_folder} created ! ')

# loop through user images folder

try :
    for filename in os.listdir(folder):
        if filename.endswith(".jpeg") or filename.endswith(".jpg"):
            img = Image.open(f'{folder}/{filename}')
            clean_name = os.path.splitext(filename)[0]
            img.save(f'{new_folder}/{clean_name}.png', 'png')   # convert images to png & save to the new folder
        else :
            continue
    print('All done!')
except :
    print('Error while processing your file ! ')





