#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
import os
from core import colors
import traceback
import sys
from core.prettytable import PrettyTable

def count():
	isfile = os.path.isfile
	join = os.path.join

	directory = 'modules'
	global module_count
	module_count = sum(1 for item in os.listdir(directory) if isfile(join(directory, item)))
	module_count = module_count - 2
	count.mod = str(module_count)

def printoptions(modadd):
	try:
		print(" ")
		t = PrettyTable([colors.green+'Option', 'Value', 'Description'+colors.end])
		t.add_row(["------","------","-----------"])
		t.align = 'l'
		t.valing = 'm'
		t.border = False

		for key, val in zip(modadd.variables.items(),modadd.vdesc):
				t.add_row([key[0], key[1], val])

		print (t,'\n')
		try:
			print(modadd.option_notes,'\n')
		except(AttributeError):
			pass

	except Exception as error:
		print(colors.red+"error: module is corrupted\n")
		traceback.print_exc(file=sys.stdout)
		print(colors.end)