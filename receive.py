import socket
UDP_IP = "128.141.118.251"
UDP_PORT = 5005

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", UDP_PORT))
    data, addr = sock.recvfrom(1024)
    print "received message: ", data
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto((raw_input('Message: ')).encode(), (UDP_IP, UDP_PORT))
