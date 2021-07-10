#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
from core import colors
import http.client
from core.hakkuframework import *
import socket

conf = {
    "name": "webserver_scout",
    "version": "1.0",
    "shortdesc": "get information from webserver",
    "author": "4shadoww",
    "github": "4shadoww",
    "email": "4shadoww0@gmail.com",
    "initdate": "17.5.2016",
    "lastmod": "3.1.2017",
    "apisupport": True
}

# List of the variables
variables = OrderedDict((
    ('target', ['google.com', 'target address']),
    ('timeout', ['1', 'timeout (default: 1)']),
))

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
    try:
        try:
            socket.setdefaulttimeout(float(variables['timeout'][0]))
        except ValueError:
            printError('invalid timeout')
            return ModuleError("invalid timeout")
        conn = http.client.HTTPConnection(variables['target'][0])
        conn.request("HEAD","/index.html")
        res = conn.getresponse()
        results = res.getheaders()
        print('')
        for item in results:
            print(colors.yellow+item[0], item[1]+colors.end)
        print('')
        return results
    except http.client.InvalidURL:
        printError('invalid url')
        return ("invalid url")
    except socket.gaierror:
        printError('name or service not known')
        return ModuleError("name or service not known")
    except socket.timeout:
        printError('timeout')
        return ModuleError("timeout")