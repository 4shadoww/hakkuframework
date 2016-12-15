#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
import sys
from core import colors
from collections import OrderedDict
import socket
import subprocess
from datetime import datetime

conf = {
	"name": "port_scanner",
	"version": "1.0",
	"shortdesc": "scan open ports",
	"author": "4shadoww",
	"github": "4shadoww",
	"email": "4shadoww0@gmail.com",
	"initdate": "4.3.2016"
}

# List of the variables
variables = OrderedDict((
	('target', 'google.com'),
	('first', 1),
	('last', 100),
))

# Description for variables
vdesc = [
	'target address',
	'first port which will be scanned',
	'last port which will be scanned',
]

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	variables['target'] = variables['target'].replace("http://", "")
	variables['target'] = variables['target'].replace("https://", "")
	try:
		targetip = socket.gethostbyname(variables['target'])
	except(socket.gaierror):
		print(colors.red+'Hostname could not be resolved'+colors.end)
		return

	socket.setdefaulttimeout(0.5)

	print(colors.blue+"-" * 60)
	print("Please wait, scanning target", targetip)
	print("-" * 60+colors.end)

	t1 = datetime.now()

	end = variables['last'] + 1

	try:
		for port in range(int(variables['first']),int(end)):
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			result = sock.connect_ex((targetip, port))
			if result == 0:
				print(colors.green+"Port {}: Open".format(port)+colors.end)
			else:
				print(colors.red+"Port {}: Closed".format(port)+colors.end)

			sock.close()

	except(socket.gaierror):
		print(colors.red+'Hostname could not be resolved'+colors.end)
		sys.exit()

	except(socket.error):
		print(colors.red+"Couldn't connect to server"+colors.end)
		sys.exit()
	except(ValueError):
		print(colors.red+"Port value must be integer"+colors.end)

	# Checking the time again
	t2 = datetime.now()

	# Calculates the difference of time, to see how long it took to run the script
	total =  t2 - t1

	# Printing the information to screen
	print(colors.blue+'Scanning Completed in: ', total, colors.end)