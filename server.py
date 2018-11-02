#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys

try:
    PORT = int(sys.argv[1])
except IndexError:
    sys.exit("Usage: python3 server.py <port>")


class SIPRegistrerHandler(socketserver.DatagramRequestHandler):

    def handle(self):
        IP = self.client_address[0]
        PORT = self.client_address[1]
        Users = {'User: ', 'IP: '}
        print("Client_IP: ", IP + "\t", "Client_Port: ", PORT)
        self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")

        for line in self.rfile:
            line = line.decode('utf-8')
            line = line.split(' ')
            Method = line[0]
            if Method == 'REGISTER':
                User = line[1].split(':')[1]
                SIP = line[-1]
                Users['IP'] = IP
                Users['User'] = User
                print(Users)


if __name__ == "__main__":
    # Listens at localhost ('') port 6001
    # and calls the EchoHandler class to manage the request
    serv = socketserver.UDPServer(('', PORT), SIPRegistrerHandler)

    print("\n" + "Lanzando servidor UDP de eco LOCAL - PUERTO: " +
          str(PORT) + "\n")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
