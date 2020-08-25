from PIL import Image

im = Image.open('test.tif')
im = im.crop((550,1, 1100, 550))
im.save('CIcrop2.tif')