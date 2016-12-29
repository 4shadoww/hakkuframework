#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)

from core.hakkuframework import *

# Info about the module

conf = {
	"name": "test", # Module's name (should be same as file's name)
	"version": "1.0", # Module version
	"shortdesc": "only test", # Short description
	"author": "4shadoww", # Author
	"github": "4shadoww", # Author's github
	"email": "4shadoww0@gmail.com", # Email
	"initdate": "24.2.2016", # Initial date
	"lastmod": "29.12.2016",
	"apisupport": True, # Api support

	"message": "hello"
}

# List of the variables
variables = OrderedDict((
	("value", [0, "description"]),
))

customcommands = {
	"test": "test"
}

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	print(variables['value'][0])
	print(variables['value'][1])
	printWarning("warning")
	return variables

def test(args):
	return "ok"