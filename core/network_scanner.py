import sys
import os
from scapy.all import srp,Ether,ARP,conf
from datetime import datetime
import traceback
from core import colors

try:
	import netifaces
except ImportError:
	print(colors.red+'netifaces import error:\n')
	traceback.print_exc()
	print(colors.end)


def scan():
	print(colors.blue+"interfaces:"+colors.end)
	for iface in netifaces.interfaces():
		print(colors.yellow+iface+colors.end)
	print("")
	interface = input(colors.purple+"interface: "+colors.end)
	try:
		ip = netifaces.ifaddresses(interface)[2][0]['addr']
	except(ValueError):
		print(colors.red+"error: invalid interface"+colors.end)
		return
	ips = ip+"/24"
	print(colors.green+"\n[*] scanning please wait...\n"+colors.end)
	print(colors.blue+"MAC - IP"+colors.end)

	start_time = datetime.now()

	conf.verb = 0
	try:
		ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = ips), timeout = 2,iface=interface,inter=0.1)
	except PermissionError:
		print(colors.red+'error: root permissions required')
		return

	for snd,rcv in ans:
		print(rcv.sprintf(colors.yellow+"r%Ether.src% - %ARP.psrc%"+colors.end))
	stop_time = datetime.now()
	total_time = stop_time - start_time
	print(colors.green+"\n[*] scan completed")
	print("[*] scan duration:",total_time,colors.end)