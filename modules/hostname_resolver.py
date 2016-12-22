#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
from core import colors
from collections import OrderedDict
import socket

conf = {
	"name": "hostname_resolver",
	"version": "1.0",
	"shortdesc": "resolve hostname using ip",
	"author": "4shadoww",
	"github": "4shadoww",
	"email": "4shadoww0@gmail.com",
	"initdate": "9.5.2016",
	"apisupport": True
}

# List of the variables
variables = OrderedDict((
	('target', ['192.168.1.1', 'target ip address']),
))

#simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	try:
		querly = socket.gethostbyaddr(variables['target'][0])
		print(colors.yellow+"resolved hostname:", querly[0]+colors.end)
		return querly[0]
	except(socket.herror):
		print(colors.red+"unknown host"+colors.end)
		return "error: unknown host"
	except(socket.gaierror):
		print(colors.red+"name or service not known"+colors.end)
		return "error: name or service not known"