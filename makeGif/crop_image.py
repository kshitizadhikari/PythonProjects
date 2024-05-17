import os
from PIL import Image

crop_image_number = 0

# Set a folder to save cropped images
output_folder = "cropped_images"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get the image
image = Image.open("original_image.jpg")

# Get image dimensions
width, height = image.size

# Define the dimensions for the cropped images
crop_image_width = 910
crop_image_height = 910

# Crop image and save it
for left in range(0, width, crop_image_width):
    for top in range(0, height, crop_image_height):
        right = min(left + crop_image_width, width)
        bottom = min(top + crop_image_height, height)

        print(f"Left: {left}\nRight: {right }" )
        print(f"Top: {top}\nBottom: {bottom }" )
        box = (left, top, right, bottom)
        cropped_image = image.crop(box)
        cropped_image_save_path = os.path.join(output_folder, f"crop{crop_image_number}.jpg")
        print(cropped_image_save_path,"\n")
        cropped_image.save(cropped_image_save_path)
        crop_image_number += 1

print("Images cropped and saved successfully")
