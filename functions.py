from tkinter import Tk, filedialog
import os
import settings
import pytesseract
from PIL import ImageGrab, Image

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def ask_folder():
    # pointing to searched directory
    root = Tk() 
    root.withdraw() 
    root.attributes('-topmost', True) 
    return filedialog.askdirectory() 
    
def list_files(folder_path):
    # lists image files
    extensions = settings.extensions
    list_of_files = os.listdir(folder_path)
    list_of_images = []
    for file in list_of_files:
        for extension in extensions:
            if file.endswith(extension):
                image = os.path.join(folder_path,file)
                list_of_images.append(image)
    return list_of_images

def read_image(imgpath):
    # extracts text from image
    text = pytesseract.image_to_string(Image.open(imgpath), lang='eng')
    return text