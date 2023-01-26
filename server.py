import socket

# function to convert fahrenheit input to celsius
def fahrenheit_to_celsius(temp_F):
    temp_C = (temp_F - 32) * (5/9)
    return temp_C

def main():
    # create socket 
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    # bind the socket to host and port
    serverSocket.bind(("192.168.56.1", 8080))                                  

    # listen for connection
    serverSocket.listen(1)

    print("Server had been started...waiting for client..")

    while True:
        # establish connection
        clientSocket, addr = serverSocket.accept()      
        print("Got a connection from %s" % str(addr))

        temp_F = clientSocket.recv(1024).decode()
        temp_C = fahrenheit_to_celsius(float(temp_F))
        temp_C = round(temp_C,2)
        temp_C = str(temp_C)
        clientSocket.send(temp_C.encode())

#execute main func
main()
