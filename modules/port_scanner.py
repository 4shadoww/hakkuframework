# Copyright (C) 2015 – 2021 Noa-Emil Nissinen (4shadoww)
from core.hakkuframework import *
from core import colors
import socket
import subprocess
from datetime import datetime

conf = {
    "name": "port_scanner",
    "version": "1.0",
    "shortdesc": "scan open ports",
    "author": "4shadoww",
    "github": "4shadoww",
    "email": "4shadoww0@gmail.com",
    "initdate": "2016-03-04",
    "lastmod": "2017-01-03",
    "apisupport": True
}

# List of the variables
variables = OrderedDict((
    ('target', ['google.com', 'target address']),
    ('first', [1, 'first port which will be scanned']),
    ('last', [100, 'last port which will be scanned']),
))

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
    open_ports = []
    variables['target'][0] = variables['target'][0].replace("http://", "")
    variables['target'][0] = variables['target'][0].replace("https://", "")
    try:
        targetip = socket.gethostbyname(variables['target'][0])
    except(socket.gaierror):
        print_error('hostname could not be resolved')
        return ModuleError("hostname could not be resolved")

    socket.setdefaulttimeout(0.5)

    print(colors.blue+"-" * 60)
    print("please wait, scanning target", targetip)
    print("-" * 60+colors.end)

    t1 = datetime.now()

    end = variables['last'][0] + 1

    try:
        for port in range(int(variables['first'][0]),int(end)):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((targetip, port))
            if result == 0:
                print(colors.green+"Port {}: Open".format(port)+colors.end)
                open_ports.append(port)
            else:
                print(colors.red+"Port {}: Closed".format(port)+colors.end)

            sock.close()

    except(socket.gaierror):
        print_error('hostname could not be resolved')
        return ModuleError("hostname could not be resolved")
    except(socket.error):
        print_error(colors.red+"couldn't connect to server"+colors.end)
        return ModuleError("couldn't connect to server")
    except(ValueError):
        print_error("port value must be integer")
        return ModuleError("port value must be integer")

    # Checking the time again
    t2 = datetime.now()

    # Calculates the difference of time, to see how long it took to run the script
    total =  t2 - t1

    # Printing the information to screen
    print_info('scanning Completed in: '+ str(total))
    return open_ports
