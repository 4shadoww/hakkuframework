#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
import sys
from core import bcolors
from collections import OrderedDict
import socket


#info about module
#modules name (must be same as filename)
modulename = "hostname_resolver"
#module version
version = "1.0"
#description
desc = "resolver hostname using ip"
#creator's github
github = "4shadoww"
#created by (creators name)
createdby = "4shadoww"
#email
email = "4shadoww0@gmail.com"

#list of variables
variables = OrderedDict((
('target', '192.168.1.1'),
))

#description for variables
vdesc = [
'target ip address',
]


#simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	try:
		querly = socket.gethostbyaddr(variables['target'])
		print(bcolors.YEL+"resolved hostname:", querly[0]+bcolors.END)
	except(socket.herror):
		print(bcolors.WARNING+"unknown host"+bcolors.END)
	except(socket.gaierror):
		print(bcolors.WARNING+"name or service not known"+bcolors.END)