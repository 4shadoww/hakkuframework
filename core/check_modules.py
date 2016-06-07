#        Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
import os

def check():
	isfile = os.path.isfile
	join = os.path.join

	directory = 'modules'
	global module_count
	module_count = sum(1 for item in os.listdir(directory) if isfile(join(directory, item)))
	module_count = module_count - 2
	check.mod = str(module_count)