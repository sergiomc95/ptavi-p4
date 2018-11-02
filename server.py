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
        Users = {'USER':'', 'IP':'', 'EXPIRES':''}
        print("Client_IP: ", IP + "\t", "Client_Port: ", PORT)

        Lineas = self.rfile.read()
        Lineas = Lineas.decode('utf-8')
        Info = Lines.split()
        METHOD = Info[0]
        USER = Info[1].split(':')[1]
        EXPIRES = Info[-1]
            
        if Method == 'REGISTER':
            Users['User'] = User
            Users['IP'] = IP
            Users['Expires'] = EXPIRES
                
        if int(EXPIRES) == 0:
            del Users['USER']
            print(Users)
            self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
        else:
            print(Users)


if __name__ == "__main__":


    serv = socketserver.UDPServer(('', PORT), SIPRegistrerHandler)

    print("\n" + "Lanzando servidor UDP de eco LOCAL - PUERTO: " +
          str(PORT) + "\n")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
