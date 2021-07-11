# Copyright (C) 2015 – 2021 Noa-Emil Nissinen (4shadoww)

from core.hakkuframework import *
from core import getpath
import http.client
import socket

conf = {
    "name": "apache_users", # Module's name (should be same as file's name)
    "version": "1.1", # Module version
    "shortdesc": "scan directory of apache users", # Short description
    "github": "4shadoww", # Author's github
    "author": "4shadoww", # Author
    "email": "4shadoww0@gmail.com",
    "initdate": "2016-03-01",
    "lastmod": "2021-07-11",
    "apisupport": True
}

# List of the variables
variables = OrderedDict((
    ("target", ["google.com", "target address"]),
))

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
    variables['target'][0] = variables['target'][0].replace("http://", "")
    variables['target'][0] = variables['target'][0].replace("https://", "")
    print_info("your target : " + variables['target'][0])
    print_info("loading path list...")

    f = open(getpath.db()+'apache_users.txt', 'r')
    paths = []
    for line in f:
        paths.append(line.replace('\n', ''))
    f.close()

    try:
        paths_found = []
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
        print_error("host is down")
        return ModuleError("host is down")
