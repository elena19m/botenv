#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 Software Name : botenv
 SPDX-FileCopyrightText: Copyright (c) 2021 Orange
 SPDX-License-Identifier: GPL-2.0-only

 This software is distributed under the GNU General Public License v2 only,
 the text of which is available at https://spdx.org/licenses/GPL-2.0-only.html
 or see the 'LICENCE' file for more details.

 Author: Elkin AGUAS <elkin.aguas@orange.com>
"""

import socket
import threading

class cc:
    def __init__(self, name):
        self.name = name

    # Handles connection threads from bots
    def threaded_bot(self, connection):
        connection.send(str.encode('Welcome to the Server\n'))
        while True:
            data = connection.recv(2048)
            print(data)
            reply = "0x00 0x01"
            if not data:
                break
            connection.sendall(str.encode(reply))

        connection.close()

    # Starts command & control server
    def start_server(self, ip='127.0.0.1'):
        ServerSocket = socket.socket()
        host = ip
        port = 2525
        ThreadCount = 0
        thread_list = []

        try:
            ServerSocket.bind((host, port))
        except socket.error as e:
            print(str(e))

        print('Waiting for a Connection..')
        ServerSocket.listen(5)

        while True:
            bot, address = ServerSocket.accept()
            print('Connected to: ' + address[0] + ':' + str(address[1]))
            ident = threading.Thread(target=self.threaded_bot, args=(bot, ))
            ident.start()
            print("identifier: "+str(ident))
            thread_list.append(ident)
            ThreadCount = threading.active_count()

            print('Thread Number: ' + str(ThreadCount))

        ServerSocket.close()

def main():
	pass

if __name__ == "__main__":
	main()
