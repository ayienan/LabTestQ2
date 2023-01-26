import socket

def main():
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    sc.connect(("192.168.56.1", 8080))                               

    temp_F = input("Please enter temperature in Fahrenheit: ")
    sc.send(temp_F.encode())
    
    temp_C = sc.recv(1024).decode()
    print("The temperature in Celsius is:",temp_C)

main()
