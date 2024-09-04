# INSTALL THE rembg AND pillow LIBRARY USING "pip install rembg" AND "pip install pillow"

# it's important to install this libraries to tun this program in your system.

from rembg import remove
from PIL import Image

input_path = 'Car.jpg'
output_path = 'output.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)

#------------------------------------------------------------------------------------------#

# HERE THE SAME CODE WITH DIFFERENT IMAGE OF CAR IN WHICH WE ALSO REMOVE THE BACKGROUND AND SAVE IT IN OUR SYSTEM.

# car_img = Image.open("Car.jpg")
# car_img_2 = remove(car_img)
# car_img_2.save("E:\\PROJECT S\\python\\background-remove")