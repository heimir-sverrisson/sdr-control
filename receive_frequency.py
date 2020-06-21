import socket
import json

UDP_IP = "192.168.86.213"
UDP_PORT = 4242

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print(data)
    setting = json.loads(data)
    print(setting["mode"])
