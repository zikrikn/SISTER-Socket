#UDP Client
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
PESAN = input(" -> ")

print("target IP : ", UDP_IP)
print("target port:", UDP_PORT)

while PESAN.lower().strip() != 'bye':
    print("pesan : ", PESAN)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP

    sock.sendto(PESAN.encode (), (UDP_IP, UDP_PORT))
    
    PESAN = input(" -> ")