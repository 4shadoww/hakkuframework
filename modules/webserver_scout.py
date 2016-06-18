#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
import sys
from core import bcolors
from collections import OrderedDict
import http.client
from core.messages import *
import socket

#info about module
#modules name (must be same as filename)
modulename = "webserver_scout"
#module version
version = "1.0"
#description
desc = "get information from webserver"
#creator's github
github = "4shadoww"
#created by (creators name)
createdby = "4shadoww"
#email
email = "4shadoww0@gmail.com"
#alert user if root permissions not available (remove variable below if root permissions needed)

#list of variables
variables = OrderedDict((
('target', 'google.com'),
('timeout', '1'),
))

#description for variables
vdesc = [
'target address',
'timeout (default: 1)',
]


#simple changelog
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
			print(bcolors.YEL+item[0], item[1]+bcolors.END)
		print('')
	except http.client.InvalidURL:
		printerror('invalid url')
	except socket.gaierror:
		printerror('name or service not known')
	except socket.timeout:
		printerror('timeout')