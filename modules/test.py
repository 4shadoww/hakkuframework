#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)

import sys
from core import bcolors
from collections import OrderedDict
from core import getpath

#info about module
#modules name (must be same as filename)
modulename = "test"
#module version
version = "1.0"
#description
desc = "only test"
#created by
createdby = "4shadoww"
#creator's github
github = "4shadoww"
#email
email = "4shadoww0@gmail.com"

message = "hello!"


#list
variables = OrderedDict((
('value', 0),

))
#description for variables
vdesc = [
'description1',
]

#simple changelog
changelog = bcolors.YEL+"Version 1.0:\nrelease"+bcolors.END



def run():
	print(variables['value'])