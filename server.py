import socket

def fahrenheit_to_celsius(temp_F):
    temp_C = (temp_F - 32) * (5/9)
    return temp_C

def main():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    serverSocket.bind(("192.168.56.1", 8080))                                  

    serverSocket.listen(1)

    print("Server had been started...waiting for client..")

    while True:
        clientSocket, client_addr = serverSocket.accept()      
        print("Got a connection from %s" % str(client_addr))

        temp_F = clientSocket.recv(1024).decode()
        temp_C = fahrenheit_to_celsius(float(temp_F))
        temp_C = round(temp_C,2)
        temp_C = str(temp_C)
        clientSocket.send(temp_C.encode())

main()
