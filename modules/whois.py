# Copyright (C) 2015 – 2021 Noa-Emil Nissinen (4shadoww)
from core.hakkuframework import *
from whois import query

conf = {
    "name": "whois", # Module's name (should be same as file name)
    "version": "1.1", # Module version
    "shortdesc": "perform whois query", # Short description
    "github": "4shadoww", # Author's github
    "author": "4shadoww", # Author
    "email": "4shadoww0@gmail.com", # Email
    "initdate": "2016-12-18", # Initial date
    "lastmod": "2021-07-11",
    "apisupport": True,
    "dependencies": ["whois"]
}

# List of the variables
variables = OrderedDict((
    ("target", ["google.com", "target address"]),
))

# Simple changelog
changelog = "Version 1.0:\nrelease\nVersion 1.1:\nfixes"

def run():
    # Run
    print("loading records for", variables["target"][0])
    w = query(variables["target"][0])
    print("creationg date:\t\t", w.creation_date)
    print("expiration date:\t", w.expiration_date)
    print("last updated:\t\t", w.last_updated)
    print("name:\t\t\t", w.name)
    print("name servers:\t\t", w.name_servers)
    print("registrant:\t\t", w.registrant)
    print("registrant country:\t", w.registrant_country)
    print("registrar:\t\t", w.registrant)
    print("status:\t\t\t", w.status)
    print("statuses:\t\t", w.statuses)
    print("dnssec:\t\t\t", w.dnssec)

    return w
