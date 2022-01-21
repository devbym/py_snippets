
import base64, io, os
from PIL import Image


def PNGtoB64(path_to_icon):
    if not os.path.isfile(path_to_icon):
        return "No filepath Found"
    with open(path_to_icon,"r+b") as infile:
        i = infile.read()
        b = base64.encodestring(i).strip()
        return f"data:image/png:base64,{b.decode('utf-8')}"

def B64toPNG(png_string_or_byte_string):
    png = png_string_or_byte_string
    if type(png) != bytes:
        img = bytes(png.split(",")[-1],encoding="utf-8")
    else:
        img = png
    img = base64.decodestring(img)
    img = Image.open(io.BytesIO(img))
    return img

def list_pictures_in_homefolder():
    pics_abs = os.path.abspath("Pictures")
    png_list = [x.path for x in os.scandir(pics_abs) if x.name.endswith("png")]
    return png_list


if __name__== '__main__':
    i = input("B64 bytestring or filepath to PNG")
    if i == "list":
        x = list_pictures_in_homefolder()
        for p in x:
            print(p)
    try:
        x = PNGtoB64(i)
        print(f"converted PNG to B64:\n {x}")
    except:
        pass
    try:
        x = B64toPNG(i)
        print(f"Converted B64 to PNG: \n {x}")
    except:
        print("Input error")    
        

