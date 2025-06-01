import socket  
serverHost = "0.0.0.0"
serverPort = 8080
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind((serverHost,serverPort)) 
serverSocket.listen(5)
print(f"Server is listening on port {serverPort}...")

while True:
    clientSocket, clientAddress = serverSocket.accept()
    request = clientSocket.recv(1024).decode() 
    print(request)
    headers = request.split('\n')
    firstHeader = headers[0].split()
    httpMehthod = firstHeader[0]
    path = firstHeader[1] 
    if httpMehthod == "GET":
        if path == '/':
            fin = open('index.html')
            content = fin.read()
            fin.close()
            response = 'http/1.1 200 OK\n\n' + content
    else:
        response = 'HTTP/1.1 405 Method Not Allowed\n\n Allowed methods are GET only'
        clientSocket.sendall(response.encode())
    clientSocket.sendall(response.encode())
    clientSocket.close()