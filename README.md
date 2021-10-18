# Botenv

Botenv is an easy-to-deploy environment that emulates Mirai-like botnet traffic. Botenv easily deploys and connects the main components of a botnet (C&C, bots, loader server) in a virtualized environment, allowing to build a multitude of scenarios. Botenv emulates traffic from three stages of a botnet's life-cycle: device scanning, communication with C&C server, and binary download from loader server. Additionally, with Botenv you can change the deployed botnet's topology and behavior as desired, and add new functionalities, which let's you addapt this projecty to the particular conditions and needs of your research.

The increasing adoption of IoT devices, which is expected to continue growing in coming years, has caused an increment in the use of IoT botnets. The public release of botnet's source code, as it is Mirai's case, has made possible the emergence of numerous Mirai-like botnets, making building and renting a botnet easier than ever before.

Researches are interested in studying IoT botnets, however, up to date datasets are scarsed, and the ones that exist are at risk of going outdated because IoT botnets evolve constantly to avoid mitigaion techniques.

Botenv proposes a solution to this problem, by implementing a plug-and-play set of functions that emulate Mirai-like botnet traffic, making possible to deploy an IoT botnet, emulate its traffic when scanning and connecting to servers (C&C and loader), and additionally change the botnet's topology and behavior as desired. The generated traffic can be recovered in the form of pcap files and converted to communication flows in CSV format for later use.

### Requirements
Vagrant and VirtualBox.

### Start Virtual Machines
Go the project's root folder and run the following commands to install the necessary Vagrant plugins.

```
vagrant plugin install vagrant-junos
vagrant plugin install vagrant-scp
```

1. Go to the project's root folder and start the virtual machines with the command :
```
vagrant up
```

2. Open three terminals in the project's root folder and run the following commands in order:

**Terminal 1: ** login to C&C machine and start the C&C server
```bash
vagrant ssh cc
vagrant@cc:~$ cd botenv
vagrant@cc:~$ sudo python3 cc_example.py
```

**Terminal 2: ** login to loader machine and start the loader server
```bash
vagrant ssh loader
vagrant@loader:~$ cd botenv
vagrant@loader:~$ sudo python3 loader_example.py
```

**Terminal 3: ** login to to11 machine and start a bot
```bash
vagrant ssh to11
vagrant@to11:~$ cd botenv
vagrant@to11:~$ sudo python3 bot1_example.py
```

**Terminal 4**
```bash
vagrant ssh to17
vagrant@to17:~$ cd ..
vagrant@to17:~$ cd admin1
vagrant@to17:~$ ls
```

Firstly, you should see how the bot started on terminal 3 will connect to the C&C server and start the heart beat signal. Secondly, the bot will scan the devices on the network and will try to connect to the device to17 (which has telnet installed). Finally, the bot will report the vulnerable device (to17) to the loader server, which will connect to the vulnerable device and download the necessary files to install and execute a new bot.

To see the downloaded files login to to17 and go to the admin1 folder, as done in Terminal 4.

### License
This project is licensed under the GNU [General Public License version 2](LICENSE).
