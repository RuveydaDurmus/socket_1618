import socket
import time
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")

ip = "34.234.82.161"
port = 13571

s.connect((ip, port))
print("socket connected to %s" %(port))
connection_name = "ruveyda".ljust(32)[:32]
topic_name = "ruveyda_topic".ljust(32)[:32]

while(True):
    user_input = input("Enter text: ")
    byte_array = bytearray(user_input.encode('utf-8'))

    length = len(byte_array)
    packed_value = struct.pack("!I", length)
    s.sendall(connection_name.encode('utf-8'))
    s.sendall(topic_name.encode('utf-8'))
    s.sendall(packed_value)

    s.sendall(byte_array)

    time.sleep(5)

s.close()
