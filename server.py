import socket
import tqdm
import os

#device IP address
SERVER_HOST = "192.168.1.186" #0.0.0.0 OR localhost
SERVER_PORT = 8080

#receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPERATOR = "<SEPERATOR>"

#tcp scoket
s = socket.socket()

#bind socket to local address
s.bind((SERVER_HOST, SERVER_PORT))

#enable server to accept connections, number show show many accepted connections
s.listen(5)

while True:

    print(f"[*] Listening as {SERVER_HOST} : {SERVER_PORT}")

#accept any connections
    client_socket, address = s.accept()

#code executes when sender connects
    print(f"[+] {address} is connected.")

#receive file info
#receive using client socket not server socket
    received = client_socket.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPERATOR)
#remove absolute path if there is because sender may send file with their own path which may differ from ours
    filename = os.path.basename(filename) #os.path.basename() returns the final component of path name
#convert to integer
    filesize = int(filesize)

#receive file from sockets and writing to file stream
    progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for _ in progress:
        #read 1024 bytes from the socket (receiver)
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:
            #nothing is received, file transmitting is done
                break
        #write to the file the bytes we received
            f.write(bytes_read)
        #update progress bar
            progress.update(len(bytes_read))

#close client socket
    client_socket.close()
#close the server socket
#s.close()