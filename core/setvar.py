#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
import __main__
from core import colors

def setvar(variable, value):
	__main__.funcname.variables[variable] = value
	print(colors.green+variable +" => "+ value + colors.end)