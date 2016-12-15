#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
import sys
from core import colors
from collections import OrderedDict
import urllib.request
import socket
from core.messages import *
import http.client
import re

conf = {
	"name": "proxy_scout",
	"version": "1.0",
	"shortdesc": "verify http proxy",
	"author": "4shadoww",
	"github": "4shadoww",
	"email": "4shadoww0@gmail.com",
	"initdate": "19.5.2016"

}

# List of the variables
variables = OrderedDict((
	('target', '192.168.1.2'),
	('port', '80'),
	('timeout', '1'),
	('port_range', '1-100000'),
	('use_range', '0'),
	('scan_common', '0'),
))

# Description for variables
vdesc = [
	'target address',
	'target port',
	'timeout (default: 1)',
	'port range (default: 1-100000)',
	'scan port range(1=yes/0=no)',
	'scan commonly used ports(1=yes/0=no)',
]

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	commonports = ['80', '8080', '8888', '25', '3128', '8003', '9529', '8088', '8118', '4624', '9090', '82', '8090', '5555', '81', '7004', '9797', '7777', '8998', '9999', '10200']
	variables['target'] = variables['target'].replace("http://", "").replace("https://", "")
	if variables['target'] == 'google.com':
		printerror('not valid address')
		return
	try:
		try:
			socket.setdefaulttimeout(int(variables['timeout']))
		except ValueError:
			printerror('not valid timeout')
			return
		if variables['use_range'] != '1' and variables['scan_common'] != '1':
			proxy_support = urllib.request.ProxyHandler({"http":variables['target']+':'+variables['port']})
			opener = urllib.request.build_opener(proxy_support)
			urllib.request.install_opener(opener)

			html = urllib.request.urlopen("http://www.google.com").read()
			printsuccess('proxy server detected')
		if variables['scan_common'] == '1':
			for port in commonports:
				try:
					status = colors.yellow+'[*] scanning port '+ port+colors.end
					sys.stdout.write("\r%s" % status)
					sys.stdout.flush()
					proxy_support = urllib.request.ProxyHandler({"http":variables['target']+':'+port})
					opener = urllib.request.build_opener(proxy_support)
					urllib.request.install_opener(opener)

					html = urllib.request.urlopen("http://www.google.com").read()
					print(' :'+colors.green+' proxy detected'+colors.end)

				except http.client.BadStatusLine:
					printsuccess('\nproxy server detected')
					break

				except urllib.error.URLError:
					pass
				
				except socket.timeout:
					pass
				
				except ConnectionResetError:
					print(' :'+colors.green+' proxy detected'+colors.end)
			printsuccess('\ndone')

		if variables['use_range'] == '1':
			ports = re.sub("-", " ",  variables['port_range']).split()
			for port in range(int(ports[0]), int(ports[1])):
				try:
					status = colors.yellow+'[*] scanning port '+ str(port)+colors.end
					sys.stdout.write("\r%s" % status)
					sys.stdout.flush()
					proxy_support = urllib.request.ProxyHandler({"http":variables['target']+':'+str(port)})
					opener = urllib.request.build_opener(proxy_support)
					urllib.request.install_opener(opener)

					html = urllib.request.urlopen("http://www.google.com").read()
					print(' :'+colors.green+' proxy detected'+colors.end)

				except http.client.BadStatusLine:
					printsuccess('\nproxy server detected')
					break

				except urllib.error.URLError:
					pass
				
				except socket.timeout:
					pass
				
				except ConnectionResetError:
					print(' :'+colors.green+' proxy detected'+colors.end)
			printsuccess('\ndone')
			
			



	except http.client.BadStatusLine:
		printsuccess('proxy server detected')

	except urllib.error.URLError:
		printerror('URLError')
	
	except socket.timeout:
		printerror('timeout')
	
	except ConnectionResetError:
		printsuccess('proxy detected')
