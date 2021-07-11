# Copyright (C) 2015 – 2021 Noa-Emil Nissinen (4shadoww)

from core.hakkuframework import *
import socket

conf = {
    "name": "hostname_resolver",
    "version": "1.0",
    "shortdesc": "resolve hostname using ip",
    "author": "4shadoww",
    "github": "4shadoww",
    "email": "4shadoww0@gmail.com",
    "initdate": "2016-05-09",
    "lastmod": "2017-01-03",
    "apisupport": True
}

# List of the variables
variables = OrderedDict((
    ('target', ['192.168.1.1', 'target ip address']),
))

#simple changelog
changelog = "Version 1.0:\nrelease"

def run():
    try:
        querly = socket.gethostbyaddr(variables['target'][0])
        print_success("resolved hostname: "+ querly[0])
        return querly[0]
    except(socket.herror):
        print_error("unknown host")
        return ModuleError("unknown host")
    except(socket.gaierror):
        print_error("name or service not known")
        return ModuleError("name or service not known")
