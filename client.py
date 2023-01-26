import socket

def main():
    # create socket
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    # connect to server on the port.
    sc.connect(("192.168.56.1", 8080))                               

    # prompt user to input the temp in fahrenheit
    temp_F = input("Please enter temperature in Fahrenheit: ")
    sc.send(temp_F.encode())
    
    # receive response from server then print output
    temp_C = sc.recv(1024).decode()
    print("The temperature in Celsius is:",temp_C)

# execute main func
main()
