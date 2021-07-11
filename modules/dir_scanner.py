# Copyright (C) 2015 – 2021 Noa-Emil Nissinen (4shadoww)

import http.client
import socket
from core.hakkuframework import *
from core import getpath

conf = {
    "name": "dir_scanner",
    "version": "1.1",
    "shortdesc": "scans dirs from website",
    "author": "4shadoww",
    "github": "4shadoww",
    "email": "4shadoww0@gmail.com",
    "initdate": "24.2.2016",
    "lastmod": "3.1.2017",
    "apisupport": True
}

# List of variables
variables = OrderedDict((
    ('target', ['google.com', 'target address']),
    ('timeout', ['10', 'timeout (default: 10)']),
    ('pos', ['false', 'print only success[true/false]']),
))

# Simple changelog
changelog = "Version 1.0:\nrelease\n\nVersion 1.1:\n+ added timeout variable"

def run():
    variables['target'][0] = variables['target'][0].replace("http://", "")
    variables['target'][0] = variables['target'][0].replace("https://", "")
    print_info("your target : " + variables['target'][0])

    f = open(getpath.db()+'apache_users.txt', 'r')
    paths = []
    for line in f:
        paths.append(line.replace('\n', ''))
    f.close()

    try:
        paths_found = []
        if variables['pos'][0] == 'true':
            for path in paths:
                path = path.replace("\n", "")
                conn = http.client.HTTPConnection(variables['target'][0])
                try:
                    conn.timeout = float(variables['timeout'][0])
                except ValueError:
                    print_error('invalid timeout')
                    return ModuleError("invalid timeout")
                conn.request("GET", path)
                res = conn.getresponse()
                if(res.status==200):
                    print_success("[%s] ... [%s %s]" % (path, res.status, res.reason))
                    paths_found.append(path)
        else:
            for path in paths:
                path = path.replace("\n", "")
                conn = http.client.HTTPConnection(variables['target'][0])
                try:
                    conn.timeout = float(variables['timeout'][0])
                except ValueError:
                    print_error('invalid timeout')
                    return ModuleError("invalid timeout")
                conn.request("GET", path)
                res = conn.getresponse()
                if(res.status==200):
                    print_success("[%s] ... [%s %s]" % (path, res.status, res.reason))
                    paths_found.append(path)
                else:
                    print_warning("[%s] ... [%s %s]" % (path, res.status, res.reason))
    except (socket.gaierror):
        print_error("target "+variables['target'][0]+" not found")
        return ModuleError("not found")
    except (socket.timeout):
        print_error("time out "+variables['target'][0])
        return ModuleError("timeout")
