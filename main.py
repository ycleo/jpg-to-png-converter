import sys
import os
from PIL import Image

# grab first and second arguments
origin_folder = sys.argv[1]
target_folder = sys.argv[2]

# check wether new/ exists, if not, create it
if not os.path.isdir(target_folder):
    os.makedirs(target_folder)

# loop through pokemon folder and save to new/ folder
for filename in os.listdir(origin_folder):
    im = Image.open(f"{origin_folder}/{filename}")
    clean_name = os.path.splitext(filename)[0]
    im.save(f"{target_folder}/{clean_name}.png", "png")
    print(f"{filename} has been converted to {clean_name}.png")
