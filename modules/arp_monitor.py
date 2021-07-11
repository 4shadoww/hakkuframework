# Copyright (C) 2015 – 2021 Noa-Emil Nissinen (4shadoww)

from core.hakkuframework import *
import scapy.all as scapy

conf = {
    "name": "arp_monitor", # Module's name (should be same as file name)
    "version": "1.0", # Module version
    "shortdesc": "arp packet monitor", # Short description
    "github": "4shadoww", # Author's github
    "author": "4shadoww", # Author
    "email": "4shadoww0@gmail.com", # Email
    "initdate": "2016-12-31", # Initial date
    "lastmod": "2021-07-11", # Last modification
    "apisupport": False, # Api support
    "needroot": 1, # Alert user if root permissions not available (remove variable below if root permissions not needed)
}

# List of the variables
variables = OrderedDict((
    
))

# Additional notes to options
option_notes = " this module doesn't have any options"

# Simple changelog
changelog = "Version 1.0:\nrelease"

def arp_display(pkt):
    if pkt[scapy.ARP].op == 1: #who-has (request)
        return "Request: " + pkt[scapy.ARP].psrc + " is asking about " + pkt[scapy.ARP].pdst
    if pkt[scapy.ARP].op == 2: #is-at (response)
        return "*Response: " + pkt[scapy.ARP].hwsrc + " has address " + pkt[scapy.ARP].psrc

# Run function
def run():
    print_info("starting arp monitor...")
    print_info("ctrl + c to end")
    print(scapy.sniff(prn=arp_display, filter="arp", store=0))
    print_info("monitoring ended")
