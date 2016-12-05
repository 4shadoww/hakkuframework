#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)

import sys
from core import colors
from collections import OrderedDict
from core import getpath

# Info about the module
# Module's name (should be same as file's name)
name = "test"
# Module version
version = "1.0"
# Description
desc = "only test"
#created by
createdby = "4shadoww"
# Creator's github
github = "4shadoww"
# Email
email = "4shadoww0@gmail.com"

message = "hello!"

#list
variables = OrderedDict((
('value', 0),
))
# Description for variables
vdesc = [
'description',
]

#simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	print(variables['value'])
