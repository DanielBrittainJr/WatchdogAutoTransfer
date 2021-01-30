import sys
import socket
import os
import time
import logging
import tqdm
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler



#http://brunorocha.org/python/watching-a-directory-for-file-changes-with-python.html






def socketfunction(srcpath):
    SEPERATOR = "<SEPERATOR>"
    BUFFER_SIZE = 4096

    host = "192.168.1.186"  
    port = 8080

    #filename = MyHandler.on_created()
    filesize = os.path.getsize(srcpath)

    sock = socket.socket()

    print(f"[+] Connecting to {host}:{port}")
    sock.connect((host, port))
    print("[+] Connected.")

    sock.send(f"{srcpath}{SEPERATOR}{filesize}".encode())

    progressbar = tqdm.tqdm(range(filesize), f"Sending {srcpath}", unit="B",
    unit_scale=True, unit_divisor=1024)

    with open(srcpath, "rb") as f:
        for _ in progressbar:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            sock.sendall(bytes_read)
            
            progressbar.update(len(bytes_read))

    sock.close





class MyHandler(FileSystemEventHandler):

    def process(self, event):
        print(event.src_path, event.event_type)
        """
        event.src_path
            path/to/observed/file
        event.event_type 
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        """
        filename = event.src_path
        socketfunction(filename)

    def on_created(self, event):
        self.process(event)
    


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s', #format of 
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = "C:/Users/djbri/Desktop/Media"
    #initialize event handler
    event_handler = MyHandler()
    #initialize observer
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)





 
    #start
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
        