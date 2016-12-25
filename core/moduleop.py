#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
import os
from core import colors
import traceback
import sys
from prettytable import PrettyTable
from core import getpath

def count():
	isfile = os.path.isfile
	join = os.path.join

	directory = getpath.modules()
	global module_count
	module_count = sum(1 for item in os.listdir(directory) if isfile(join(directory, item)))
	module_count = module_count - 1
	count.mod = str(module_count)

def printoptions(modadd):
	try:
		print(" ")
		t = PrettyTable([colors.red +'Option', 'Value', 'Description'+colors.end])
		t.add_row(["------","------","-----------"])
		t.align = 'l'
		t.valing = 'm'
		t.border = False

		for key, val in modadd.variables.items():
				t.add_row([key, val[0], val[1]])

		print (t,'\n')
		try:
			print(modadd.option_notes,'\n')
		except(AttributeError):
			pass

	except Exception as error:
		print(colors.red+"error: module is corrupted\n")
		traceback.print_exc(file=sys.stdout)
		print(colors.end)