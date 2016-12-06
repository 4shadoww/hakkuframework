#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
from core import colors
from collections import OrderedDict
import socket


# Info about the module
# Module's name (should be same as file's name)
name = "hostname_resolver"
# Module version
version = "1.0"
# Description
desc = "resolve hostname using ip"
# Creator's github
github = "4shadoww"
# Creator's name
createdby = "4shadoww"
# Email
email = "4shadoww0@gmail.com"

# List of the variables
variables = OrderedDict((
('target', '192.168.1.1'),
))

# Description for variables
vdesc = [
'target ip address',
]


#simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	try:
		querly = socket.gethostbyaddr(variables['target'])
		print(colors.yellow+"resolved hostname:", querly[0]+colors.end)
	except(socket.herror):
		print(colors.red+"unknown host"+colors.end)
	except(socket.gaierror):
		print(colors.red+"name or service not known"+colors.end)