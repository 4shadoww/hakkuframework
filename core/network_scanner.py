import sys
import os
from scapy.all import srp,Ether,ARP,conf
from datetime import datetime
import netifaces
from core import bcolors

def scan():
	print(bcolors.OKBLUE+"interfaces:"+bcolors.END)
	try:
		for iface in netifaces.interfaces():
			print(bcolors.YEL+iface+bcolors.END)
	except(ValueError):
		print(bcolors.WARNING+"error: invalid range"+bcolors.END)
		return
	print("")
	interface = input(bcolors.HEADER+"interface: "+bcolors.END)
	print(bcolors.OKBLUE+"\n[*] default range 24"+bcolors.END)
	iprange = input(bcolors.HEADER+"range: "+bcolors.END)
	try:
		ip = netifaces.ifaddresses(interface)[2][0]['addr']
	except(ValueError):
		print(bcolors.WARNING+"error: invalid interface"+bcolors.END)
		return
	ips = ip+"/"+iprange
	print(bcolors.OKGREEN+"\n[*] scanning...\n"+bcolors.END)

	start_time = datetime.now()

	conf.verb = 0
	try:
		ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = ips), timeout = 2,iface=interface,inter=0.1)
	except(ValueError):
		print(bcolors.WARNING+"error: invalid range"+bcolors.END)
		return

	print(bcolors.OKBLUE+"MAC - IP"+bcolors.END)

	for snd,rcv in ans:
		print(rcv.sprintf(bcolors.YEL+"r%Ether.src% - %ARP.psrc%"+bcolors.END))
	stop_time = datetime.now()
	total_time = stop_time - start_time
	print(bcolors.OKGREEN+"\n[*] scan completed")
	print("[*] scan duration:",total_time,bcolors.END)