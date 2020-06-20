import socket
import json

UDP_IP = "192.168.42.88"
UDP_PORT = 4200

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    setting = json.loads(data)
    print(setting["uplink"])