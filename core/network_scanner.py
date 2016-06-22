import sys
import os
from scapy.all import srp,Ether,ARP,conf
from datetime import datetime
import traceback
from core import bcolors
try:
	import netifaces
except ImportError:
	print(bcolors.WARNING+'netifaces import error:\n')
	traceback.print_exc()
	print(bcolors.END)


def scan():
	print(bcolors.OKBLUE+"interfaces:"+bcolors.END)
	for iface in netifaces.interfaces():
		print(bcolors.YEL+iface+bcolors.END)
	print("")
	interface = input(bcolors.HEADER+"interface: "+bcolors.END)
	try:
		ip = netifaces.ifaddresses(interface)[2][0]['addr']
	except(ValueError):
		print(bcolors.WARNING+"error: invalid interface"+bcolors.END)
		return
	ips = ip+"/24"
	print(bcolors.OKGREEN+"\n[*] scanning...\n"+bcolors.END)
	print(bcolors.OKBLUE+"MAC - IP"+bcolors.END)

	start_time = datetime.now()

	conf.verb = 0
	try:
		ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = ips), timeout = 2,iface=interface,inter=0.1)
	except PermissionError:
		print(bcolors.WARNING+'error: root permissions required')
		return

	for snd,rcv in ans:
		print(rcv.sprintf(bcolors.YEL+"r%Ether.src% - %ARP.psrc%"+bcolors.END))
	stop_time = datetime.now()
	total_time = stop_time - start_time
	print(bcolors.OKGREEN+"\n[*] scan completed")
	print("[*] scan duration:",total_time,bcolors.END)