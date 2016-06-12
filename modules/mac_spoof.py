#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
import sys
import os
from core import bcolors
from collections import OrderedDict
from scapy.all import *
from core import network_scanner
import random
from core import getpath
from core.setvar import setvar

#info about module
#modules name (must be same as filename)
modulename = "mac_spoof"
#module version
version = "1.0"
#description
desc = "mac spoof"
#creator's github
github = "4shadoww"
#created by (creators name)
createdby = "4shadoww"
#email
email = "4shadoww0@gmail.com"
#alert user if root permissions not available (remove variable below if root permissions needed)
needroot = 1

#custom commands
customcommands = (
'scan',
'random_mac',
'reset',
)

#list of variables
variables = OrderedDict((
('fake_mac', '02:a0:04:d3:00:11'),
('interface', 'eth0'),
))

#description for variables
vdesc = [
'fake mac',
'network interface',
]

mhelp =  OrderedDict((
('scan', 'scan network'),
('random_mac', 'generate random mac'),
('reset', 'end mac spoof'),
))

#additional help notes
help_notes = bcolors.WARNING+"this module will not work without root permissions!"+bcolors.END

#additional notes to options
option_notes = bcolors.YEL+" you can generate fake_mac using 'random_mac' command\n use 'reset' command to end mac spoof"+bcolors.END

#simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	xterm1 = "service network-manager stop"
	xterm2 = "ifconfig "+variables['interface']+" hw ether "+variables['fake_mac']
	xterm3 = "service network-manager start"
	print(bcolors.OKBLUE+"[*] starting mac spoof"+bcolors.YEL)
	os.system(xterm1)
	print(bcolors.OKGREEN+"trying to set fake mac address..."+bcolors.YEL)
	os.system(xterm2)
	os.system(xterm3)
	print(bcolors.OKGREEN+"done!"+bcolors.END)

def scan():
	network_scanner.scan()

def random_mac():
	mac = "f4:ac:c1:%02x:%02x:%02x" % (
		random.randint(0, 255),
		random.randint(0, 255),
		random.randint(0, 255),
	)
	setvar('fake_mac', mac)

def reset():
	command = ['ethtool', '-P', variables['interface']]
	output = subprocess.Popen( command, stdout=subprocess.PIPE ).communicate()[0]
	realmac = str(output)
	realmac = realmac.replace("b'Permanent address: ", "")
	realmac = realmac.replace("'", "")
	realmac =  realmac[:-2]
	if not realmac:
		print(bcolors.WARNING+"[!] error"+bcolors.END)
	else:
		print(bcolors.OKBLUE+"realmac: "+realmac)
		xterm1a = "service network-manager stop"
		xterm2a = "ifconfig "+variables['interface']+" hw ether "+realmac
		xterm3a = "service network-manager start"
		print("[*] setting real mac"+bcolors.YEL)
		os.system(xterm1a)
		print(bcolors.OKGREEN+"trying to set real mac address..."+bcolors.YEL)
		os.system(xterm2a)
		os.system(xterm3a)
		print(bcolors.OKGREEN+"done!"+bcolors.END)