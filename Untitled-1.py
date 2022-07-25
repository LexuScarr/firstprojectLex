from distutils import extension
from pkgutil import extend_path
from watchdog.observers import Observer
import os
import time
from watchdog.events import FileSystemEventHandler

class handler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_track):
            extension = filename.split(".")
            if len(extension) > 1 and (extension[1].lower() == "txt"):            
                file = folder_track + "/" + filename
                new_path = folder_dest + "/" + filename
                os.rename(file, new_path)
            if len(extension) > 1 and (extension[1].lower() == "jpg" or extension[1].lower() == "png"):
                file = folder_track + "/" + filename
                new_path = folder_dest1 + "/" + filename
                os.rename(file, new_path)

folder_track = "C:/Users/sanch/firstprojectLex/1"
folder_dest = "C:/Users/sanch/firstprojectLex/2" 
folder_dest1 = "C:/Users/sanch/firstprojectLex/3" 

handle = handler()
Observer = Observer()
Observer.schedule(handle, folder_track, recursive=True)
Observer.start()

try:
    while(True):
        time.sleep(10)
except KeyboardInterrupt:
    Observer.stop()
        
Observer.join()