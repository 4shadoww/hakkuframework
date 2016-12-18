#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
from core import colors

def setvar(variable, value, variables):
	variables[variable][0] = value
	print(colors.green+variable +" => "+ value + colors.end)