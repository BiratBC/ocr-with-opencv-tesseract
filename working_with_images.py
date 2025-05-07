from PIL import Image

im_file = "data/test1.png"

im = Image.open(im_file)

# print(im) #prints meta data of the image loaded by Pillow
# print(im.size)
# im.show()
# im.save("/path")