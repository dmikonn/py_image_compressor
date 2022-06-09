import os
from PIL import Image
from readable_size import get_size_format

def get_input_image(image_name, new_image_name):

    if new_image_name:
        # get the original image size in bytes
        image_size = os.path.getsize(image_name)
        # get the new image size in bytes
        new_image_size = os.path.getsize(new_image_name)
        # print the new size in a good format
        print("[+] Size after compression:", get_size_format(new_image_size))
        # calculate the saving bytes
        saving_diff = new_image_size - image_size
        # print the saving percentage
        print(f"[+] Image size change: {saving_diff / image_size * 100:.2f}% of the original image size.")

    else:
        # load the image to memory
        img = Image.open(image_name)
        # print the original image shape
        print("[*] Image shape:", img.size)
        # get the original image size in bytes
        image_size = os.path.getsize(image_name)
        # print the size before compression/resizing
        print("[*] Size before compression:", get_size_format(image_size))