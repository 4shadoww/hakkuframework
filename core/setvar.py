#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
import __main__
from core import bcolors

def setvar(variable, value):
	__main__.funcname.variables[variable] = value
	print(bcolors.OKGREEN+variable +" => "+ value + bcolors.END)