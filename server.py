# 2023-cs-609
# Web server task
from socket import * 
serverSocket = socket(AF_INET, SOCK_STREAM) 
port = 7000
serverSocket.bind(('', port)) 
serverSocket.listen(1)  
print(f"Server is running on port {port}")
while True: 
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  
    print(f"Connection established with {addr}")
    try: 
        message = connectionSocket.recv(1024).decode()
        print(f"Received message: {message}")
        # checking message is not empty and GET request
        if len(message.split()) > 1 and message.split()[0] == 'GET':
            filename = message.split()[1] 
            if filename == '/':
                filename = '/HelloWorld.html' 
            try:
                # if file is founded, we will opening get file in binary mode
                f = open(filename[1:], 'rb')
                outputdata = f.read()  
                f.close()  
                connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n")
                connectionSocket.send(outputdata)
            except IOError:
                # if file is not found
                connectionSocket.send(b"HTTP/1.1 404 Not Found\r\n\r\n")
                connectionSocket.send(b"<html><head></head><body><h1>404 Not Found</h1></body></html>")
        connectionSocket.close()  
    except Exception as e:
        print(f"Error: {e}")
        connectionSocket.close()  