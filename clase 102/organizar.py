from distutils import extension
from importlib.resources import path
import os 

to_dir = "C:\\Users\\Alonso\\Downloads\\Byjus\\clase 102"
from_dir = "C:\\prueba\\Imagenes"

list_of_files = os.listdir(from_dir)
#print(list_of_files)
for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)
   # print(name)
   # print(extension)
    if extension == '':
     continue
    if extension in [".gif",".jpg",".png",".jfif"]:
        path1 = from_dir + "\\" + file_name
        path2 = to_dir + "\\" + "Image_Files"
        path3 = to_dir + "\\" + "Image_Files" + "\\" + file_name
        print("path1",path1)
        print("path3",path3)
