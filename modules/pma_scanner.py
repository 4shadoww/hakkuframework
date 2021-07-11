# Copyright (C) 2015 – 2021 Noa-Emil Nissinen (4shadoww)

from core.hakkuframework import *
import http.client
import socket

conf = {
    "name": "pma_scanner",
    "version": "1.0",
    "shortdesc": "PHPMyAdmin login page scanner",
    "author": "4shadoww",
    "github": "4shadoww",
    "email": "4shadoww0@gmail.com",
    "initdate": "2016-03-01",
    "lastmod": "2017-01-03",
    "apisupport": True
}

# List of the variables
variables = OrderedDict((
    ('target', ['google.com', 'target address']),
))

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
    variables['target'][0] = variables['target'][0].replace("http://", "")
    variables['target'][0] = variables['target'][0].replace("https://", "")
    print_info("your target : " + variables['target'][0])
    print_info("loading path list... please wait...")
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
    print_info("starting scan...")
    paths_found = []
    try:
        for path in paths:
            path = path.replace("\n", "")
            conn = http.client.HTTPConnection(variables['target'][0])
            conn.request("GET", path)
            res = conn.getresponse()
            if(res.status==200):
                print_success("[%s] ... [%s %s]" % (path, res.status, res.reason))
                paths_found.append(path)
            else:
                print_warning("[%s] ... [%s %s]" % (path, res.status, res.reason))
        return paths_found
    except(socket.gaierror):
        print_error("host is down!")
        return ModuleError("host is down")
    except socket.timeout:
        print_error("timeout")
        return ModuleError("timeout")
