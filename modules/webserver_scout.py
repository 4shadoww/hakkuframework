# Copyright (C) 2015 – 2021 Noa-Emil Nissinen (4shadoww)
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
    "initdate": "2016-05-17",
    "lastmod": "2017-01-03",
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
            print_error('invalid timeout')
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
        print_error('invalid url')
        return ("invalid url")
    except socket.gaierror:
        print_error('name or service not known')
        return ModuleError("name or service not known")
    except socket.timeout:
        print_error('timeout')
        return ModuleError("timeout")
