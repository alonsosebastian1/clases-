import os 
import time
import sys 
import time
import random
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

to_dir = "C:\\Users\\alons\\Downloads"
from_dir = "C:\\Users\\alons\\Desktop\\prueba\\Imagenes"
dir_tree  ={
    "image_files":['.jpg','.jpeg','.png','.gif'],
    "video_files":['.mp4',".mov",'.mp3'],
    "document_files":['.ppt','.pdf','.txt','.xlsx','docx'],
    "setup_files":['.exe','.cmd',".bin"]
}
class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        name,extension = os.path.splitext(event.src_path)
        time.sleep(1)
        for key, value in dir_tree.items():
            time.sleep(1)
            if extension in value:
                file_name = os.path.basename(event.src_path)
                print("decargado" + file_name)
                path1 = from_dir + "\\" + file_name
                path2 = to_dir + "\\" + key
                path3 = to_dir + "\\" + key + "\\" + file_name
                if os.path.exists(path2):
                    print("el directorio no existe")
                    print("moviendo" + file_name + "...")
                    shutil.move(path1,path3)
                    time.sleep(1)
                else:
                    print("creando directorio")
                    os.makedirs(path2)
                    print("moviendo"+file_name + "...")
                    shutil.move(path1,path3)
                    time.sleep(1)
event_handler = FileMovementHandler()
observer = Observer()
observer.schedule(event_handler,from_dir,recursive=True)
observer.start()
try:
    while True:
        time.sleep(2)
        print("ejecutando")
except KeyboardInterrupt:
    print("detenido")
    observer.stop() 