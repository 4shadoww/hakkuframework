#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)

import sys
import os
from core import colors
from collections import OrderedDict
from dns import resolver
import dns



# Info about the module
#modules name
name = "cloudflare_resolver"
#version
version = "2.2"
# Description
desc = "tries to resolve ip from subdomains"
#created by
createdby = "4shadoww"
# Creator's github
github = "4shadoww"
# Email
email = "4shadoww0@gmail.com"

#list
variables = OrderedDict((
('target', 'google.com'),
('pos', 'false'),
('timeout', '0.5')
))

vdesc = [
'target address',
'print only success[true/false]',
'timeout',
]

#simple changelog
changelog = "Version 1.0:\nrelease\n\nVersion 2.0:\n+ fixed timeout bug\n+ module is now using dnspython library\n\nVersion 2.1:\n+ added more colors\n\nVersion 2.2:\n+ added ? when resolved is same than default ip\n+ added timeout variable"

# Run function
def run():
	ipresolver = resolver.Resolver()
	ipresolver.timeout = float(variables['timeout'])
	ipresolver.lifetime = float(variables['timeout'])

	variables['target'] = variables['target'].replace("http://", "")
	variables['target'] = variables['target'].replace("https://", "")
	sub = ('mail', 'webmail', 'email', 'direct-connect-mail',
	'direct', 'direct-connect', 'cpanel', 'phpmyadmin', 'ftp', 'forum', 'blog',
	'm', 'dev', 'record', 'ssl', 'dns', 'help', 'ns', 'ns1', 'ns2',
	'ns3', 'ns4', 'irc', 'server', 'status', 'portal', 'beta',
	'admin', 'alpha', 'imap', 'smtp', 'test')
	try:
		orgip = ipresolver.query(variables['target'], 'A')
		print(colors.green+"[-------------------------]"+colors.end)
		print(colors.green+"[+] Default IP Address : %s"%orgip[0]+colors.end)
		print(colors.green+"[-------------------------]"+colors.end)
	except(dns.exception.Timeout):
		print(colors.red+"[-] Error : Host is Down !"+colors.end)
	for i in sub:
		host = i+'.'+variables['target']
		try:
			query = ipresolver.query(host, 'A')
			if query[0] == orgip[0]:
				print(colors.yellow+"[?] %s : %s"%(host, query[0])+colors.end)
			else:
				print(colors.green+"[+] %s : %s"%(host, query[0])+colors.end)
		except(dns.exception.Timeout):
			if variables['pos'] != 'true':
				print(colors.red+"[-] %s : N/A"%host+colors.end)