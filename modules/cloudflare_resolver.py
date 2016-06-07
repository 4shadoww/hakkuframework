#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)

import sys
import socket
import os
from core import bcolors
from collections import OrderedDict
from core.alert import alert


#info about module
#modules name
modulename = "cloudflare_resolver"
#version
version = "1.0"
#description
desc = "Tries to resolve ip from subdomains"
#created by
createdby = "4shadoww"
#creator's github
github = "4shadoww"
#email
email = "4shadoww0@gmail.com"

#list
variables = OrderedDict((
('target', 'google.com'),
('alert', 'false'),
('pos', 'false'),
))

vdesc = [
'target address',
'alert when done(beep)[true/false]',
'print only success[true/false]',
]

#simple changelog
changelog = bcolors.YEL+"Version 1.0:\nrelease"+bcolors.END

#run function
def run():
	variables['target'] = variables['target'].replace("http://", "")
	variables['target'] = variables['target'].replace("https://", "")
	socket.setdefaulttimeout(1)
	sub = ('mail', 'webmail', 'email', 'direct-connect-mail',
	'direct', 'direct-connect', 'cpanel', 'phpmyadmin', 'ftp', 'forum', 'blog',
	'm', 'dev', 'record', 'ssl', 'dns', 'help', 'ns', 'ns1', 'ns2',
	'ns3', 'ns4', 'irc', 'server', 'status', 'portal', 'beta',
	'admin', 'alpha', 'imap', 'smtp', 'test')
	try:
		orgip = socket.gethostbyname(variables['target'])
		print(bcolors.OKGREEN+"[-------------------------]"+bcolors.END)
		print(bcolors.OKGREEN+"[+] Default IP Address : %s"%orgip+bcolors.END)
		print(bcolors.OKGREEN+"[-------------------------]"+bcolors.END)
	except(socket.gaierror):
		print(bcolors.WARNING+"[-] Error : Host is Down !"+bcolors.END)
	for i in sub:
		host = i+'.'+variables['target']
		try:
			ip = socket.gethostbyname(host)
			print(bcolors.OKGREEN+"[+] %s : %s"%(host, ip)+bcolors.END)
		except(socket.gaierror):
			if variables['pos'] != 'true':
				print(bcolors.WARNING+"[-] %s : N/A"%host+bcolors.END)
	if variables['alert'] == 'true':
			alert('scanning ended')