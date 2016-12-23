#		Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)

saveddict = None

def save_values(variables):
	global saveddict
	saveddict = variables

def set_values(tdict):
	global saveddict

	for key0 in saveddict.keys():
		for key1 in tdict.keys():
			if key0 == key1:
				tdict[key0][0] = saveddict[key0][0]