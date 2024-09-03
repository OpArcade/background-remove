# INSTALL THE rembg AND pillow LIBRARY USING "pip install rembg" AND "pip install pillow"

# it's important to install this libraries to tun this program in your system.

from rembg import remove   #importing the remove from the rembg | this help to remove the background from the image.

from PIL import Image #importing the Image from the pillow 

img = Image.open("E:\PROJECT S\python\background remove\nameLogo.png") #We create a 'img' variable and use Image to open / export save it in 'img' variable.

Img2 = remove(img) # Here we are removing the background from the image which is save in 'img' variable and save it in 'Img2' variable.

Img2.save("E:\PROJECT S\python\background remove\Remove-Logo.png") # here we are saving the output which we got from the upper function in the given path in PNG format.

#------------------------------------------------------------------------------------------#

# HERE THE SAME CODE WITH DIFFERENT IMAGE OF CAR IN WHICH WE ALSO REMOVE THE BACKGROUND AND SAVE IT IN OUR SYSTEM.

car_img = Image.open("E:\PROJECT S\python\background remove\Car.jpg")
car_img_2 = remove(car_img)
car_img_2.save("E:\PROJECT S\python\background remove\Car-remove.jpg")