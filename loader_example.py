"""
 Software Name : botenv
 SPDX-FileCopyrightText: Copyright (c) 2021 Orange
 SPDX-License-Identifier: GPL-2.0-only

 This software is distributed under the GNU General Public License v2 only,
 the text of which is available at https://spdx.org/licenses/GPL-2.0-only.html
 or see the 'LICENCE' file for more details.

 Author: Elkin AGUAS <elkin.aguas@orange.com>
"""

from botenv import servers

loader = servers.servers("loader")
#loader.device_connect()
loader.start_loader(ip='192.168.100.12')
