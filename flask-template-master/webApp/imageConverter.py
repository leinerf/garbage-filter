import os
import base64

def convertImageAndSaveToImages(img_data):
    name = str(img_data[:4])
    path = os.path.dirname(os.path.abspath(__file__)) + "/images/"
    with open(path + name + ".png", "wb") as fh:
        fh.write(base64.decodebytes(img_data))
    return name