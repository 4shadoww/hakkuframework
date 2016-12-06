#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
from core import colors
from collections import OrderedDict
import http.client
from core.messages import *
import socket

# Info about the module
# Module's name (should be same as file's name)
name = "webserver_scout"
# Module version
version = "1.0"
# Description
desc = "get information from webserver"
# Creator's github
github = "4shadoww"
# Creator's name
createdby = "4shadoww"
# Email
email = "4shadoww0@gmail.com"
# Alert user if root permissions not available (remove variable below if root permissions not needed)

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
			print(colors.yellow+item[0], item[1]+colors.end)
		print('')
	except http.client.InvalidURL:
		printerror('invalid url')
	except socket.gaierror:
		printerror('name or service not known')
	except socket.timeout:
		printerror('timeout')