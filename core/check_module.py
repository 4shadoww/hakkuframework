#		 Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)

from core import colors
import sys
from glob import glob

def testfailed():
	print(colors.red+"\ntest not passed!\n"+colors.end)

def check():
	try:
		global modadd

		print(colors.yellow+'\nchecking',modadd.conf["name"]+colors.end)

		modadd.conf["version"]
		if modadd.conf["shortdesc"] == 'modules_description':
			print(colors.red+'\ndesc variable has default value'+colors.end)
			testfailed()
		if modadd.conf["github"] == 'mygithub':
				print(colors.red+'\ngithub variable has default value'+colors.end)
				testfailed()
		if modadd.conf["author"] == 'creators_name':
			print(colors.red+'\ncreatedby variable has default value'+colors.end)
			testfailed()
		if modadd.conf["email"] == 'creators@email.com':
			print(colors.red+'\nemail variable has default value'+colors.end)
			testfailed()

		for item in modadd.variables.items():
			if item[0] == 'option1' or item[0] == 'option2' or item[1] == 'none1' or item[1] == 'none2':
				print(colors.red+'\nvariables has default value')
				testfailed()

		for desc in modadd.vdesc:
			if desc == 'description1' or desc == 'description2':
				print(colors.red+'\ndesc list has default value'+colors.end)
				testfailed()
		if len(modadd.variables) != len(modadd.vdesc):
			print(colors.red+'\nvdesc has not same amount of items than variables')
			testfailed()

		modadd.changelog
		modadd.run

		print(colors.green+'\ntest passed'+colors.end)
	except:
		print(colors.red+"error:\n")
		traceback.print_exc()
		print(colors.end)

	try:
		modadd.customcommands
		check_customcommands()
	except AttributeError:
		pass