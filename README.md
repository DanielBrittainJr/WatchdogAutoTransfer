# WatchdogAutoTransfer
Automatically send files from client to server when a new file is created by using the watchdog library to monitor a folder for new files and socket to transfer them.


Instructions for use:

To use clone the repository and put the detect.py file in the folder that you new files to be monitored and sent.

Put the server.py file on the other machine in the folder that you want the files to be sent to.

Run the server.py file in the console with either "python server" or "python3 server" in the terminal within the relevent directory.
Example: ~C:\home\Media\ $ python server

The server will now run and be listening for files to be sent.
The server and watchdog files will run indefinitely so files can passively be sent. I use this for when I download files, 
they go to the directory and are automatically be sent.

To end the programs hit ctrl + c repeatedly in the terminal.
