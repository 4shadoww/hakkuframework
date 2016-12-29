#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)

from core.hakkuframework import *
import socket

conf = {
	"name": "hostname_resolver",
	"version": "1.0",
	"shortdesc": "resolve hostname using ip",
	"author": "4shadoww",
	"github": "4shadoww",
	"email": "4shadoww0@gmail.com",
	"initdate": "9.5.2016",
	"lastmod": "29.12.2016",
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
		printSuccess("resolved hostname: "+ querly[0])
		return querly[0]
	except(socket.herror):
		printError("unknown host")
		return "[err] unknown host"
	except(socket.gaierror):
		printError("name or service not known")
		return "[err] name or service not known"