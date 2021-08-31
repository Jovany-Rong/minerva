# coding: utf-8

import pytesseract
from PIL import Image, ImageGrab

pytesseract.pytesseract.tesseract_cmd = 'lib/tesseract/tesseract.exe'

def load_img_from_file(imgPath):
    img = Image.open(imgPath)
    if isinstance(img, Image.Image):
        img.save('temp.png')
        return Image.open(imgPath)
    else:
        return None

def load_img_from_clipboard():
    img = ImageGrab.grabclipboard()
    if isinstance(img, Image.Image):
        img.save('temp.png')
        return load_img_from_file('temp.png')
    else:
        return None
    
def img_to_txt(img, lang='chi_sim'):
    custom_oem_psm_config = r'--psm 3'
    text = pytesseract.image_to_string(img, lang, config=custom_oem_psm_config)
    return text

if __name__ == "__main__":
    img1 = load_img_from_file('test.png')
    img2 = load_img_from_clipboard()
    
    print(img_to_txt(img2))
    