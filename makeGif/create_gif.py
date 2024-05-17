import os 
from PIL import Image

# open cropped_images folder and append the images in a list
cropped_image_folder = "cropped_images"
images = []
for fileName in os.listdir(cropped_image_folder):
    image_path = os.path.join(cropped_image_folder, fileName)
    image = Image.open(image_path)
    images.append(image)

# set a output gif folder
gif_folder = "created_gif"
if not os.path.exists(gif_folder):
    os.makedirs(gif_folder)

gif_save_name = "firstGif.gif"
gif_save_path = os.path.join(gif_folder, gif_save_name)


# create gif
images[0].save(
    gif_save_path,
    save_all=True,
    append_images=images[1:],
    duration=100,
    loop=0
)

print("Gif created successfully")