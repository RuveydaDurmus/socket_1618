import socket
import time
import struct

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = "34.234.82.161"
port = 13571
s.connect((ip, port))

connection_name = "ruveyda".ljust(32)[:32]
topic_name = "ruveyda_topic".ljust(32)[:32]
user_input = input("Enter text : ")
byte_array = bytearray(user_input.encode('utf-8'))
length = len(byte_array)
packed_value = struct.pack("!I", length)
while True:
    s.sendall(connection_name.encode('utf-8'))
    s.sendall(topic_name.encode('utf-8'))
    s.sendall(packed_value)

    data = s.recv(1024)
    print("Received:", data.decode('utf-8'))

s.close()
