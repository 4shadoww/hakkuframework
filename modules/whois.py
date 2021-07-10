# Copyright (C) 2015 – 2021 Noa-Emil Nissinen (4shadoww)
from core.hakkuframework import *
import whois

conf = {
    "name": "whois", # Module's name (should be same as file name)
    "version": "1.0", # Module version
    "shortdesc": "perform whois query", # Short description
    "github": "4shadoww", # Author's github
    "author": "4shadoww", # Author
    "email": "4shadoww0@gmail.com", # Email
    "initdate": "18.12.2016", # Initial date
    "lastmod": "29.12.2016",
    "apisupport": True
}

# List of the variables
variables = OrderedDict((
    ("target", ["google.com", "target address"]),
))

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
    # Run
    w = whois.whois(variables["target"][0])
    print(w)
    return w