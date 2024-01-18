from rembg import remove
from PIL import Image

input_path = "Wallpaper.png"
output_path = "Removed_Wallpaper.png"

input_image = Image.open(input_path)

output = remove(input_image)

output.save(output_path)