from PIL import Image
import os.path, sys

path = "C:\\Users\\NFS\\PycharmProjects\\dataset\\img_align_celeba"
dirs = os.listdir(path)

def crop():
    for item in dirs:
        fullpath = os.path.join(path,item)         #corrected
        if os.path.isfile(fullpath):
            im = Image.open(fullpath)
            f, e = os.path.splitext(fullpath)
            imCrop = im.crop((0, 20, 178, 198)) #corrected
            imResize = imCrop.resize((64,64), Image.ANTIALIAS)
            imResize.save(path + '\\cropped\\' + item, "BMP", quality=100)

crop()