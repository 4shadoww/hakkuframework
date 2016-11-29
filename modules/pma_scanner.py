#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
import sys
from core import colors
from collections import OrderedDict
import http.client
from time import sleep
import socket

# Info about the module
# Module's name (should be same as file's name)
name = "pma_scanner"
# Module version
version = "1.0"
# Description
desc = "PHPMyAdmin login page scanner"
# Creator's github
github = "4shadoww"
# Creator's name
createdby = "4shadoww"
# Email
email = "4shadoww0@gmail.com"

# List of the variables
variables = OrderedDict((
('target', 'google.com'),
))

# Description for variables
vdesc = [
'target address',
]

#simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	variables['target'] = variables['target'].replace("http://", "")
	variables['target'] = variables['target'].replace("https://", "")
	print(colors.green + "[*]Your Target : " + variables['target'] + colors.end)
	print(colors.blue + "[*]Loading Path List ... Please Wait ..." + colors.end)
	sleep(2)
	paths = ['/phpMyAdmin/',
'/phpmyadmin/',
'/PMA/',
'/admin/',
'/dbadmin/',
'/mysql/',
'/myadmin/',
'/phpmyadmin2/',
'/phpMyAdmin2/',
'/phpMyAdmin-2/',
'/php-my-admin/',
'/phpMyAdmin-2.2.3/',
'/phpMyAdmin-2.2.6/',
'/phpMyAdmin-2.5.1/',
'/phpMyAdmin-2.5.4/',
'/phpMyAdmin-2.5.5-rc1/',
'/phpMyAdmin-2.5.5-rc2/',
'/phpMyAdmin-2.5.5/',
'/phpMyAdmin-2.5.5-pl1/',
'/phpMyAdmin-2.5.6-rc1/',
'/phpMyAdmin-2.5.6-rc2/',
'/phpMyAdmin-2.5.6/',
'/phpMyAdmin-2.5.7/',
'/phpMyAdmin-2.5.7-pl1/',
'/phpMyAdmin-2.6.0-alpha/',
'/phpMyAdmin-2.6.0-alpha2/',
'/phpMyAdmin-2.6.0-beta1/',
'/phpMyAdmin-2.6.0-beta2/',
'/phpMyAdmin-2.6.0-rc1/',
'/phpMyAdmin-2.6.0-rc2/',
'/phpMyAdmin-2.6.0-rc3/',
'/phpMyAdmin-2.6.0/',
'/phpMyAdmin-2.6.0-pl1/',
'/phpMyAdmin-2.6.0-pl2/',
'/phpMyAdmin-2.6.0-pl3/',
'/phpMyAdmin-2.6.1-rc1/',
'/phpMyAdmin-2.6.1-rc2/',
'/phpMyAdmin-2.6.1/',
'/phpMyAdmin-2.6.1-pl1/',
'/phpMyAdmin-2.6.1-pl2/',
'/phpMyAdmin-2.6.1-pl3/',
'/phpMyAdmin-2.6.2-rc1/',
'/phpMyAdmin-2.6.2-beta1/',
'/phpMyAdmin-2.6.2-rc1/',
'/phpMyAdmin-2.6.2/',
'/phpMyAdmin-2.6.2-pl1/',
'/phpMyAdmin-2.6.3/',
'/phpMyAdmin-2.6.3-rc1/',
'/phpMyAdmin-2.6.3/',
'/phpMyAdmin-2.6.3-pl1/',
'/phpMyAdmin-2.6.4-rc1/',
'/phpMyAdmin-2.6.4-pl1/',
'/phpMyAdmin-2.6.4-pl2/',
'/phpMyAdmin-2.6.4-pl3/',
'/phpMyAdmin-2.6.4-pl4/',
'/phpMyAdmin-2.6.4/',
'/phpMyAdmin-2.7.0-beta1/',
'/phpMyAdmin-2.7.0-rc1/',
'/phpMyAdmin-2.7.0-pl1/',
'/phpMyAdmin-2.7.0-pl2/',
'/phpMyAdmin-2.7.0/',
'/phpMyAdmin-2.8.0-beta1/',
'/phpMyAdmin-2.8.0-rc1/',
'/phpMyAdmin-2.8.0-rc2/',
'/phpMyAdmin-2.8.0/',
'/phpMyAdmin-2.8.0.1/',
'/phpMyAdmin-2.8.0.2/',
'/phpMyAdmin-2.8.0.3/',
'/phpMyAdmin-2.8.0.4/',
'/phpMyAdmin-2.8.1-rc1/',
'/phpMyAdmin-2.8.1/',
'/phpMyAdmin-2.8.2/',
'/sqlmanager/',
'/mysqlmanager/',
'/p/m/a/',
'/PMA2005/',
'/pma2005/',
'/phpmanager/',
'/php-myadmin/',
'/phpmy-admin/',
'/webadmin/',
'/sqlweb/',
'/websql/',
'/webdb/',
'/mysqladmin/',
'/mysql-admin/',]
	print(colors.blue+"[*]Starting scan..."+colors.end)
	try:
		for path in paths:
			path = path.replace("\n", "")
			conn = http.client.HTTPConnection(variables['target'])
			conn.request("GET", path)
			res = conn.getresponse()
			if(res.status==200):
				print(colors.bold + colors.green + "[%s] ... [%s %s]" % (path, res.status, res.reason) + colors.end)
			else:
				print(colors.yellow + "[%s] ... [%s %s]" % (path, res.status, res.reason) + colors.end)
	except(socket.gaierror):
		print(colors.red+"[!]Host is down!"+colors.end)