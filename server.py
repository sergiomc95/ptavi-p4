#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Servidor UDP con handle de registro."""

import socketserver
import sys
import json
from datetime import datetime, date, time, timedelta

try:
    PORT = int(sys.argv[1])
except IndexError:
    sys.exit("Usage: python3 server.py <port>")

Time = '%Y-%m-%d %H:%M:%S'


class SIPRegistrerHandler(socketserver.DatagramRequestHandler):
    """SIP Register and .json file."""  
    
    List = []
    Users = {}

    def json2registered(self):
        """If registered.json exist."""
        try:
            with open("registered.json", "r") as jsonfile:
                self.Users = json.load(jsonfile)
                print(self.Users)

        except:
            pass

    def register2_json(self):
        """registered.json file."""
        with open("registered.json", "w") as jsonfile:
            json.dump(self.Users, jsonfile, indent=3)

    def handle(self):
        """Request handled in this method."""
        self.json2registered()
        IP = self.client_address[0]
        PORT = self.client_address[1]
        Users = {'USER': '', 'IP': '', 'EXPIRES': ''}
        print("Client_IP: ", IP + "\t", "Client_Port: ", PORT)

        Lineas = self.rfile.read()
        Lineas = Lineas.decode('utf-8').split()
        Info = Lines.decode('utf-8').split()
        METHOD = Info[0]
        USER = Info[1].split(':')[1]
        EXPIRES = Info[-1]

        if Method == 'REGISTER':
            try:

                if (EXPIRES) == 0:
                    del self.Users['USER']
                    self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
                else:
                    EXPIRES = datetime.now() + timedelta(seconds=EXPIRES)
                    Date = EXPIRES.strftime(Time)
                    self.Users[USER] = [str(IP), Date]
                    self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")

            except KeyError:
                print("No User registered")
        for user in self.Users:
            Now = datetime.now().strftime(Time)
            Date = self.Users[user][1]
            if Date >= Now:
                del self.Users[USER]
        print(self.Users)
        self.register2_json()


if __name__ == "__main__":
    serv = socketserver.UDPServer(('', PORT), SIPRegistrerHandler)
    print("\n" + "Lanzando servidor UDP de eco LOCAL - PUERTO: " +
          str(PORT) + "\n")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
