#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys

try:
    SERVER = sys.argv[1]
    PORT = int(sys.argv[2])
    METHOD = sys.argv[3]
    USER = sys.argv[4]


except IndexError:
    sys.exit(" Usage: python3 client.py <server> <method> <email>")
# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:

    my_socket.connect((SERVER, PORT))

    if METHOD == "register" or METHOD == "REGISTER":

        METHOD = "REGISTER"
        line = METHOD + " sip:" + str(USER) + " SIP/2.0\r\n\r\n"
        print("Enviando:", line)
        my_socket.send(bytes(line, 'utf-8'))
        data = my_socket.recv(1024)
        print(data.decode('utf-8'))
    else:
        sys.exit(" Usage: python3 client.py <server> <method> <meail>")
print("Socket terminado. \r\n")
