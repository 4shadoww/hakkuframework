#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
import sys
from core import bcolors
from collections import OrderedDict
import socket
import subprocess
from datetime import datetime

#info about module
#modules name (must be same as filename)
modulename = "port_scanner"
#module version
version = "1.0"
#description
desc = "scan open ports"
#creator's github
github = "4shadoww"
#created by (creators name)
createdby = "4shadoww"
#email
email = "4shadoww0@gmail.com"

#list of variables
variables = OrderedDict((
('target', 'google.com'),
('first', 1),
('last', 100),
))

#description for variables
vdesc = [
'target address',
'first port which will be scanned',
'last port which will be scanned',
]

#simple changelog
changelog = bcolors.YEL+"Version 1.0:\nrelease"+bcolors.END

def run():
	variables['target'] = variables['target'].replace("http://", "")
	variables['target'] = variables['target'].replace("https://", "")
	try:
		targetip = socket.gethostbyname(variables['target'])
	except(socket.gaierror):
		print(bcolors.WARNING+'Hostname could not be resolved'+bcolors.END)
		return

	socket.setdefaulttimeout(0.5)

	print(bcolors.OKBLUE+"-" * 60)
	print("Please wait, scanning target", targetip)
	print("-" * 60+bcolors.END)

	t1 = datetime.now()

	end = variables['last'] + 1

	try:
		for port in range(int(variables['first']),int(end)):
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			result = sock.connect_ex((targetip, port))
			if result == 0:
				print(bcolors.OKGREEN+"Port {}: Open".format(port)+bcolors.END)
			else:
				print(bcolors.WARNING+"Port {}: Closed".format(port)+bcolors.END)

			sock.close()

	except(socket.gaierror):
		print(bcolors.WARNING+'Hostname could not be resolved'+bcolors.END)
		sys.exit()

	except(socket.error):
		print(bcolors.WARNING+"Couldn't connect to server"+bcolors.END)
		sys.exit()
	except(ValueError):
		print(bcolors.WARNING+"Port value must be integer"+bcolors.END)

	# Checking the time again
	t2 = datetime.now()

	# Calculates the difference of time, to see how long it took to run the script
	total =  t2 - t1

	# Printing the information to screen
	print(bcolors.OKBLUE+'Scanning Completed in: ', total, bcolors.END)