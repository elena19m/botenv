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

import numpy as np
from datetime import datetime

# This file handles the random generation of IPs to be scanned in the network

def uniform():
	seed_gen()
	u = np.random.uniform(0,1,10)
	return u

def normal():
	seed_gen()
	n = np.random.normal(0,1,10)
	return n

def ip(net_start = 0, net_end = 255, host_start = 0, host_end = 255):
	seed_gen()
	net_oct = np.random.random_integers(net_start, net_end)
	host_oct = np.random.random_integers(host_start, host_end)
	return f"192.168.{net_oct}.{host_oct}"

def seed_gen():
	return np.random.seed(int(datetime.now().strftime("%d%H%f")))

def main():
	pass

if __name__ == "__main__":
	main()
