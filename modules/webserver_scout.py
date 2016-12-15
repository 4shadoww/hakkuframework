#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
from core import colors
from collections import OrderedDict
import http.client
from core.messages import *
import socket

conf = {
	"name": "webserver_scout",
	"version": "1.0",
	"shortdesc": "get information from webserver",
	"author": "4shadoww",
	"github": "4shadoww",
	"email": "4shadoww0@gmail.com",
	"initdate": "17.5.2016"
}

# List of the variables
variables = OrderedDict((
	('target', 'google.com'),
	('timeout', '1'),
))

# Description for variables
vdesc = [
	'target address',
	'timeout (default: 1)',
]


# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	try:
		try:
			socket.setdefaulttimeout(float(variables['timeout']))
		except ValueError:
			printerror('invalid timeout')
		conn = http.client.HTTPConnection(variables['target'])
		conn.request("HEAD","/index.html")
		res = conn.getresponse()
		results = res.getheaders()
		print('')
		for item in results:
			print(colors.yellow+item[0], item[1]+colors.end)
		print('')
	except http.client.InvalidURL:
		printerror('invalid url')
	except socket.gaierror:
		printerror('name or service not known')
	except socket.timeout:
		printerror('timeout')