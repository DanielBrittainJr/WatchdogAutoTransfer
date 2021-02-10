# WatchdogAutoTransfer
Automatically send files from client to server when a new file is created by using the watchdog library to monitor a folder for new files and socket to transfer them.

I personally use this to passively download files from the internet on my main PC and they are automatically sent to my Raspberry PI device.

Instructions for use:

1. To use, clone the repository and put the detect.py file in the folder that you would like newly created files to be monitored and sent.

2. You will need to edit the detect.py file and the server.py file and change the "host" and "SERVER_HOST" variable to the IP addess of the device that will be receiving the files.

3. Put the server.py file on the other machine in the folder that you want the files to be sent to.

4. Run the server.py file in the console with either "python server" or "python3 server" in the terminal within the relevent directory.
Example: ~C:\home\Media\ $ python server

The server will now run and be listening for files to be sent.

Run the watchdog.py file on the machine that is sending the files.

The server and watchdog files will run indefinitely so files can passively be sent. I use this for when I download files, 
they go to the directory and are automatically be sent.

5. To end the programs hit ctrl + c repeatedly in the terminal.
